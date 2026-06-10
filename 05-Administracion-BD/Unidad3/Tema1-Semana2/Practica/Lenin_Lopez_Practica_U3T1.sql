CREATE DATABASE BD_Quito;
GO
USE BD_Quito;
CREATE TABLE Cuentas_Quito (
 id_cuenta INT PRIMARY KEY,
 cliente VARCHAR(50),
 saldo DECIMAL(12,2) NOT NULL CHECK (saldo >= 0)
);
INSERT INTO Cuentas_Quito VALUES (1001, 'Ana Martínez (Sierra)', 1500.00);
GO
CREATE DATABASE BD_Guayaquil;
GO
USE BD_Guayaquil;
CREATE TABLE Cuentas_Guayaquil (
 id_cuenta INT PRIMARY KEY,
 cliente VARCHAR(50),
 saldo DECIMAL(12,2) NOT NULL CHECK (saldo >= 0)
);
INSERT INTO Cuentas_Guayaquil VALUES (2002, 'Carlos Ruiz (Costa)', 500.00);
GO


USE BD_Quito;
GO
CREATE VIEW V_CUENTAS_GLOBAL AS
SELECT id_cuenta, cliente, saldo, 'Quito' AS Ubicacion_Fisica FROM
BD_Quito.dbo.Cuentas_Quito
UNION ALL
SELECT id_cuenta, cliente, saldo, 'Guayaquil' AS Ubicacion_Fisica FROM
BD_Guayaquil.dbo.Cuentas_Guayaquil;
GO
-- El usuario consulta todo el banco sin saber que está dividido en dos ciudades
SELECT * FROM V_CUENTAS_GLOBAL;



USE BD_Quito;
GO
BEGIN TRY
 -- Iniciamos la transacción distribuida (Invoca internamente a 2PC)
 BEGIN DISTRIBUTED TRANSACTION;
 -- 1. Nodo Quito: Debitar 1000 USD
 UPDATE BD_Quito.dbo.Cuentas_Quito
 SET saldo = saldo - 1000
 WHERE id_cuenta = 1001;
 -- 2. Nodo Guayaquil: Acreditar 1000 USD
 UPDATE BD_Guayaquil.dbo.Cuentas_Guayaquil
 SET saldo = saldo + 1000
 WHERE id_cuenta = 2002;
 -- Si ambas operaciones fueron exitosas, el coordinador ejecuta la Fase2: COMMIT
 COMMIT TRANSACTION;
 PRINT 'Transacción Distribuida Exitosa con 2PC.';
END TRY
BEGIN CATCH
 -- Si algún nodo falla (no acepta o error de red), se ejecuta ROLLBACK global
 ROLLBACK TRANSACTION;
 PRINT 'Error detectado. Se ejecutó ROLLBACK global para garantizar
consistencia.';
END CATCH


-- Verificación de saldos
SELECT * FROM BD_Quito.dbo.Cuentas_Quito;
SELECT * FROM BD_Guayaquil.dbo.Cuentas_Guayaquil;


USE BD_Quito;
GO
BEGIN TRY
 BEGIN DISTRIBUTED TRANSACTION;
 -- Intentamos debitar 2000 USD
 UPDATE BD_Quito.dbo.Cuentas_Quito
 SET saldo = saldo - 2000
 WHERE id_cuenta = 1001;
-- Esta instrucción en Guayaquil teóricamente es válida, pero no debe consolidarse
 UPDATE BD_Guayaquil.dbo.Cuentas_Guayaquil
 SET saldo = saldo + 2000
 WHERE id_cuenta = 2002;
 COMMIT TRANSACTION;
END TRY
BEGIN CATCH
 -- El CATCH atrapará la violación del CHECK constraint de Quito
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;
 PRINT 'Transacción abortada con éxito. Razón del fallo: ' +
ERROR_MESSAGE();
END CATCH;
-- Comprobación, los saldos deben seguir intactos (atomicidad)
SELECT * FROM BD_Quito.dbo.Cuentas_Quito;
SELECT * FROM BD_Guayaquil.dbo.Cuentas_Guayaquil;


