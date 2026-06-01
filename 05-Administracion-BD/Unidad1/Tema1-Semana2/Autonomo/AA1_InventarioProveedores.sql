-- ============================================================
--  ACTIVIDAD AUTÓNOMA 1 - ADMINISTRACIÓN DE BASES DE DATOS
--  Sistema de Inventario y Proveedores
--  Motor: SQL Server (T-SQL)
--  Autor: Lenin Lara
--  Carrera: Ciencia de Datos e Inteligencia Artificial
--  Periodo: 2026-1S  |  UNACH
-- ============================================================

-- ============================================================
-- PARTE 1: CREACIÓN DEL ESQUEMA DE BASE DE DATOS
-- ============================================================

-- Crear y usar la base de datos
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'InventarioProveedores')
    CREATE DATABASE InventarioProveedores;
GO

USE InventarioProveedores;
GO

-- ----------------------------------------------------------
-- Tabla: Proveedores
-- ----------------------------------------------------------
IF OBJECT_ID('Transacciones', 'U') IS NOT NULL DROP TABLE Transacciones;
IF OBJECT_ID('Productos',     'U') IS NOT NULL DROP TABLE Productos;
IF OBJECT_ID('Proveedores',   'U') IS NOT NULL DROP TABLE Proveedores;
GO

CREATE TABLE Proveedores (
    proveedor_id INT           IDENTITY(1,1) PRIMARY KEY,
    nombre       VARCHAR(100)  NOT NULL,
    contacto     VARCHAR(100)  NOT NULL,
    ciudad       VARCHAR(80)   NOT NULL
);
GO

-- ----------------------------------------------------------
-- Tabla: Productos
-- ----------------------------------------------------------
CREATE TABLE Productos (
    producto_id INT            IDENTITY(1,1) PRIMARY KEY,
    nombre      VARCHAR(100)   NOT NULL,
    categoria   VARCHAR(80)    NOT NULL,
    precio      DECIMAL(10,2)  NOT NULL CHECK (precio > 0),
    stock       INT            NOT NULL CHECK (stock >= 0)
);
GO

-- ----------------------------------------------------------
-- Tabla: Transacciones
-- ----------------------------------------------------------
CREATE TABLE Transacciones (
    transaccion_id INT           IDENTITY(1,1) PRIMARY KEY,
    producto_id    INT           NOT NULL REFERENCES Productos(producto_id),
    proveedor_id   INT           NOT NULL REFERENCES Proveedores(proveedor_id),
    fecha          DATETIME      NOT NULL DEFAULT GETDATE(),
    cantidad       INT           NOT NULL CHECK (cantidad > 0),
    tipo           VARCHAR(10)   NOT NULL CHECK (tipo IN ('COMPRA','VENTA')),
    monto          DECIMAL(12,2) NOT NULL CHECK (monto > 0)
);
GO

-- ----------------------------------------------------------
-- Índices recomendados (sección 1.4 del contenido)
-- ----------------------------------------------------------
-- Índice no agrupado sobre producto_id en Transacciones
-- (consultas frecuentes filtran por producto)
CREATE NONCLUSTERED INDEX IX_Trans_ProductoId
    ON Transacciones (producto_id);

-- Índice no agrupado sobre proveedor_id en Transacciones
CREATE NONCLUSTERED INDEX IX_Trans_ProveedorId
    ON Transacciones (proveedor_id);

-- Índice no agrupado sobre tipo (COMPRA / VENTA)
CREATE NONCLUSTERED INDEX IX_Trans_Tipo
    ON Transacciones (tipo);

-- Índice no agrupado sobre categoría en Productos
CREATE NONCLUSTERED INDEX IX_Prod_Categoria
    ON Productos (categoria);
GO

-- ----------------------------------------------------------
-- Datos de prueba
-- ----------------------------------------------------------
INSERT INTO Proveedores (nombre, contacto, ciudad) VALUES
    ('TechSupply Ecuador',  'tech@supply.ec',    'Quito'),
    ('DataComp S.A.',       'ventas@datacomp.ec', 'Guayaquil'),
    ('InnovateTech Cía.',   'info@innovate.ec',   'Cuenca');

INSERT INTO Productos (nombre, categoria, precio, stock) VALUES
    ('Laptop Core i7 16GB',  'Computación',  1250.00, 30),
    ('Monitor 27" 4K',       'Periféricos',   450.00, 50),
    ('SSD NVMe 1TB',         'Almacenamiento', 120.00, 80),
    ('Teclado Mecánico RGB', 'Periféricos',    85.00, 60),
    ('Switch 24 puertos',    'Redes',          320.00, 15);
