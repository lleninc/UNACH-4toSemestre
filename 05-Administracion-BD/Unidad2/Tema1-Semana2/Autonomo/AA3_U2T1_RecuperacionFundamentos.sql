/*
AA3 - ADMINISTRACION DE BASES DE DATOS - U2T1
Implementacion de estrategias de consistencia, control de concurrencia
y respaldos basicos en SQL Server.

Autor: <TU NOMBRE>
Fecha: <FECHA>

NOTA:
- Ejecuta por bloques (GO) y, en concurrencia, usa DOS sesiones separadas.
- Ajusta la ruta de respaldo a una carpeta existente con permisos.
*/

/* ============================================================
   0) CREACION DE BASE DE DATOS
   ============================================================ */
USE master;
GO

IF DB_ID('RecuperacionFundamentos') IS NOT NULL
BEGIN
    ALTER DATABASE RecuperacionFundamentos SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE RecuperacionFundamentos;
END
GO

CREATE DATABASE RecuperacionFundamentos;
GO

ALTER DATABASE RecuperacionFundamentos SET RECOVERY FULL;
GO

USE RecuperacionFundamentos;
GO

/* ============================================================
   1) ESQUEMA AMPLIADO (INCLUYE MAS TABLAS)
   Tablas base solicitadas:
   - Departamentos
   - Empleados
   Tablas adicionales:
   - Cargos
   - Proyectos
   - EmpleadoProyecto
   - HistorialSalario
   - BitacoraCambios
   ============================================================ */

CREATE TABLE dbo.Departamentos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL UNIQUE,
    presupuesto DECIMAL(14,2) NOT NULL CHECK (presupuesto >= 0),
    estado VARCHAR(20) NOT NULL DEFAULT 'ACTIVO' CHECK (estado IN ('ACTIVO', 'INACTIVO'))
);
GO

CREATE TABLE dbo.Cargos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(80) NOT NULL UNIQUE,
    salario_min DECIMAL(10,2) NOT NULL CHECK (salario_min > 0),
    salario_max DECIMAL(10,2) NOT NULL CHECK (salario_max > salario_min)
);
GO

CREATE TABLE dbo.Empleados (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL,
    salario DECIMAL(10,2) NOT NULL CHECK (salario > 0),
    departamento_id INT NOT NULL,
    cargo_id INT NOT NULL,
    fecha_ingreso DATE NOT NULL DEFAULT CAST(GETDATE() AS DATE),
    email VARCHAR(150) NULL UNIQUE,
    CONSTRAINT FK_Empleados_Departamentos FOREIGN KEY (departamento_id) REFERENCES dbo.Departamentos(id),
    CONSTRAINT FK_Empleados_Cargos FOREIGN KEY (cargo_id) REFERENCES dbo.Cargos(id)
);
GO

CREATE TABLE dbo.Proyectos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(120) NOT NULL UNIQUE,
    departamento_id INT NOT NULL,
    presupuesto DECIMAL(14,2) NOT NULL CHECK (presupuesto > 0),
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'PLANIFICADO' CHECK (estado IN ('PLANIFICADO','EN_EJECUCION','CERRADO')),
    CONSTRAINT FK_Proyectos_Departamentos FOREIGN KEY (departamento_id) REFERENCES dbo.Departamentos(id),
    CONSTRAINT CK_Proyectos_Fechas CHECK (fecha_fin IS NULL OR fecha_fin >= fecha_inicio)
);
GO

CREATE TABLE dbo.EmpleadoProyecto (
    empleado_id INT NOT NULL,
    proyecto_id INT NOT NULL,
    rol VARCHAR(80) NOT NULL,
    horas_asignadas INT NOT NULL CHECK (horas_asignadas > 0),
    fecha_asignacion DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    CONSTRAINT PK_EmpleadoProyecto PRIMARY KEY (empleado_id, proyecto_id),
    CONSTRAINT FK_EmpleadoProyecto_Empleado FOREIGN KEY (empleado_id) REFERENCES dbo.Empleados(id),
    CONSTRAINT FK_EmpleadoProyecto_Proyecto FOREIGN KEY (proyecto_id) REFERENCES dbo.Proyectos(id)
);
GO

