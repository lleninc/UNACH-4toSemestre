-- ============================================================================
-- AUTONOMO 2: Implementación de Vistas, Funciones, Procedimientos y Triggers
-- Base de datos: InventarioProveedores_LL
-- ============================================================================

-- 1. CREAR TABLA DE AUDITORÍA
-- ============================================================================
IF NOT EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'Auditoria_Transacciones')
BEGIN
    CREATE TABLE dbo.Auditoria_Transacciones
    (
        auditoria_id INT PRIMARY KEY IDENTITY(1,1),
        transaccion_id INT NOT NULL,
        tipo VARCHAR(50) NOT NULL,
        fecha DATETIME NOT NULL,
        fecha_auditoria DATETIME DEFAULT GETDATE()
    );
    PRINT 'Tabla Auditoria_Transacciones creada correctamente.';
END
ELSE
    PRINT 'Tabla Auditoria_Transacciones ya existe.';
GO

-- 2. CREAR VISTAS
-- ============================================================================

-- Vista 1: Vista_ProductosActivos
-- Muestra productos con stock > 0 junto con el nombre del proveedor
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_NAME = 'Vista_ProductosActivos')
    DROP VIEW dbo.Vista_ProductosActivos;
GO

CREATE VIEW dbo.Vista_ProductosActivos
AS
SELECT 
    p.producto_id,
    p.nombre AS nombre_producto,
    p.categoria,
    p.precio,
    p.stock,
    prov.nombre AS nombre_proveedor,
    prov.proveedor_id
FROM dbo.Productos p
INNER JOIN dbo.Transacciones t ON p.producto_id = t.producto_id
INNER JOIN dbo.Proveedores prov ON t.proveedor_id = prov.proveedor_id
WHERE p.stock > 0
GROUP BY p.producto_id, p.nombre, p.categoria, p.precio, p.stock, prov.nombre, prov.proveedor_id;
GO

PRINT 'Vista Vista_ProductosActivos creada correctamente.';
GO

-- Vista 2: Vista_Transacciones
-- Muestra todas las transacciones realizadas (compra y venta)
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_NAME = 'Vista_Transacciones')
    DROP VIEW dbo.Vista_Transacciones;
GO

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
INNER JOIN dbo.Proveedores prov ON t.proveedor_id = prov.proveedor_id
ORDER BY t.fecha DESC;
GO

PRINT 'Vista Vista_Transacciones creada correctamente.';
GO

-- 3. CREAR FUNCIONES
-- ============================================================================

-- Función 1: CalcularIVA (Función Escalar)
-- Calcula el 12% de IVA de un monto
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = 'CalcularIVA' AND ROUTINE_TYPE = 'FUNCTION')
    DROP FUNCTION dbo.CalcularIVA;
GO

CREATE FUNCTION dbo.CalcularIVA(@monto DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @iva DECIMAL(10,2);
    SET @iva = @monto * 0.12;
    RETURN @iva;
END;
GO

PRINT 'Función CalcularIVA creada correctamente.';
GO

-- Función 2: TransaccionesPorProveedor (Función de Tabla)
-- Retorna todas las transacciones asociadas a un proveedor
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = 'TransaccionesPorProveedor' AND ROUTINE_TYPE = 'FUNCTION')
    DROP FUNCTION dbo.TransaccionesPorProveedor;
GO

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
GO

PRINT 'Función TransaccionesPorProveedor creada correctamente.';
GO

-- 4. CREAR PROCEDIMIENTOS ALMACENADOS
-- ============================================================================

-- Procedimiento 1: InsertarCompra
-- Registra una compra, actualiza el stock e inserta la transacción
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = 'InsertarCompra' AND ROUTINE_TYPE = 'PROCEDURE')
    DROP PROCEDURE dbo.InsertarCompra;
GO

CREATE PROCEDURE dbo.InsertarCompra
    @producto_id INT,
    @proveedor_id INT,
    @cantidad INT,
    @monto DECIMAL(10,2)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Verificar que el producto existe
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id)
        BEGIN
            THROW 50001, 'El producto no existe.', 1;
        END;
        
        -- Verificar que el proveedor existe
        IF NOT EXISTS (SELECT 1 FROM dbo.Proveedores WHERE proveedor_id = @proveedor_id)
        BEGIN
            THROW 50002, 'El proveedor no existe.', 1;
        END;
        
        -- Actualizar el stock
        UPDATE dbo.Productos
        SET stock = stock + @cantidad
        WHERE producto_id = @producto_id;
        
        -- Insertar la transacción
        INSERT INTO dbo.Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (@producto_id, @proveedor_id, GETDATE(), @cantidad, 'COMPRA', @monto);
        
        COMMIT TRANSACTION;
        PRINT 'Compra registrada correctamente.';
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO

