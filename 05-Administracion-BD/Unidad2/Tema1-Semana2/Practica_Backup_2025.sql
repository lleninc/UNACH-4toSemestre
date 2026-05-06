CREATE DATABASE SistemaVentas;
GO
USE SistemaVentas;
GO
-- Crear una tabla de ejemplo
CREATE TABLE Productos (
Id INT PRIMARY KEY IDENTITY(1,1),
Nombre VARCHAR(50),
Precio DECIMAL(10,2),
FechaRegistro DATETIME DEFAULT GETDATE()
);
-- Insertar datos iniciales
INSERT INTO Productos (Nombre, Precio) VALUES ('Laptop', 1200), ('Mouse',
25);
GO
-----------------------------------------------------------------
--PRIMERA PARTE DE LA PR�CTICA
--Fase 1: El Backup Completo
--Imagina que es lunes a las 8:00 AM. Hacemos el primer respaldo total.
--SCRIPT
-----------------------------------------------------------------
BACKUP DATABASE SistemaVentas
TO DISK = 'C:\Backups\SistemaVentas_Full_2025.bak'
WITH FORMAT, MEDIANAME = 'FullVentas', NAME = 'Full Backup de SistemaVentas';
GO
--Fase 2: Cambios y Backup Diferencial
--Imagina que es mediod�a del lunes. Se han realizado nuevas ventas (datos
--nuevos).
--SCRIPT: Se insertan dos nuevos datos
INSERT INTO Productos (Nombre, Precio) VALUES ('Teclado', 45), ('Monitor',
300);
GO
--SCRIPT: Realizar Backup Diferencial (Solo guarda los 2 productos nuevos)
BACKUP DATABASE SistemaVentas
TO DISK = 'C:\Backups\SistemaVentas_Diff_2025.bak'
WITH DIFFERENTIAL, NAME = 'Diferencial Ventas Ma�ana';
GO

--Fase 3: El Desastre
--Un error humano borra la base de datos a las 2:00 PM.
--SCRIPT: Borrado de la base completa.
USE master;
GO
DROP DATABASE SistemaVentas;
GO

---SCRIPT: Si diera error, forzamos al borrado:
USE master;
GO
ALTER DATABASE SistemaVentas
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE;
DROP DATABASE SistemaVentas;
GO

--Fase 4: Recuperaci�n (RTO en marcha)
--Para recuperar hasta el �ltimo punto antes del desastre, debemos seguir el
--orden l�gico.
--SCRIPT: Restaurar el Backup COMPLETO primero (con NORECOVERY para
--permitir m�s archivos)
RESTORE DATABASE SistemaVentas
FROM DISK = 'C:\Backups\SistemaVentas_Full_2025.bak'
WITH NORECOVERY;
GO
--SCRIPT: Restaurar el Backup DIFERENCIAL (Trae los datos del mediod�a)
RESTORE DATABASE SistemaVentas
FROM DISK = 'C:\Backups\SistemaVentas_Diff_2025.bak'
WITH RECOVERY;
GO
--SCRIPT: Verificar que los datos est�n ah�
USE SistemaVentas;
SELECT * FROM Productos;


----------------------------------------
--SCRIPT: Asegurar que la BD permite copias incrementales (Logs)
ALTER DATABASE SistemaVentas SET RECOVERY FULL;
GO
--SCRIPT: Simulamos actividad a las 3:00 PM
INSERT INTO Productos (Nombre, Precio) VALUES ('Impresora', 150);
GO
--SCRIPT: Realizamos el Backup Incremental (Log)
BACKUP LOG SistemaVentas
TO DISK = 'C:\Backups\SistemaVentas_Log1_2025.trn'
WITH NAME = 'Incremental_3PM';
GO
--SCRIPT: Simulamos m�s actividad a las 4:00 PM
INSERT INTO Productos (Nombre, Precio) VALUES ('Parlantes', 80);
GO
--SCRIPT: Simular otro Backup Incremental
BACKUP LOG SistemaVentas
TO DISK = 'C:\Backups\SistemaVentas_Log2_2025.trn'
WITH NAME = 'Incremental_4PM';
GO
--Fase 6: Pruebas de Recuperaci�n
---Las Pruebas de Recuperaci�n no son solo restaurar, es verificar que el plan
---cumple con el RPO.
---Vamos a recuperar la base de datos exactamente como estaba a las 3:00
---PM (solo con la Impresora, sin los Parlantes).
--SCRIPT: Borrar la base de datos
USE master;
GO
DROP DATABASE SistemaVentas;
--SCRIPT: Si diera error, forzamos al borrado:
USE master;
GO
ALTER DATABASE SistemaVentas
SET SINGLE_USER
WITH ROLLBACK IMMEDIATE;
DROP DATABASE SistemaVentas;
GO
--SCRIPT: Restaurar el Full (obligatorio)
RESTORE DATABASE SistemaVentas FROM DISK =
'C:\Backups\SistemaVentas_Full_2025.bak' WITH NORECOVERY;
--SCRIPT: Restaurar el Diferencial (trae informaci�n hasta mediod�a)
RESTORE DATABASE SistemaVentas FROM DISK =
'C:\Backups\SistemaVentas_Diff_2025.bak' WITH NORECOVERY;
--SCRIPT: Restaurar solo el primer Incremental (Log de las 3:00 PM)
RESTORE LOG SistemaVentas FROM DISK =
'C:\Backups\SistemaVentas_Log1_2025.trn' WITH RECOVERY;
--SCRIPT: Para verificar la prueba:
USE SistemaVentas;
SELECT * FROM Productos;
--Deber�a aparecer la Impresora, pero NO los Parlantes, observemos:
---TERCERA PARTE DE LA PR�CTICA
--Monitoreo y automatizaci�n: Los SGBD modernos y herramientas
--externas permiten programar respaldos autom�ticos y generar alertas
--en caso de fallos.
--Preparar el escenario: Iniciar el SQL Server Agent
--Para que los Jobs funcionen, el servicio del SQL Server Agent debe estar en
--ejecuci�n.
--� En el Object Explorer, busca el icono del agente al final de la lista.
--� Si tiene un c�rculo rojo, haz clic derecho y selecciona Start.

SELECT SERVERPROPERTY('Edition') AS Edition;
select @@VERSION