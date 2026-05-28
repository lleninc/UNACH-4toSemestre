-- Actividad Autonoma 4
-- Unidad 2: Recuperacion avanzada de bases de datos
-- Tema 2: Recuperacion en gestores de BD
-- Caso propuesto: tienda de ropa

/*
    Este script esta pensado para SQL Server.
    Cubre:
    - Creacion de una base de datos con 5 tablas
    - Configuracion del modelo de recuperacion FULL
    - Ejemplos de UNDO y REDO con transacciones
    - Ejemplos de backup y restauracion point-in-time
    - Referencia teorica para log shipping y PostgreSQL PITR
*/

IF DB_ID('TiendaRopa_DB') IS NOT NULL
BEGIN
    ALTER DATABASE TiendaRopa_DB SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE TiendaRopa_DB;
END
GO

CREATE DATABASE TiendaRopa_DB;
GO

ALTER DATABASE TiendaRopa_DB SET RECOVERY FULL;
GO

USE TiendaRopa_DB;
GO

CREATE TABLE Categorias (
    IdCategoria INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE Clientes (
    IdCliente INT IDENTITY(1,1) PRIMARY KEY,
    Nombre NVARCHAR(120) NOT NULL,
    Email NVARCHAR(120) NOT NULL UNIQUE,
    Telefono NVARCHAR(20) NULL,
    FechaRegistro DATETIME2 NOT NULL DEFAULT SYSDATETIME()
);

CREATE TABLE Productos (
    IdProducto INT IDENTITY(1,1) PRIMARY KEY,
    IdCategoria INT NOT NULL,
    Nombre NVARCHAR(120) NOT NULL,
    Talla NVARCHAR(10) NOT NULL,
    Color NVARCHAR(30) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL CHECK (Precio >= 0),
    Stock INT NOT NULL CHECK (Stock >= 0),
    CONSTRAINT FK_Productos_Categorias
        FOREIGN KEY (IdCategoria) REFERENCES Categorias(IdCategoria)
);

CREATE TABLE Ventas (
    IdVenta INT IDENTITY(1,1) PRIMARY KEY,
    IdCliente INT NOT NULL,
    FechaVenta DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
    Total DECIMAL(10,2) NOT NULL CHECK (Total >= 0),
    Estado NVARCHAR(20) NOT NULL DEFAULT 'Registrada',
    CONSTRAINT FK_Ventas_Clientes
        FOREIGN KEY (IdCliente) REFERENCES Clientes(IdCliente)
);

CREATE TABLE DetalleVenta (
    IdDetalle INT IDENTITY(1,1) PRIMARY KEY,
    IdVenta INT NOT NULL,
    IdProducto INT NOT NULL,
    Cantidad INT NOT NULL CHECK (Cantidad > 0),
    PrecioUnitario DECIMAL(10,2) NOT NULL CHECK (PrecioUnitario >= 0),
    Subtotal AS (Cantidad * PrecioUnitario) PERSISTED,
    CONSTRAINT FK_DetalleVenta_Ventas
        FOREIGN KEY (IdVenta) REFERENCES Ventas(IdVenta),
    CONSTRAINT FK_DetalleVenta_Productos
        FOREIGN KEY (IdProducto) REFERENCES Productos(IdProducto)
);
GO

INSERT INTO Categorias (Nombre)
VALUES
    ('Camisas'),
    ('Pantalones'),
    ('Chaquetas'),
    ('Vestidos');

INSERT INTO Clientes (Nombre, Email, Telefono)
VALUES
    ('Ana Lopez', 'ana.lopez@example.com', '0991111111'),
    ('Carlos Vera', 'carlos.vera@example.com', '0982222222'),
    ('Maria Torres', 'maria.torres@example.com', '0973333333');

INSERT INTO Productos (IdCategoria, Nombre, Talla, Color, Precio, Stock)
VALUES
    (1, 'Camisa formal', 'M', 'Blanco', 28.50, 25),
    (1, 'Camisa casual', 'L', 'Azul', 24.90, 18),
    (2, 'Jean clasico', '32', 'Denim', 35.75, 20),
    (3, 'Chaqueta impermeable', 'M', 'Negro', 54.99, 12),
    (4, 'Vestido verano', 'S', 'Rojo', 42.00, 15);

INSERT INTO Ventas (IdCliente, Total, Estado)
VALUES
    (1, 87.00, 'Registrada'),
    (2, 35.75, 'Registrada');

INSERT INTO DetalleVenta (IdVenta, IdProducto, Cantidad, PrecioUnitario)
VALUES
    (1, 1, 2, 28.50),
    (1, 3, 1, 30.00),
    (2, 3, 1, 35.75);
GO

-- Verificacion inicial
SELECT c.Nombre AS Categoria, p.Nombre AS Producto, p.Stock, p.Precio
FROM Productos p
INNER JOIN Categorias c ON c.IdCategoria = p.IdCategoria;
GO

/*
    UNDO: se ejecutan varias operaciones dentro de una transaccion y luego se revierte.
    Esto demuestra que SQL Server deshace los cambios antes del COMMIT.
*/
BEGIN TRAN UndoDemo;

INSERT INTO Clientes (Nombre, Email, Telefono)
VALUES ('Lucia Mena', 'lucia.mena@example.com', '0964444444');

UPDATE Productos
SET Stock = Stock - 2
WHERE Nombre = 'Camisa formal';

DELETE FROM Productos
WHERE Nombre = 'Vestido verano';

-- El estado puede revisarse antes del ROLLBACK
SELECT Nombre, Stock
FROM Productos
WHERE Nombre IN ('Camisa formal', 'Vestido verano');

ROLLBACK TRAN UndoDemo;
GO

-- Verificacion despues del ROLLBACK
SELECT Nombre, Stock
FROM Productos
WHERE Nombre IN ('Camisa formal', 'Vestido verano');
GO

/*
    REDO: los cambios se confirman con COMMIT y quedan protegidos por el log.
    Luego se respalda la base y el log para permitir restauracion hasta un punto exacto.
*/
BEGIN TRAN RedoDemo;

UPDATE Productos
SET Stock = Stock - 1
WHERE Nombre = 'Jean clasico';

UPDATE Ventas
SET Total = 64.75
WHERE IdVenta = 2;

COMMIT TRAN RedoDemo;
GO

-- Configuracion recomendada para trabajar con restauracion por log
BACKUP DATABASE TiendaRopa_DB
TO DISK = 'C:\Backups\TiendaRopa_DB_Full.bak'
WITH INIT, COMPRESSION, NAME = 'TiendaRopa_DB Full Backup';
GO

BACKUP LOG TiendaRopa_DB
TO DISK = 'C:\Backups\TiendaRopa_DB_Log1.trn'
WITH INIT, COMPRESSION, NAME = 'TiendaRopa_DB Log Backup 1';
GO

-- Ejemplo de recuperacion point-in-time en SQL Server
-- Ajustar nombres logicos y rutas fisicas segun el equipo local.
--
-- RESTORE DATABASE TiendaRopa_DB_Recuperada
-- FROM DISK = 'C:\Backups\TiendaRopa_DB_Full.bak'
-- WITH NORECOVERY,
--      MOVE 'TiendaRopa_DB' TO 'C:\SQLData\TiendaRopa_DB_Recuperada.mdf',
--      MOVE 'TiendaRopa_DB_log' TO 'C:\SQLLog\TiendaRopa_DB_Recuperada.ldf';
--
-- RESTORE LOG TiendaRopa_DB_Recuperada
-- FROM DISK = 'C:\Backups\TiendaRopa_DB_Log1.trn'
-- WITH STOPAT = '2026-05-26T15:30:00', RECOVERY;

-- Escenario de log shipping en SQL Server
-- 1. BACKUP LOG en la base primaria.
-- 2. Copia automatica del .trn al servidor secundario.
-- 3. RESTORE LOG en el secundario con NORECOVERY o STANDBY.
-- 4. Monitoreo de latencia y fallos de copia/restauracion.

-- Referencia teorica de PITR en PostgreSQL
-- postgresql.conf:
--   wal_level = replica
--   archive_mode = on
--   archive_command = 'copy "%p" "C:\\pg_archive\\%f"'
-- recovery.conf / parametros actuales:
--   restore_command = 'copy "C:\\pg_archive\\%f" "%p"'
--   recovery_target_time = '2026-05-26 15:30:00'
--   recovery_target_action = 'promote'

-- Comprobacion final de integridad de datos
SELECT *
FROM Clientes;

SELECT *
FROM Productos;

SELECT *
FROM Ventas;

SELECT *
FROM DetalleVenta;