GO

-- ============================================================
-- PARTE 2: TRANSACCIONES ACID
-- ============================================================

-- ----------------------------------------------------------
-- 2a. TRANSACCIÓN DE COMPRA (incrementa stock)
--     Propiedad demostrada: Atomicidad, Consistencia,
--     Aislamiento y Durabilidad
-- ----------------------------------------------------------
PRINT '--- TRANSACCIÓN COMPRA: Laptop Core i7 ---';

BEGIN TRY
    BEGIN TRANSACTION;

        -- Paso 1: Registrar la compra en Transacciones
        INSERT INTO Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (1, 1, GETDATE(), 10, 'COMPRA', 12500.00);

        -- Paso 2: Actualizar stock del producto
        UPDATE Productos
        SET stock = stock + 10
        WHERE producto_id = 1;

        -- Verificar stock actualizado
        DECLARE @stock_post_compra INT;
        SELECT @stock_post_compra = stock FROM Productos WHERE producto_id = 1;
        PRINT 'Stock tras COMPRA: ' + CAST(@stock_post_compra AS VARCHAR);

    COMMIT TRANSACTION;
    PRINT 'COMPRA confirmada con COMMIT.';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'ERROR en COMPRA — se aplicó ROLLBACK.';
    PRINT 'Mensaje: ' + ERROR_MESSAGE();
END CATCH;
GO

-- ----------------------------------------------------------
-- 2b. TRANSACCIÓN DE VENTA (reduce stock)
--     Incluye validación de stock suficiente
-- ----------------------------------------------------------
PRINT '--- TRANSACCIÓN VENTA: Monitor 27" 4K ---';

BEGIN TRY
    BEGIN TRANSACTION;

        DECLARE @cantidad_venta INT   = 5;
        DECLARE @stock_actual   INT;
        DECLARE @precio_unit    DECIMAL(10,2);

        -- Bloqueo de fila: SELECT ... WITH (UPDLOCK)
        -- Garantiza que nadie más modifique esta fila mientras validamos
        SELECT @stock_actual = stock, @precio_unit = precio
        FROM Productos WITH (UPDLOCK, ROWLOCK)
        WHERE producto_id = 2;

        -- Validación de negocio: stock suficiente
        IF @stock_actual < @cantidad_venta
        BEGIN
            RAISERROR('Stock insuficiente. Disponible: %d, solicitado: %d',
                      16, 1, @stock_actual, @cantidad_venta);
        END

        -- Paso 1: Registrar la venta
        INSERT INTO Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (2, 2, GETDATE(), @cantidad_venta, 'VENTA', @precio_unit * @cantidad_venta);

        -- Paso 2: Reducir stock
        UPDATE Productos
        SET stock = stock - @cantidad_venta
        WHERE producto_id = 2;

        DECLARE @stock_post_venta INT;
        SELECT @stock_post_venta = stock FROM Productos WHERE producto_id = 2;
        PRINT 'Stock tras VENTA: ' + CAST(@stock_post_venta AS VARCHAR);

    COMMIT TRANSACTION;
    PRINT 'VENTA confirmada con COMMIT.';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'ERROR en VENTA — se aplicó ROLLBACK.';
    PRINT 'Mensaje: ' + ERROR_MESSAGE();
END CATCH;
GO

-- ----------------------------------------------------------
-- 2c. TRANSACCIÓN CON ROLLBACK FORZADO
--     Simula un error en el segundo paso para demostrar
--     la propiedad de Atomicidad (todo o nada)
-- ----------------------------------------------------------
PRINT '--- DEMO ROLLBACK: Error intencional en paso 2 ---';

BEGIN TRY
    BEGIN TRANSACTION;

        -- Paso 1: Inserción correcta
        INSERT INTO Transacciones (producto_id, proveedor_id, fecha, cantidad, tipo, monto)
        VALUES (3, 1, GETDATE(), 20, 'COMPRA', 2400.00);

        PRINT 'Paso 1 completado. Simulando error en paso 2...';

        -- Paso 2: Error intencional (stock negativo no permitido por CHECK)
        UPDATE Productos
        SET stock = -999
        WHERE producto_id = 3;

    COMMIT TRANSACTION;
    PRINT 'COMMIT (no debería llegar aquí)';
