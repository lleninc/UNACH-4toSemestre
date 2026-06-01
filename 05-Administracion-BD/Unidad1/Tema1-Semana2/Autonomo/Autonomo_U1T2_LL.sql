--CREACION DE TABLAS PROVEEDORES, PRODUCTOS, TRANSACCIONES

CREATE TABLE Proveedores (
    proveedor_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    contacto VARCHAR(100) NOT NULL,
    ciudad VARCHAR(80) NOT NULL
);
GO
CREATE TABLE Productos (
    producto_id INT IDENTITY(1,1) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(80) NOT NULL,
    precio DECIMAL(10,2) NOT NULL CHECK (precio > 0),
    stock INT NOT NULL CHECK (stock >= 0)
);
GO

CREATE TABLE Transacciones (
    transaccion_id INT IDENTITY(1,1) PRIMARY KEY,
    producto_id INT NOT NULL REFERENCES Productos(producto_id),
    proveedor_id INT NOT NULL REFERENCES Proveedores(proveedor_id),
    fecha DATETIME NOT NULL DEFAULT GETDATE(),
    cantidad INT NOT NULL CHECK (cantidad > 0),
    tipo VARCHAR(10) NOT NULL CHECK (tipo IN ('COMPRA','VENTA')),
    monto DECIMAL(12,2) NOT NULL CHECK (monto > 0)
);
GO

--Ingreso de datos a las tablas de las BDD para realizar el siguiente literal

INSERT INTO Proveedores (nombre, contacto, ciudad) VALUES
    ('Tecnomega','ventas@tecnomega.com.ec','Quito'),
    ('Megatecnology','ventas@megatecnology.com','Ibarra'),
    ('IDCComputer','info@idccomputer.com','Riobamba'),
    ('Fenix','ventas1@fenix.com','Tulcan'),
    ('Infinity','informacion@infinity.com','Ambato');

INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
    ('NOT. HP 255R G10 AMD Ryzen 5 7535U','Computación',750.00,30),
    ('IMP. SAT TERMICA 22T','Impresoras',150.00,50),
    ('SSD KINGSTON 240GB A400','Almacenamiento',70.00,80),
    ('TECLADO GENIUS WIRELESS NUMPAD','Periféricos',8.28,60),
    ('SWITCH TP-LINK TL-SL1218MP','Redes',220.00,15);
GO

select * from Proveedores
select * from Productos

-------------------TRANSACCIONES COMPRA Y VENTA----------------
---------------------------------------------------------------
------------------------ COMPRA PRODUCTO id 1------------------
---------------------------------------------------------------
PRINT '--- TRANSACCIÓN COMPRA: Laptop Core i7 ---';

BEGIN TRY
    BEGIN TRANSACTION;

        -- Paso 1: Registrar la compra en Transacciones
        INSERT INTO Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (1, 1, GETDATE(), 10, 'COMPRA', 7500.00);

        -- Paso 2: Actualizar stock del producto
        UPDATE Productos
        SET stock = stock + 10
        WHERE producto_id = 1;

       COMMIT TRANSACTION;
    PRINT 'COMPRA CONFIRMADA OK.';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'ERROR en COMPRA ROLLBACK.';
    PRINT 'Mensaje: ' + ERROR_MESSAGE();
END CATCH;
GO
--------------------------------VENTA ID 2----------------------------------------------
PRINT '--- TRANSACCIÓN VENTA: IMPRESORA ---';
BEGIN TRANSACTION;
BEGIN TRY
        -- Paso 1: Registrar la venta
        INSERT INTO Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (2, 2, GETDATE(), 60, 'VENTA', 300);

        -- Paso 2: Reducir stock
        UPDATE Productos
        SET stock = stock - 60
        WHERE producto_id = 2;

        IF (SELECT stock FROM Productos WHERE producto_id=2)<0
            THROW 50000, 'No hay stock suficiente',1;

        COMMIT 
        PRINT 'Venta realizada con exito....';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'ERROR en VENTA — se aplicó ROLLBACK.';
    PRINT 'Mensaje: ' + ERROR_MESSAGE();
END CATCH;
GO

select * from Productos WHERE producto_id=2;

---------------------3.	Control de bloqueos y niveles de aislamiento --------------------------
------------Simular dos transacciones que intentan modificar el mismo producto------------
-----------------------------------------------------------------------------------------------
PRINT '----------------------------'
PRINT 'Simulacion de transacciones';
PRINT '----------------------------'

BEGIN TRANSACTION;
UPDATE Productos SET stock=66 where producto_id=4;

--- ejecutar rollback despues de visualiar si se realiza o no el cambio (lectura falsa)

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM Productos WHERE producto_id=4; 

ROLLBACK TRANSACTION;
--validar stock de producto id 4
SELECT * FROM Productos WHERE producto_id=4;

------------------------------------------------------------------------
PRINT '----------------------------'
PRINT 'SIMULACION:  READ COMMITED';
PRINT '----------------------------'

---PRIMERA VENTANA-----
BEGIN TRANSACTION;
UPDATE Productos SET stock=30 where producto_id=5;

--ROLLBACK TRANSACTION;
------------------SEGUNDA VENTANA-------------------
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;   --
SELECT * FROM Productos WHERE producto_id=5;      --
----------------------------------------------------

----------------------------------------------------------------
PRINT '----------------------------'
PRINT 'SIMULACION: REPETEABLE READ';
PRINT '----------------------------'

INSERT INTO Productos 
VALUES('IMP. EPSON SURE COLOR T3170','Impresoras',1030,3)

---VENTANA 1 --

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;
SELECT * FROM Productos WHERE producto_id=6; 

---- VENTANA 2 --
UPDATE Productos SET stock=9 WHERE producto_id=6;

--- EN VENTANA 1 EJECUTAR EL COMMIT ---
COMMIT TRANSACTION;


----------------------------------------------------------------
PRINT '----------------------------'
PRINT 'SIMULACION: SERIALIZABLE';
PRINT '----------------------------'
---- VENTANA 1
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION
SELECT * FROM Productos WHERE stock<20

----- VENTANA 2 --> CONGELADA
INSERT INTO Productos 
VALUES('MONITOR ULTRA-SLIM YXK 15.6PULG','Monitores',75,10)
