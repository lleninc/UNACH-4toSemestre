
------------------------------------------------------------------------------------------------------
-----------
------------------------------------------------------------------------------------------------------

CREATE VIEW Vista_ProductosActivos1
AS
SELECT *
FROM Productos
WHERE stock > 0


select * from Vista_ProductosActivos1

CREATE VIEW dbo.Vista_Transacciones
AS
SELECT 
    t.transaccion_id,
    p.nombre AS nombre_producto,
    prov.nombre AS nombre_proveedor,
    t.fecha,
    t.cantidad,
    t.monto,
    t.tipo,
    t.proveedor_id,
    t.producto_id
FROM dbo.Transacciones t
INNER JOIN dbo.Productos p ON t.producto_id = p.producto_id
INNER JOIN dbo.Proveedores prov ON t.proveedor_id = prov.proveedor_id;

select * from dbo.Vista_Transacciones


------------------------------------------------------------------------------------------------------
----------------FUNCION 1 CalcularIVA -----------
------------------------------------------------------------------------------------------------------

CREATE FUNCTION dbo.CalcularIVA(@monto DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @iva DECIMAL(10,2);
    SET @iva = @monto * 0.12;
    RETURN @iva;
END;

SELECT dbo.CalcularIVA(135.00) AS IVA;


-----FUNCION 2 TransaccionesPorProveedor ----
CREATE FUNCTION dbo.TransaccionesPorProveedor(@proveedor_id INT)
RETURNS TABLE
AS
RETURN
(
    SELECT 
        t.transaccion_id,
        t.producto_id,
        p.nombre AS nombre_producto,
        t.proveedor_id,
        prov.nombre AS nombre_proveedor,
        t.fecha,
        t.cantidad,
        t.monto,
        t.tipo
    FROM dbo.Transacciones t
    INNER JOIN dbo.Productos p ON t.producto_id = p.producto_id
    INNER JOIN dbo.Proveedores prov ON t.proveedor_id = prov.proveedor_id
    WHERE t.proveedor_id = @proveedor_id
);

SELECT * FROM dbo.TransaccionesPorProveedor(2);



------------------------------------------------------------------------------------------------------
----------------------PROCEDIMIENTO INSERTA COMPRA ------------------
------------------------------------------------------------------------------------------------------

CREATE PROCEDURE dbo.InsertarCompra
    @producto_id INT,
    @proveedor_id INT,
    @cantidad INT,
    @monto DECIMAL(10,2)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Validar existencia del producto
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id)
        BEGIN
            THROW 50001, 'El producto no existe.', 1;
        END;
        
        -- Validar existencia del proveedor
        IF NOT EXISTS (SELECT 1 FROM dbo.Proveedores WHERE proveedor_id = @proveedor_id)
        BEGIN
            THROW 50002, 'El proveedor no existe.', 1;
        END;
        
        -- Actualizar stock
        UPDATE dbo.Productos
        SET stock = stock + @cantidad
        WHERE producto_id = @producto_id;
        
        -- Insertar transacción
        INSERT INTO dbo.Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (@producto_id, @proveedor_id, GETDATE(), @cantidad, 'COMPRA', @monto);
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;

EXEC dbo.InsertarCompra @producto_id = 3, @proveedor_id = 2, @cantidad = 8, @monto = 200.00;


------------------------------------------------------------------------------------------------------
          -------------------PROCEDIMIENTO INSERTA VENTA ---------------------------------------
------------------------------------------------------------------------------------------------------
CREATE PROCEDURE dbo.InsertarVenta
    @producto_id INT,
    @proveedor_id INT,
    @cantidad INT,
    @monto DECIMAL(10,2)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Validar existencia del producto
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id)
        BEGIN
            THROW 50001, 'El producto no existe.', 1;
        END;
        
        -- Validar existencia del proveedor
        IF NOT EXISTS (SELECT 1 FROM dbo.Proveedores WHERE proveedor_id = @proveedor_id)
        BEGIN
            THROW 50002, 'El proveedor no existe.', 1;
        END;
        
        -- Validar stock suficiente
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id AND stock >= @cantidad)
        BEGIN
            THROW 50003, 'Stock insuficiente para realizar la venta.', 1;
        END;
        
        -- Reducir stock
        UPDATE dbo.Productos
        SET stock = stock - @cantidad
        WHERE producto_id = @producto_id;
        
        -- Insertar transacción
        INSERT INTO dbo.Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (@producto_id, @proveedor_id, GETDATE(), @cantidad, 'VENTA', @monto);
        
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;

EXEC dbo.InsertarVenta @producto_id = 6, @proveedor_id = 2, @cantidad = 10, @monto = 15000.00;


SELECT * FROM Transacciones


----------------------------------------------------------------------------------
-------------------------TIGGER AUDITA INSERT------------------------------
----------------------------------------------------------------------------------

CREATE TRIGGER dbo.trg_AuditoriaTransacciones
ON dbo.Transacciones
AFTER INSERT
AS
BEGIN
    INSERT INTO dbo.Auditoria_Transacciones (transaccion_id, tipo, fecha)
    SELECT 
        inserted.transaccion_id,
        inserted.tipo,
        inserted.fecha
    FROM inserted;
END;

SELECT * FROM Auditoria_Transacciones
----------------------------------------------------------------------------------
-------------------------TIGGER VALORES NEGATIVOS EN STOCK------------------------
----------------------------------------------------------------------------------

select * from Productos

CREATE TRIGGER dbo.trg_ValidarStockNegativo
ON dbo.Transacciones
AFTER INSERT
AS
BEGIN
    DECLARE @producto_id INT, @tipo VARCHAR(50);
    
    SELECT @producto_id = producto_id, @tipo = tipo
    FROM inserted;
    
    -- Validar que el stock no sea negativo en ventas
    IF @tipo = 'VENTA'
    BEGIN
        IF EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id AND stock < 0)
        BEGIN
            ROLLBACK TRANSACTION;
            THROW 50004, 'Error: El stock del producto no puede ser negativo.', 1;
        END;
    END;
END;

EXEC dbo.InsertarVenta @producto_id = 6, @proveedor_id = 2, @cantidad = 10, @monto = 15000.00;