END TRY
BEGIN CATCH
    ROLLBACK TRANSACTION;
    PRINT 'ERROR detectado — ROLLBACK ejecutado. Integridad preservada.';
    PRINT 'Mensaje: ' + ERROR_MESSAGE();
END CATCH;
GO

-- ============================================================
-- PARTE 3: CONTROL DE BLOQUEOS Y NIVELES DE AISLAMIENTO
-- ============================================================

-- ----------------------------------------------------------
-- 3a. SIMULACIÓN — BLOQUEO DE FILA (ROWLOCK + UPDLOCK)
--     Transacción A: obtiene el bloqueo y actualiza
--     Transacción B: debe esperar a que A haga COMMIT
--     (en un entorno real se ejecutan en sesiones paralelas)
-- ----------------------------------------------------------
PRINT '--- DEMO BLOQUEO DE FILA ---';

-- === TRANSACCIÓN A (ejecutar en Sesión 1) ===
BEGIN TRANSACTION;

    -- FOR UPDATE equivalente en T-SQL: UPDLOCK + ROWLOCK
    -- Bloquea la fila del SSD NVMe mientras dure la transacción
    SELECT producto_id, nombre, stock
    FROM Productos WITH (UPDLOCK, ROWLOCK)
    WHERE producto_id = 3;

    PRINT 'Transacción A: fila bloqueada. Actualizando stock...';

    UPDATE Productos
    SET stock = stock - 5
    WHERE producto_id = 3;

COMMIT TRANSACTION;
PRINT 'Transacción A: COMMIT ejecutado. Bloqueo liberado.';
GO

-- === TRANSACCIÓN B (simulada en el mismo script, llegaría después) ===
-- En una sesión paralela real, este SELECT WITH (UPDLOCK) habría
-- esperado hasta que A hiciera COMMIT antes de continuar.
BEGIN TRANSACTION;

    SELECT producto_id, nombre, stock
    FROM Productos WITH (UPDLOCK, ROWLOCK)
    WHERE producto_id = 3;

    PRINT 'Transacción B: obtuvo bloqueo tras COMMIT de A. Stock visible: ';
    SELECT stock FROM Productos WHERE producto_id = 3;

    UPDATE Productos
    SET stock = stock - 3
    WHERE producto_id = 3;

COMMIT TRANSACTION;
PRINT 'Transacción B: COMMIT ejecutado.';
GO

-- ----------------------------------------------------------
-- 3b. NIVEL DE AISLAMIENTO: READ COMMITTED (por defecto en SQL Server)
--     Evita lecturas sucias; puede haber lecturas no repetibles
-- ----------------------------------------------------------
PRINT '--- NIVEL: READ COMMITTED ---';

SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

BEGIN TRANSACTION;

    -- Solo se leen filas ya confirmadas por otras transacciones
    SELECT p.nombre, p.stock, p.precio,
           SUM(t.cantidad) AS unidades_movidas
    FROM Productos p
    LEFT JOIN Transacciones t ON p.producto_id = t.producto_id
    GROUP BY p.producto_id, p.nombre, p.stock, p.precio;

COMMIT TRANSACTION;
PRINT 'Consulta con READ COMMITTED completada.';
GO

-- ----------------------------------------------------------
-- 3c. NIVEL DE AISLAMIENTO: SERIALIZABLE
--     Máxima protección: evita lecturas sucias, no repetibles
--     y lecturas fantasma. Comportamiento equivalente a
--     ejecución secuencial de transacciones.
-- ----------------------------------------------------------
PRINT '--- NIVEL: SERIALIZABLE ---';

SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;

BEGIN TRANSACTION;

    -- Ninguna otra transacción puede insertar/modificar/leer
    -- registros que afecten este resultado hasta el COMMIT
    SELECT p.nombre        AS Producto,
           p.stock         AS Stock_Actual,
           p.precio        AS Precio_Unit,
           SUM(CASE WHEN t.tipo = 'COMPRA' THEN t.cantidad ELSE 0 END) AS Total_Comprado,
           SUM(CASE WHEN t.tipo = 'VENTA'  THEN t.cantidad ELSE 0 END) AS Total_Vendido,
           SUM(CASE WHEN t.tipo = 'COMPRA' THEN  t.monto ELSE -t.monto END) AS Flujo_Neto
    FROM Productos p
    LEFT JOIN Transacciones t ON p.producto_id = t.producto_id
    GROUP BY p.producto_id, p.nombre, p.stock, p.precio
    ORDER BY p.nombre;

