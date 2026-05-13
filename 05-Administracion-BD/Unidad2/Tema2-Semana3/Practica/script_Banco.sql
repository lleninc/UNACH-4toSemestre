-- CREA LA BDD
CREATE DATABASE Banco;
GO
ALTER DATABASE Banco SET RECOVERY FULL;
GO
-- CREA LA TABLA CUENTA EN BANCO
USE Banco;
CREATE TABLE Cuentas (ID INT, Saldo DECIMAL(10,2));
--INSERTA DATOS EN LA TABLA CUENTA
INSERT INTO Cuentas VALUES (1, 5000.00);

select * from Cuentas

-- RESPALDO FULL
BACKUP DATABASE Banco
TO DISK = 'C:\Respaldos\Banco_Full.bak' WITH INIT;

-- RESTORE BDD ESPEJO
RESTORE DATABASE Banco2
FROM DISK = 'C:\Respaldos\Banco_Full.bak'
WITH MOVE 'Banco' TO 'C:\Respaldos\Secundario_Data.mdf',
 MOVE 'Banco_log' TO 'C:\Respaldos\Secundario_Log.ldf',
 STANDBY = 'C:\Respaldos\Undo_Log.bak'; 

 -------------------------------------------

--SCRIPT para insertar un cambio en la base principal
INSERT INTO Banco.dbo.Cuentas VALUES (2, 300.00);



--SCRIPT para el envío del log, hacemos el backup en la principal y lo aplicamos en la secundaria
BACKUP LOG Banco TO DISK = 'C:\Respaldos\Transito.trn' WITH INIT;
--SCRIPT para aplicar en la base de datos secundaria Banco2
RESTORE LOG Banco2 FROM DISK = 'C:\Respaldos\Transito.trn'
WITH STANDBY = 'C:\Respaldos\Undo_Log.bak';
--SCRIPT para verificar que los datos ya están en la base Banco2
SELECT * FROM Banco2.dbo.Cuentas;

---------------------------------------------------

--SCRIPT para antes de un cambio masivo, tomar una "foto" de la base de datos.
CREATE DATABASE Banco_Snap ON
( NAME = Banco, FILENAME = 'C:\Respaldos\Banco_Snap.ss' )
AS SNAPSHOT OF Banco;
--SCRIPT para simular un error en la base de datos principal
UPDATE Banco.dbo.Cuentas SET Saldo = 0;

use Banco
select * from Cuentas

--SCRIPT para revertir el cambio con snapshot
USE master;
RESTORE DATABASE Banco FROM DATABASE_SNAPSHOT = 'Banco_Snap';

-----------------SI DA ERROR ---------
ALTER DATABASE Banco
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE;
GO

-------------------------------------------------------------------------
--Paso 5: Recuperación de un error humano (PITR)
--Recuperar un registro borrado accidentalmente a una hora específica.
--SCRIPT para devolver la base de datos a su modo normal (multiusuario)
ALTER DATABASE Banco
SET MULTI_USER;
GO
--SCRIPT para eliminar el snapshot
DROP DATABASE Banco_Snap;
--SCRIPT para simula que ocurre un error (ejemplo, 10:30 AM)
Use Banco
GO
DELETE FROM Cuentas WHERE ID = 1;
--SCRIPT para restaurar el backup completo y luego el log hasta las 10:29 AM o en otras palabras un minuto antes
USE master;
RESTORE DATABASE Banco FROM DISK = 'C:\Respaldos\Banco_Full.bak' WITH
NORECOVERY, REPLACE;

--------------STOPAT---------------------------------------
RESTORE LOG Banco FROM DISK = 'C:\Respaldos\Transito.trn'
WITH STOPAT = '2026-05-12T19:32:00', RECOVERY;
-----------------------------------------------------------

USE master;
GO
RESTORE DATABASE Banco WITH RECOVERY;
GO

------------------------------------------------------------------------
-- Actividades:

BACKUP DATABASE Banco
TO DISK = 'C:\Respaldos\Banco_Full.bak' WITH INIT;

-- 1. Insertar 3 registros nuevos en la tabla Cuentas.
INSERT INTO Banco.dbo.Cuentas VALUES (2, 400.00);
INSERT INTO Banco.dbo.Cuentas VALUES (2, 500.00);
INSERT INTO Banco.dbo.Cuentas VALUES (2, 600.00);

--2. Realizar un BACKUP LOG. 19:32
BACKUP LOG Banco TO DISK = 'C:\Respaldos\Transito.trn' WITH INIT;
--3. Ejecutar un UPDATE masivo que ponga todos los saldos en 0 (simulando el error).
UPDATE Banco.dbo.Cuentas SET Saldo = 0;
--4. Recuperar la base de datos al estado exacto de un minuto antes del error masivo, pero asegurándose de que los 3 registros nuevos
--   insertados en el paso 1 no se pierdan.
USE master;
RESTORE DATABASE Banco FROM DISK = 'C:\Respaldos\Banco_Full.bak' WITH
NORECOVERY, REPLACE;


-- Entregable de la actividad: El valor del STOPAT exacto utilizado y la
RESTORE LOG Banco FROM DISK = 'C:\Respaldos\Transito.trn'
WITH STOPAT = '2026-05-12T19:32:00', RECOVERY;

-- verificación del SELECT con los datos recuperados.

----------------------------------------------------------------------------


