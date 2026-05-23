-- ======================================================================
-- PRÁCTICA 2: Modelos de Respaldo y Simulación Operativa de Envío de Logs
-- ======================================================================
-- ======================= INTEGRANTES===================================
-- ===
-- ===  --> Allison Atupaña
-- ===  --> Josselyn Obando
-- ===  --> Mario Camacho
-- ===  --> Gabriel Niama
-- ===  --> Lenin López
-- ======================================================================

--------CREACION DE LA BDD ---

CREATE DATABASE MediCloud_Prod;
GO
USE MediCloud_Prod;
GO
ALTER DATABASE MediCloud_Prod SET RECOVERY FULL;
GO
CREATE TABLE Pacientes (
    IdPaciente INT PRIMARY KEY IDENTITY(1,1),
    Nombre VARCHAR(100),
    Cedula VARCHAR(10) UNIQUE,
    HistorialClinico VARCHAR(MAX)
);
CREATE TABLE Citas (
    IdCita INT PRIMARY KEY IDENTITY(1,1),
    IdPaciente INT,
    FechaHora DATETIME,
    Quirofano INT,
    Estado VARCHAR(20) DEFAULT 'Programada'
);
-- Datos iniciales 
INSERT INTO Pacientes VALUES ('Carlos Cueva', '0603456789', 'Paciente hipertenso.');
INSERT INTO Pacientes VALUES ('Ana Altamirano', '0601234567', 'Control post-quirúrgico.');
GO



SELECT * FROM Citas
SELECT * FROM Pacientes

-- 1. Respaldar el log de transacciones de la base activa (MediCloud)
BACKUP DATABASE MediCloud_Prod
TO DISK = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Full.bak' WITH INIT;


BACKUP LOG MediCloud_Prod
TO DISK = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Trans1.trn'
WITH NOFORMAT, NOINIT,
NAME = 'Respaldo de Log - MediCloud',
SKIP, NOREWIND, NOUNLOAD, STATS = 10;
GO

-- 2. Aplicar el archivo de log en el servidor secundario en modo STANDBY
-- (Se permite usar la base solo en modo lectura para auditorías/reportes)

RESTORE DATABASE MediCloud_Secundaria
FROM DISK = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Full.bak'
WITH MOVE 'MediCloud_Prod' TO 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\Secundario_Data.mdf',
 MOVE 'MediCloud_Prod_log' TO 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\Secundario_Log.ldf',
 STANDBY = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\Undo_Log.bak'; 

RESTORE LOG MediCloud_Secundaria
FROM DISK = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Trans1.trn'
WITH STANDBY = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Standby.undo';
GO

-- 3. Pruebas de accesibilidad en la base de datos secundaria (Standby)
USE MediCloud_Secundaria;
GO

-- A) Consulta de lectura (SELECT)
-- Demuestra que un auditor puede consultar los datos en tiempo real de forma segura.
SELECT *
FROM Pacientes;
GO

-- B) Intento de inserción (INSERT)
-- Verificamos que el motor bloquee cualquier modificación para mantener la congruencia de logs.
BEGIN TRY
    INSERT INTO Pacientes 
    VALUES ('Lenin Lopez', '1254885125', 'Paciente Clinico.');

END TRY
BEGIN CATCH
    -- Documentación del error generado por SQL Server:
    -- Msg 3906, Level 16, State 1, Line X
    -- Failed to update database "MediCloud_Secundaria" because the database is read-only.
    PRINT 'Error esperado capturado: ' + ERROR_MESSAGE();
END CATCH
GO

--------------STOPAT---------------------------------------
--RESTORE LOG Banco FROM DISK = 'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema2-Semana4\practica\Backup\MediCloud_Trans1.trn'
--WITH STOPAT = '2026-05-19T19:49:00', RECOVERY;
-------------------------------------------------
 


/* ======================================================================
   RESPUESTAS A LAS PREGUNTAS: RPO Y RTO
   ======================================================================
   
   1. Cálculo de RPO (Recovery Point Objective):
   - Respaldos configurados: Cada 5 minutos a partir de las 19:50 (ej: 19:48, 19:50, 19:55).
   - Último respaldo exitoso: 19:48. 19:50
   - Siniestro (destrucción total): 20:02.
   - Tiempo de información perdida: 07 minutos y *** segundos.
   > RPO Máximo de nuestro escenario: 9 minutos (es la ventana de pérdida garantizada).

   2. Cálculo de RTO (Recovery Time Objective):
   - Corresponde al tiempo necesario para poner la base secundaria en modo operativo
     como primaria (pasar de STANDBY a RECOVERY).
   - Acción requerida: Ejecutar RESTORE DATABASE MediCloud_Secundaria WITH RECOVERY;
   - Estimo que como admin de BD me tomaría entre 1 y 3 minutos (tiempo en detectar 
     la alarma, ingresar al servidor de contingencia y ejecutar la sentencia).
   > RTO Estimado: ~2 minutos.

  
   3. Explicación del diseño Log Shipping para continuidad:
   El mecanismo de Log Shipping garantiza la continuidad al mantener un "espejo diferido"
   de la base de datos en otra ubicación geográfica (Quito). Cumple con un RPO estrictamente
   controlado porque sabemos exactamente cada cuánto tiempo se emiten los respaldos de LOG 
   (15 min). La ventaja de la cláusula STANDBY es dual: minimiza enormemente el RTO porque
   la BD ya está montada en el motor y, además, permite usar esos datos en contingencia
   para lectura (reportes, auditoría) sin afectar el servidor transaccional principal.
====================================================================== */
