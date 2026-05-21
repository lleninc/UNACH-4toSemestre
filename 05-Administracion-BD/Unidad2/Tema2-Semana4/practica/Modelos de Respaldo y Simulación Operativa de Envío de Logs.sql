/*
PRACTICA 2: Modelos de Respaldo y Simulacion Operativa de Envio de Logs
Fecha: 2026-05-19

Contexto:
MediCloud requiere que un servidor secundario en Quito pueda operar de inmediato
si el primario falla. Se emula manualmente el ciclo de Log Shipping.
*/

/*
Actividad 1:
Generar un respaldo de transacciones hacia /var/opt/mssql/backup/MediCloud_Trans1.trn

Requisitos previos:
- La base MediCloud debe estar en FULL recovery.
- Deben existir respaldos FULL/DIF previos para iniciar Log Shipping.
*/
USE master;
GO

BACKUP LOG MediCloud
TO DISK = '/var/opt/mssql/backup/MediCloud_Trans1.trn'
WITH INIT, COMPRESSION, STATS = 5;
GO

/*
Actividad 2:
Aplicar el log en el servidor secundario usando WITH STANDBY
*/
RESTORE LOG MediCloud_Secundaria
FROM DISK = '/var/opt/mssql/backup/MediCloud_Trans1.trn'
WITH STANDBY = '/var/opt/mssql/backup/MediCloud_Secundaria_undo.ldf',
	 STATS = 5;
GO

/*
Actividad 3:
Prueba de accesibilidad en la base secundaria (modo STANDBY/READ ONLY)
*/
USE MediCloud_Secundaria;
GO

-- A) Consulta de lectura para auditoria
SELECT TOP (10)
    *
FROM dbo.Pacientes;
GO

-- B) Intento de insercion para verificar bloqueo de modificaciones
BEGIN TRY
	INSERT INTO dbo.Pacientes
    (PacienteId, Nombres, Apellidos, FechaNacimiento)
VALUES
    (999999, 'Paciente', 'Simulado', '1990-01-01');
END TRY
BEGIN CATCH
	SELECT
    ERROR_NUMBER() AS ErrorNumber,
    ERROR_MESSAGE() AS ErrorMessage;

	-- ERROR esperado (SQL Server):
	-- "The operation cannot be performed on database 'MediCloud_Secundaria'
	-- because it is involved in a log shipping restore sequence or is read-only."
	-- Si el mensaje difiere, reemplace este comentario con el texto exacto.
END CATCH;
GO

/*
Definicion de RPO y RTO del escenario

RPO (Punto de Recuperacion):
- Ultimo log exitoso: 13:00
- Falla total: 13:14:59
- Informacion potencialmente perdida: 14 min 59 s (≈ 15 min)

RTO (Tiempo de Recuperacion):
- Tiempo estimado para ejecutar la sentencia y habilitar la base con RECOVERY
- Estimacion: 1 min (ajustar segun la practica real)

Explicacion:
Log Shipping mantiene una copia casi en tiempo real mediante respaldos de log
frecuentes. El RPO es predecible y controlado por la frecuencia del BACKUP LOG
y el RTO es bajo porque la activacion del secundario es una accion operativa
rapida (RESTORE ... WITH RECOVERY) ante un desastre del primario.
*/

/*
Activacion del secundario en modo operativo (para el RTO):
RESTORE DATABASE MediCloud_Secundaria WITH RECOVERY;
*/