CREATE TABLE dbo.HistorialSalario (
    id INT IDENTITY(1,1) PRIMARY KEY,
    empleado_id INT NOT NULL,
    salario_anterior DECIMAL(10,2) NOT NULL,
    salario_nuevo DECIMAL(10,2) NOT NULL,
    fecha_cambio DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    usuario_cambio VARCHAR(120) NOT NULL DEFAULT SUSER_SNAME(),
    CONSTRAINT FK_HistorialSalario_Empleado FOREIGN KEY (empleado_id) REFERENCES dbo.Empleados(id),
    CONSTRAINT CK_HistorialSalario_Valores CHECK (salario_anterior > 0 AND salario_nuevo > 0)
);
GO

CREATE TABLE dbo.BitacoraCambios (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    tabla VARCHAR(80) NOT NULL,
    operacion VARCHAR(20) NOT NULL,
    clave VARCHAR(120) NOT NULL,
    fecha_evento DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    detalle VARCHAR(4000) NULL
);
GO

/* Trigger de auditoria basico para Empleados */
CREATE TRIGGER trg_Empleados_Audit
ON dbo.Empleados
AFTER INSERT, UPDATE, DELETE
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (SELECT 1 FROM inserted) AND EXISTS (SELECT 1 FROM deleted)
    BEGIN
        INSERT INTO dbo.BitacoraCambios(tabla, operacion, clave, detalle)
        SELECT 'Empleados', 'UPDATE', CAST(i.id AS VARCHAR(120)),
               CONCAT('Nombre=', i.nombre, '; Salario=', i.salario)
        FROM inserted i;
    END
    ELSE IF EXISTS (SELECT 1 FROM inserted)
    BEGIN
        INSERT INTO dbo.BitacoraCambios(tabla, operacion, clave, detalle)
        SELECT 'Empleados', 'INSERT', CAST(i.id AS VARCHAR(120)),
               CONCAT('Nombre=', i.nombre, '; Salario=', i.salario)
        FROM inserted i;
    END
    ELSE IF EXISTS (SELECT 1 FROM deleted)
    BEGIN
        INSERT INTO dbo.BitacoraCambios(tabla, operacion, clave, detalle)
        SELECT 'Empleados', 'DELETE', CAST(d.id AS VARCHAR(120)),
               CONCAT('Nombre=', d.nombre, '; Salario=', d.salario)
        FROM deleted d;
    END
END;
GO

/* ============================================================
   2) DATOS VALIDOS (CONSISTENCIA CORRECTA)
   ============================================================ */

INSERT INTO dbo.Departamentos(nombre, presupuesto, estado)
VALUES
('TI', 200000, 'ACTIVO'),
('FINANZAS', 180000, 'ACTIVO'),
('RRHH', 90000, 'ACTIVO'),
('OPERACIONES', 150000, 'ACTIVO');
GO

INSERT INTO dbo.Cargos(nombre, salario_min, salario_max)
VALUES
('Analista', 800, 1800),
('Desarrollador', 1200, 3200),
('Jefe de Area', 2200, 5000),
('Asistente', 600, 1200);
GO

INSERT INTO dbo.Empleados(nombre, salario, departamento_id, cargo_id, email)
VALUES
('Ana Torres', 1500, 1, 2, 'ana.torres@empresa.com'),
('Luis Mendez', 2600, 2, 3, 'luis.mendez@empresa.com'),
('Maria Paredes', 1000, 3, 4, 'maria.paredes@empresa.com');
GO

INSERT INTO dbo.Proyectos(nombre, departamento_id, presupuesto, fecha_inicio, fecha_fin, estado)
VALUES
('ERP Interno', 1, 85000, '2025-01-10', NULL, 'EN_EJECUCION'),
('Optimizacion Costos', 2, 45000, '2025-02-01', NULL, 'EN_EJECUCION'),
('Capacitacion 2025', 3, 12000, '2025-03-01', '2025-09-30', 'PLANIFICADO');
GO