----------------------------------------
USE BD_Quito;
GO
CREATE PROCEDURE sp_ProcesarTransferenciaInterbancaria
 @id_origen INT,
 @id_destino INT,
 @monto DECIMAL(12,2)
AS
BEGIN
 SET NOCOUNT ON;
 BEGIN TRY
 BEGIN DISTRIBUTED TRANSACTION;
 -- 1. Cargo a la cuenta de la Sierra
 UPDATE BD_Quito.dbo.Cuentas_Quito
 SET saldo = saldo - @monto
 WHERE id_cuenta = @id_origen;
 -- 2. Abono a la cuenta de la Costa
 UPDATE BD_Guayaquil.dbo.Cuentas_Guayaquil
 SET saldo = saldo + @monto
 WHERE id_cuenta = @id_destino;
 COMMIT TRANSACTION;
 PRINT '¡Transferencia procesada con éxito global!';
 END TRY
 BEGIN CATCH
 IF @@TRANCOUNT > 0 ROLLBACK TRANSACTION;

 DECLARE @ErrorMsg NVARCHAR(4000) = ERROR_MESSAGE();
 RAISERROR ('Error en la transferencia distribuida. Red de servidores segura. Detalle: %s', 16, 1, @ErrorMsg);
 END CATCH
END;
GO

------------------

EXEC sp_ProcesarTransferenciaInterbancaria 1001, 2002, 100.00;

-------------------
SELECT * FROM BD_Quito.dbo.Cuentas_Quito;
SELECT * FROM BD_Guayaquil.dbo.Cuentas_Guayaquil;

-----------------------------------------------------------
-------------------REPLICACION--TOTAL-------------------------
------------------------------------------------------------

-- Creamos la tabla original en el Nodo Central (Quito)
USE BD_Quito;
GO
CREATE TABLE Sucursales_Quito_Origen (
 id_sucursal INT PRIMARY KEY,
 nombre_sucursal VARCHAR(50),
 ciudad VARCHAR(30)
);
-- Insertamos los datos globales en el origen
INSERT INTO Sucursales_Quito_Origen VALUES
(1, 'Agencia Terminal Terrestre', 'Riobamba'),
(2, 'Agencia Mall del Río', 'Cuenca'),
(3, 'Agencia Centro Histórico', 'Quito');
GO


--Creamos la La Réplica Total en Guayaquil
USE BD_Guayaquil;
GO

CREATE TABLE Sucursales_Guayaquil_Replica (
 id_sucursal INT PRIMARY KEY,
 nombre_sucursal VARCHAR(50),
 ciudad VARCHAR(30)
);
GO
--TRÁFICO DE REPLICACIÓN
INSERT INTO BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica
SELECT * FROM BD_Quito.dbo.Sucursales_Quito_Origen;
GO
-- Se veráns todas las sucursales del país localmente
SELECT * FROM BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica;
SELECT * FROM BD_Quito.dbo.Sucursales_Quito_Origen;

--8---------------------------------------------------------------------------------------
--Preparamos el terreno en Guayaquil para recibir la réplica parcial de Quito
USE BD_Guayaquil;
GO
CREATE TABLE Clients_VIP_Quito_En_Gye (
 id_cuenta INT PRIMARY KEY,
 cliente VARCHAR(50),
 saldo DECIMAL(12,2)
);
GO
--SIMULACIÓN DEL FILTRO DE REPLICACIÓN PARCIAL (Criterio: Saldo >= 1000)
-- El motor analiza BD_Quito, pero SOLO copia las cuentas VIP hacia Guayaquil
INSERT INTO BD_Guayaquil.dbo.Clients_VIP_Quito_En_Gye (id_cuenta, cliente, saldo)
SELECT id_cuenta, cliente, saldo
FROM BD_Quito.dbo.Cuentas_Quito
WHERE saldo >= 1000.00;
GO
-- 3. Verificación del Filtro Parcial
SELECT * FROM BD_Guayaquil.dbo.Clients_VIP_Quito_En_Gye;
--Insertar un nuevo registro en la sierra para que se pase con la replicación
USE BD_Quito;
GO
INSERT INTO Cuentas_Quito VALUES (1002, 'Luis Narváez (Sierra)', 1200.00);
GO
SELECT * FROM Cuentas_Quito;
--Limpiamos la tabla espejo que está en Guayaquil
TRUNCATE TABLE BD_Guayaquil.dbo.Clients_VIP_Quito_En_Gye;
GO
--Verificamos nuevamente
SELECT * FROM BD_Guayaquil.dbo.Clients_VIP_Quito_En_Gye;

