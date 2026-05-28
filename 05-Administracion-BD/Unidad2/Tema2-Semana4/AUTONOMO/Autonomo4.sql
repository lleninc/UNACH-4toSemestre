-- ============================================================================
-- TRABAJO AUTÓNOMO 4 - ADMINISTRACIÓN DE BASES DE DATOS
-- PARTE 1: LOGS DE TRANSACCIONES Y RECUPERACIÓN PUNTO EN EL TIEMPO (PITR)
-- ============================================================================

-- 1.1. CREACIÓN DE LA BASE DE DATOS Y CONFIGURACIÓN DEL LOG
USE master;
GO

IF EXISTS (SELECT name FROM sys.databases WHERE name = N'Hospital_LL')
    DROP DATABASE Hospital_LL;
GO

CREATE DATABASE Hospital_LL;
GO

-- Configurar el Modelo de Recuperación Completo (Full Recovery Model)
-- Esto es indispensable para activar el registro detallado en el Log de Transacciones
ALTER DATABASE Hospital_LL SET RECOVERY FULL;
GO

USE Hospital_LL;
GO

-- 1.2. CREACIÓN DE LAS 3 TABLAS REQUERIDAS
CREATE TABLE Medicos (
    MedicoID INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Especialidad VARCHAR(50) NOT NULL
);

CREATE TABLE Pacientes (
    PacienteID INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100) NOT NULL,
    Edad INT NOT NULL,
    Ciudad VARCHAR(50) NOT NULL
);

CREATE TABLE Citas (
    CitaID INT PRIMARY KEY IDENTITY(1,1),
    PacienteID INT FOREIGN KEY REFERENCES Pacientes(PacienteID),
    MedicoID INT FOREIGN KEY REFERENCES Medicos(MedicoID),
    FechaHora DATETIME NOT NULL,
    Motivo VARCHAR(255)
);
GO

-- Insertar datos iniciales
INSERT INTO Medicos (Nombre, Especialidad) VALUES ('Dr. Carlos Andrade', 'Cardiología'), ('Dra. Maria Elena', 'Pediatría');
INSERT INTO Pacientes (Nombre, Edad, Ciudad) VALUES ('Juan Perez', 34, 'Quito'), ('Ana Maria', 28, 'Guayaquil'), ('Luis Torres', 45, 'Cuenca');


-- 1.3. CONFIGURACIÓN INICIAL (Respaldo Completo Base)
-- Es obligatorio realizar un primer backup completo para iniciar la cadena de logs.
BACKUP DATABASE Hospital_LL 
TO DISK = 'C:\Backups\Full\Hospital_LL_Full.bak' 
WITH INIT, FORMAT, NAME = 'Backup Completo Inicial';
GO

select * from Citas
select * from Pacientes

-- 1.4. OPERACIONES DE INSERCIÓN, ACTUALIZACIÓN Y ELIMINACIÓN (Registro en el Log)

INSERT INTO Citas (PacienteID, MedicoID, FechaHora, Motivo) 
VALUES (1, 1, '26-05-2026 09:00:00', 'Chequeo de rutina'),
       (2, 2, '26-05-2026 10:30:00', 'Control pediátrico');
GO

-- Simulación de tiempo transcurrido y transacciones legítimas adicionales
-- Digamos que esto ocurre exactamente a las 21:55:00
WAITFOR DELAY '00:00:02'; -- Pausa para separar tiempos
INSERT INTO Pacientes (Nombre, Edad, Ciudad) VALUES ('Marta Gomez', 52, 'Manta'); -- Registro ingresado OKZ
GO
select * from Pacientes

-- Realizamos un respaldo del log para resguardar estas operaciones 
BACKUP LOG Hospital_LL 
TO DISK = 'C:\Backups\Trn\Hospital_LL_Log1.trn' 
WITH INIT, NAME = 'Respaldo de Log Operaciones';
GO


-- 1.5. SIMULACIÓN DEL ERROR HUMANO (PÉRDIDA PARCIAL / BORRADO MASIVO)
-- Escenario: El administrador pretendía borrar el registro de Marta Gomez, 
-- pero olvidó la cláusula WHERE a las 22:02:00, vaciando toda la tabla de Pacientes.

SELECT GETDATE() AS 'Hora_Antes_Del_Error'; 
-- Suponiendo que la consulta arrojó: 2026-05-27 2159 (Punto objetivo STOPAT)

GO
-- Ejecución del desastre por error humano
DELETE FROM Citas;
DELETE FROM Pacientes; -- ¡Desastre! Se eliminaron todos los pacientes y citas por falta de WHERE.
GO

-- Comprobación del desastre
SELECT * FROM Pacientes; -- Debería devolver 0 filas.
SELECT * FROM Citas; -- Debería devolver 0 filas.
GO


-- 1.6. PROCEDIMIENTO DE RECUPERACIÓN AVANZADA (PITR CON STOPAT)
-- El fallo se declara formalmente unos minutos después. 
-- Paso A: Realizar un respaldo del log de cola (Tail-Log Backup) sin truncar el log actual.
USE master;
GO
BACKUP LOG Hospital_LL 
TO DISK = 'C:\Backups\Trn\Hospital_LL_TailLog.trn' 
WITH NORECOVERY, NO_TRUNCATE, NAME = 'Tail-Log Backup Hospital_LL';
GO
-- Nota: La base de datos queda en estado RESTORING (no accesible) mientras se recupera.

-- Paso B: Secuencia ordenada de comandos RESTORE combinando el Full Backup y Logs
-- Restaurar el Full Backup con NORECOVERY para permitir aplicar la cadena de logs
RESTORE DATABASE Hospital_LL 
FROM DISK = 'C:\Backups\Full\Hospital_LL_Full.bak' 
WITH NORECOVERY, REPLACE;
GO

-- Restaurar el primer log limpio con NORECOVERY
RESTORE LOG Hospital_LL 
FROM DISK = 'C:\Backups\Trn\Hospital_LL_Log1.trn' 
WITH NORECOVERY;
GO

-- Restaurar el Tail-Log aplicando la cláusula WITH STOPAT para detenerse un minuto 
-- antes del borrado masivo
RESTORE LOG Hospital_LL 
FROM DISK = 'C:\Backups\Trn\Hospital_LL_TailLog.trn' 
WITH STOPAT = '2026-05-27T22:31:14', RECOVERY;
GO

-- Paso C: Verificación del estado consistente y exitoso de la BD
USE Hospital_LL;
GO
SELECT * FROM Pacientes; 
SELECT * FROM Citas; 