INSERT INTO dbo.EmpleadoProyecto(empleado_id, proyecto_id, rol, horas_asignadas)
VALUES
(1, 1, 'Backend', 120),
(2, 2, 'Lider', 80),
(3, 3, 'Coordinacion', 60);
GO

/* ============================================================
   3) PRUEBAS DE CONSISTENCIA (REGISTROS INVALIDOS)
   ============================================================ */

PRINT '--- Prueba A: salario negativo (debe fallar por CHECK) ---';
BEGIN TRY
    INSERT INTO dbo.Empleados(nombre, salario, departamento_id, cargo_id, email)
    VALUES('Empleado Invalido Salario', -500, 1, 1, 'invalido.salario@empresa.com');
END TRY
BEGIN CATCH
    PRINT CONCAT('ERROR CONTROLADO A: ', ERROR_MESSAGE());
END CATCH;
GO

PRINT '--- Prueba B: departamento inexistente (debe fallar por FOREIGN KEY) ---';
BEGIN TRY
    INSERT INTO dbo.Empleados(nombre, salario, departamento_id, cargo_id, email)
    VALUES('Empleado Invalido FK', 1200, 9999, 1, 'invalido.fk@empresa.com');
END TRY
BEGIN CATCH
    PRINT CONCAT('ERROR CONTROLADO B: ', ERROR_MESSAGE());
END CATCH;
GO

/* ============================================================
   4) CONTROL DE CONCURRENCIA (EJECUTAR EN 2 SESIONES)
   ============================================================ */

/*
CASO 1: LECTURA SUCIA (READ UNCOMMITTED)
-----------------------------------------
Sesion 1:
    BEGIN TRAN;
    UPDATE dbo.Empleados SET salario = salario + 500 WHERE id = 1;
    -- NO hacer COMMIT aun

Sesion 2:
    SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
    BEGIN TRAN;
    SELECT id, nombre, salario FROM dbo.Empleados WHERE id = 1;
    COMMIT;

Sesion 1:
    ROLLBACK;

Resultado esperado:
Sesion 2 puede ver un valor no confirmado (lectura sucia).

Solucion:
Usar READ COMMITTED o superior en Sesion 2.
*/

/*
CASO 2: LECTURA NO REPETIBLE
----------------------------
Sesion 1:
    SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
    BEGIN TRAN;
    SELECT salario FROM dbo.Empleados WHERE id = 1;
    -- esperar

Sesion 2:
    UPDATE dbo.Empleados SET salario = salario + 100 WHERE id = 1;
    COMMIT;

Sesion 1:
    SELECT salario FROM dbo.Empleados WHERE id = 1;
    COMMIT;

Resultado esperado:
Dos lecturas distintas en Sesion 1.

Solucion:
Usar REPEATABLE READ para mantener lectura estable de filas leidas.
*/

/*
CASO 3: LECTURA FANTASMA
------------------------
Sesion 1:
    SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
    BEGIN TRAN;
    SELECT COUNT(*) AS total_ti FROM dbo.Empleados WHERE departamento_id = 1;
    -- esperar

Sesion 2:
    INSERT INTO dbo.Empleados(nombre, salario, departamento_id, cargo_id, email)
    VALUES('Nuevo TI', 1400, 1, 1, 'nuevo.ti@empresa.com');
    COMMIT;

Sesion 1:
    SELECT COUNT(*) AS total_ti FROM dbo.Empleados WHERE departamento_id = 1;
    COMMIT;

Resultado esperado:
Puede aparecer una fila adicional (fantasma).

Solucion:
Usar SERIALIZABLE para bloquear rango y evitar inserciones fantasma.
*/

/* ============================================================
   5) COPIAS DE SEGURIDAD (FULL, DIFERENCIAL, LOG)
   ============================================================ */

DECLARE @RutaBase NVARCHAR(400) = N'E:\Backups\RecuperacionFundamentos\';
-- Asegurate de que la carpeta exista en el servidor SQL y tenga permisos.