------------------------------------------
-----------------ACTIVIDAD 1--------------
------------------------------------------
-- 1. Crea una tabla en BD_Quito llamada Clients_VIP_Gye_En_Quito
CREATE TABLE Clients_VIP_Gye_En_Quito (
 id_cuenta INT PRIMARY KEY,
 cliente VARCHAR(50),
 saldo DECIMAL(12,2) NOT NULL CHECK (saldo >= 0));

--2. Realiza un INSERT en BD_Guayaquil.dbo.Cuentas_Guayaquil 
--   de un nuevo cliente de la Costa (María Belén, id: 2003) con un saldo inicial de 1,400.00USD.
INSERT INTO BD_Guayaquil.dbo.Cuentas_Guayaquil VALUES (2003, 'María Belén (Costa)', 1400.00);

-- 3. Escribe el script de replicación parcial que extraiga los datos VIP desde
--    Guayaquil y los inserte en la nueva tabla de Quito.
INSERT INTO BD_Quito.dbo.Clients_VIP_Gye_En_Quito (id_cuenta, cliente, saldo)
SELECT id_cuenta, cliente, saldo
FROM BD_Guayaquil.dbo.Cuentas_Guayaquil
WHERE saldo >= 1000.00;

-- 4. Ejecuta un SELECT en Quito para demostrar que el nuevo cliente VIP de
--    la Costa ya es visible en la Sierra.

SELECT * FROM BD_Quito.dbo.Clients_VIP_Gye_En_Quito;

------------------------------------------------------
--------------------ACTIVIDAD 2-----------------------
-------------------------------------------------------

/*Si un saldo cambia, la réplica se queda desactualizada. El
reto es obligar al motor a mantener la consistencia en tiempo real.
Automatizar la Replicación Total de Sucursales. Cada vez que el Administrador
inserte una nueva sucursal en el origen (BD_Quito), esta debe replicarse en el
mismo milisegundo en el nodo remoto (BD_Guayaquil) de forma automática sin
que el usuario digite código extra.
Tareas a realizar:*/

---DATOS ANTES DE TRIGGER
SELECT * FROM BD_Quito.dbo.Sucursales_Quito_Origen;
SELECT * FROM BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica;

-- 1	Agencia Terminal Terrestre	Riobamba
-- 2	Agencia Mall del Río	Cuenca
-- 3	Agencia Centro Histórico	Quito

-- 1. Crea un disparador (AFTER INSERT TRIGGER) en la tabla Sucursales_Quito_Origen.
-- 2. El trigger debe incluir internamente un bloque distributivo que inserte el
--    nuevo registro en BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica.
use BD_Quito;
GO
CREATE TRIGGER trg_ReplicaSucursales
ON Sucursales_Quito_Origen
AFTER INSERT
AS
BEGIN
 -- Insertamos los nuevos registros en la réplica de Guayaquil
 INSERT INTO BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica (id_sucursal, nombre_sucursal, ciudad)
 SELECT id_sucursal, nombre_sucursal, ciudad
 FROM inserted; -- 'inserted' contiene los nuevos registros que se acaban de insertar en Sucursales_Quito_Origen
END;
GO

--3. Inserta la "Agencia Norte" en Quito y demuestra mediante un SELECT en
--   Guayaquil que apareció mágicamente.
INSERT INTO Sucursales_Quito_Origen VALUES (4, 'Agencia Norte', 'Quito');
SELECT * FROM BD_Guayaquil.dbo.Sucursales_Guayaquil_Replica;
SELECT * FROM BD_Quito.dbo.Sucursales_Quito_Origen;

-- datos después del trigger
-- 1	Agencia Terminal Terrestre	Riobamba
-- 2	Agencia Mall del Río	Cuenca
-- 3	Agencia Centro Histórico	Quito
-- 4	Agencia Norte	Quito