PRINT 'Procedimiento InsertarCompra creado correctamente.';
GO

-- Procedimiento 2: InsertarVenta
-- Registra una venta, reduce el stock e inserta la transacción
IF EXISTS (SELECT * FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_NAME = 'InsertarVenta' AND ROUTINE_TYPE = 'PROCEDURE')
    DROP PROCEDURE dbo.InsertarVenta;
GO

CREATE PROCEDURE dbo.InsertarVenta
    @producto_id INT,
    @proveedor_id INT,
    @cantidad INT,
    @monto DECIMAL(10,2)
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        
        -- Verificar que el producto existe
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id)
        BEGIN
            THROW 50001, 'El producto no existe.', 1;
        END;
        
        -- Verificar que el proveedor existe
        IF NOT EXISTS (SELECT 1 FROM dbo.Proveedores WHERE proveedor_id = @proveedor_id)
        BEGIN
            THROW 50002, 'El proveedor no existe.', 1;
        END;
        
        -- Verificar que hay suficiente stock
        IF NOT EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id AND stock >= @cantidad)
        BEGIN
            THROW 50003, 'Stock insuficiente para realizar la venta.', 1;
        END;
        
        -- Actualizar el stock (reducir)
        UPDATE dbo.Productos
        SET stock = stock - @cantidad
        WHERE producto_id = @producto_id;
        
        -- Insertar la transacción
        INSERT INTO dbo.Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (@producto_id, @proveedor_id, GETDATE(), @cantidad, 'VENTA', @monto);
        
        COMMIT TRANSACTION;
        PRINT 'Venta registrada correctamente.';
    END TRY
    BEGIN CATCH
        ROLLBACK TRANSACTION;
        THROW;
    END CATCH;
END;
GO

PRINT 'Procedimiento InsertarVenta creado correctamente.';
GO

-- 5. CREAR TRIGGERS
-- ============================================================================

-- Trigger 1: Auditoría de Transacciones
-- Audita los INSERT en la tabla Transacciones
IF EXISTS (SELECT * FROM sys.triggers WHERE name = 'trg_AuditoriaTransacciones')
    DROP TRIGGER dbo.trg_AuditoriaTransacciones;
GO

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
    
    PRINT 'Transacción auditada correctamente.';
END;
GO

PRINT 'Trigger trg_AuditoriaTransacciones creado correctamente.';
GO

-- Trigger 2: Validación de Stock Negativo
-- Impide que el stock de un producto sea negativo
IF EXISTS (SELECT * FROM sys.triggers WHERE name = 'trg_ValidarStockNegativo')
    DROP TRIGGER dbo.trg_ValidarStockNegativo;
GO

CREATE TRIGGER dbo.trg_ValidarStockNegativo
ON dbo.Transacciones
AFTER INSERT
AS
BEGIN
    DECLARE @producto_id INT, @tipo VARCHAR(50);
    
    SELECT @producto_id = producto_id, @tipo = tipo
    FROM inserted;
    
    -- Si es una VENTA, verificar que el stock no sea negativo
    IF @tipo = 'VENTA'
    BEGIN
        IF EXISTS (SELECT 1 FROM dbo.Productos WHERE producto_id = @producto_id AND stock < 0)
        BEGIN
            ROLLBACK TRANSACTION;
            THROW 50004, 'Error: El stock del producto no puede ser negativo. La operación ha sido cancelada.', 1;
        END;
    END;
END;
GO

PRINT 'Trigger trg_ValidarStockNegativo creado correctamente.';
GO

-- ============================================================================
-- FIN DEL SCRIPT
-- ============================================================================
PRINT '
===============================================================
TODOS LOS OBJETOS HAN SIDO CREADOS EXITOSAMENTE
===============================================================
Vistas creadas:
  - Vista_ProductosActivos
  - Vista_Transacciones

Funciones creadas:
  - CalcularIVA
  - TransaccionesPorProveedor

Procedimientos creados:
  - InsertarCompra
  - InsertarVenta

Triggers creados:
  - trg_AuditoriaTransacciones
  - trg_ValidarStockNegativo

Tabla de auditoría creada:
  - Auditoria_Transacciones
===============================================================
';
GO