COMMIT TRANSACTION;
PRINT 'Consulta con SERIALIZABLE completada. Máxima integridad garantizada.';
GO

-- ============================================================
-- PARTE 4: CONSULTAS AVANZADAS (JOIN, CTE, SUBCONSULTAS,
--          FUNCIONES DE VENTANA)
-- ============================================================

-- ----------------------------------------------------------
-- 4a. JOIN: Reporte completo de movimientos
-- ----------------------------------------------------------
PRINT '--- REPORTE: Movimientos con JOIN ---';

SELECT
    t.transaccion_id,
    p.nombre          AS Producto,
    p.categoria       AS Categoria,
    pr.nombre         AS Proveedor,
    pr.ciudad         AS Ciudad,
    t.fecha,
    t.tipo,
    t.cantidad,
    t.monto
FROM Transacciones t
INNER JOIN Productos   p  ON t.producto_id   = p.producto_id
INNER JOIN Proveedores pr ON t.proveedor_id  = pr.proveedor_id
ORDER BY t.fecha DESC;
GO

-- ----------------------------------------------------------
-- 4b. CTE: Resumen de movimientos por producto
-- ----------------------------------------------------------
PRINT '--- CTE: Resumen por producto ---';

WITH ResumenMovimientos AS (
    SELECT
        producto_id,
        SUM(CASE WHEN tipo = 'COMPRA' THEN cantidad ELSE 0 END) AS total_comprado,
        SUM(CASE WHEN tipo = 'VENTA'  THEN cantidad ELSE 0 END) AS total_vendido,
        SUM(CASE WHEN tipo = 'COMPRA' THEN monto ELSE -monto END) AS flujo_neto
    FROM Transacciones
    GROUP BY producto_id
)
SELECT
    p.nombre         AS Producto,
    p.stock          AS Stock_Actual,
    r.total_comprado AS Unid_Compradas,
    r.total_vendido  AS Unid_Vendidas,
    r.flujo_neto     AS Flujo_Neto_USD
FROM Productos p
LEFT JOIN ResumenMovimientos r ON p.producto_id = r.producto_id
ORDER BY r.flujo_neto DESC;
GO

-- ----------------------------------------------------------
-- 4c. SUBCONSULTA: Productos con stock por debajo del promedio
-- ----------------------------------------------------------
PRINT '--- SUBCONSULTA: Productos bajo stock promedio ---';

SELECT nombre, categoria, stock, precio
FROM Productos
WHERE stock < (SELECT AVG(stock) FROM Productos)
ORDER BY stock ASC;
GO

-- ----------------------------------------------------------
-- 4d. FUNCIÓN DE VENTANA: Ranking de productos por monto movido
-- ----------------------------------------------------------
PRINT '--- WINDOW FUNCTION: Ranking por monto ---';

SELECT
    p.nombre                                         AS Producto,
    t.tipo,
    t.monto,
    SUM(t.monto) OVER (PARTITION BY p.producto_id)   AS Total_Monto_Producto,
    RANK()       OVER (ORDER BY t.monto DESC)         AS Ranking_Monto,
    AVG(t.monto) OVER (PARTITION BY t.tipo)           AS Promedio_Por_Tipo
FROM Transacciones t
INNER JOIN Productos p ON t.producto_id = p.producto_id
ORDER BY t.monto DESC;
GO

-- ----------------------------------------------------------
-- 4e. CTE RECURSIVA: Cadena de suministro por proveedor
--     (jerarquía de categorías / rutas)
-- ----------------------------------------------------------
PRINT '--- CTE RECURSIVA: Jerarquía de proveedores ---';

WITH JerarquiaProveedores AS (
    -- Caso base: primer proveedor registrado
    SELECT proveedor_id, nombre, ciudad, 1 AS nivel
    FROM Proveedores
    WHERE proveedor_id = 1

    UNION ALL

    -- Paso recursivo: proveedores de niveles siguientes
    SELECT p.proveedor_id, p.nombre, p.ciudad, j.nivel + 1
    FROM Proveedores p
    INNER JOIN JerarquiaProveedores j ON p.proveedor_id = j.nivel + 1
    WHERE j.nivel < (SELECT COUNT(*) FROM Proveedores)
)
SELECT nivel AS Nivel, nombre AS Proveedor, ciudad AS Ciudad
FROM JerarquiaProveedores
ORDER BY nivel;
GO

-- ============================================================
-- FIN DEL SCRIPT
-- ============================================================
PRINT '=== Script AA1 ejecutado correctamente ===';