-- FULL
BACKUP DATABASE RecuperacionFundamentos
TO DISK = @RutaBase + N'RecuperacionFundamentos_FULL.bak'
WITH INIT, FORMAT, NAME = 'FULL RecuperacionFundamentos', STATS = 5;
GO

-- Cambios posteriores al FULL
UPDATE dbo.Empleados SET salario = salario + 50 WHERE id = 2;
INSERT INTO dbo.Proyectos(nombre, departamento_id, presupuesto, fecha_inicio, fecha_fin, estado)
VALUES ('Tablero KPI', 2, 30000, '2025-05-12', NULL, 'EN_EJECUCION');
GO

-- DIFERENCIAL
BACKUP DATABASE RecuperacionFundamentos
TO DISK = N'E:\Backups\RecuperacionFundamentos\RecuperacionFundamentos_DIFF.bak'
WITH DIFFERENTIAL, INIT, NAME = 'DIFF RecuperacionFundamentos', STATS = 5;
GO

-- Nuevos cambios para LOG
UPDATE dbo.Empleados SET salario = salario + 30 WHERE id = 1;
INSERT INTO dbo.HistorialSalario(empleado_id, salario_anterior, salario_nuevo)
VALUES (1, 1500, 1530);
GO

-- LOG (incremental transaccional)
BACKUP LOG RecuperacionFundamentos
TO DISK = N'E:\Backups\RecuperacionFundamentos\RecuperacionFundamentos_LOG.trn'
WITH INIT, NAME = 'LOG RecuperacionFundamentos', STATS = 5;
GO

/*
VENTAJAS / LIMITACIONES (resumen rapido)
- FULL: restauracion simple y rapida; consume mas tiempo/espacio.
- DIFERENCIAL: restauracion mas rapida que incremental; crece hasta siguiente full.
- LOG: minimo impacto y alta granularidad de recuperacion; requiere cadena de logs y recovery model FULL.
*/

/* ============================================================
   6) PLAN DE RESPALDO Y ESTRATEGIA DE RECUPERACION
   ============================================================ */

/*
PLAN PROPUESTO (RecuperacionFundamentos)
- Full: domingo 02:00
- Diferencial: diario 22:00
- Log: cada 30 minutos (horario laboral)

ALMACENAMIENTO
- Local: E:\Backups\RecuperacionFundamentos\ (retencion 30 dias)
- Nube/Sitio externo: copia semanal cifrada (retencion 6-12 meses)

RPO / RTO
- RPO: 30 minutos (perdida maxima aceptable)
- RTO: 2 horas (tiempo maximo de restauracion)

PRUEBAS DE RESTAURACION
- Simulacro mensual en entorno de pruebas:
    1) Restaurar FULL
    2) Aplicar ultimo DIFF
    3) Aplicar LOG hasta punto objetivo
    4) Validar conteos y sumas criticas

AUTOMATIZACION
- SQL Server Agent con jobs:
    - Job_Full_Semanal
    - Job_Diff_Diario
    - Job_Log_30min
- Alertas por correo en caso de error.
*/

/* ============================================================
   7) CONSULTAS DE VERIFICACION FINAL
   ============================================================ */

SELECT 'Departamentos' AS tabla, COUNT(*) AS total FROM dbo.Departamentos
UNION ALL
SELECT 'Cargos', COUNT(*) FROM dbo.Cargos
UNION ALL
SELECT 'Empleados', COUNT(*) FROM dbo.Empleados
UNION ALL
SELECT 'Proyectos', COUNT(*) FROM dbo.Proyectos
UNION ALL
SELECT 'EmpleadoProyecto', COUNT(*) FROM dbo.EmpleadoProyecto
UNION ALL
SELECT 'HistorialSalario', COUNT(*) FROM dbo.HistorialSalario
UNION ALL
SELECT 'BitacoraCambios', COUNT(*) FROM dbo.BitacoraCambios;
GO

SELECT TOP 20 * FROM dbo.BitacoraCambios ORDER BY id DESC;
GO
