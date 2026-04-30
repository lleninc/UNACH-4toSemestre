# AUTONOMO 2: Implementación de Vistas, Funciones, Procedimientos y Triggers

**Asignatura:** Administración de Bases de Datos  
**Unidad:** Unidad 1 - Programación avanzada en SQL  
**Tema:** Tema 2 - Programación en SQL  
**Semana:** 4

---

## 1. OBJETIVO DE LA ACTIVIDAD

Ampliar el sistema de inventario y proveedores mediante la creación de vistas, funciones, procedimientos almacenados y triggers, aplicando buenas prácticas de programación en SQL para mejorar la seguridad, la eficiencia y la automatización en la gestión de bases de datos.

---

## 2. BASE DE DATOS UTILIZADA

- **Servidor:** localhost\SQLEXPRESS
- **Base de datos:** InventarioProveedores_LL
- **Tablas existentes:**
  - `Productos` (producto_id, nombre, categoria, precio, stock)
  - `Proveedores` (proveedor_id, nombre, contacto, ciudad)
  - `Transacciones` (transaccion_id, producto_id, proveedor_id, fecha, cantidad, tipo, monto)

---

## 3. OBJETOS CREADOS

### 3.1 TABLA DE AUDITORÍA

Se creó la tabla `Auditoria_Transacciones` para registrar todas las transacciones:

```sql
CREATE TABLE dbo.Auditoria_Transacciones
(
    auditoria_id INT PRIMARY KEY IDENTITY(1,1),
    transaccion_id INT NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    fecha DATETIME NOT NULL,
    fecha_auditoria DATETIME DEFAULT GETDATE()
);
```

**Propósito:** Mantener un registro histórico de todas las operaciones (INSERT) realizadas en la tabla Transacciones.

---

### 3.2 VISTAS

#### Vista 1: Vista_ProductosActivos

```sql
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
```

**Propósito:** Mostrar todos los productos con stock mayor a 0 junto con el nombre del proveedor.

**Columnas retornadas:**
- `producto_id`: ID del producto
- `nombre_producto`: Nombre del producto
- `categoria`: Categoría del producto
- `precio`: Precio del producto
- `stock`: Cantidad en inventario
- `nombre_proveedor`: Nombre del proveedor
- `proveedor_id`: ID del proveedor

---

#### Vista 2: Vista_Transacciones

```sql
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
```

**Propósito:** Mostrar todas las transacciones realizadas en el sistema (compras y ventas) con información completa.

**Columnas retornadas:**
- `transaccion_id`: ID único de la transacción
- `nombre_producto`: Nombre del producto
- `nombre_proveedor`: Nombre del proveedor
- `fecha`: Fecha de la transacción
- `cantidad`: Cantidad transaccionada
- `monto`: Monto de la transacción
- `tipo`: Tipo de transacción (COMPRA/VENTA)
- `proveedor_id`: ID del proveedor
- `producto_id`: ID del producto

---

### 3.3 FUNCIONES

#### Función 1: CalcularIVA (Función Escalar)

```sql
CREATE FUNCTION dbo.CalcularIVA(@monto DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @iva DECIMAL(10,2);
    SET @iva = @monto * 0.12;
    RETURN @iva;
END;
```

**Propósito:** Calcular el IVA (12%) de un monto dado.

**Parámetros:**
- `@monto`: Monto sobre el cual se calculará el IVA

**Retorna:** Valor del IVA calculado (12% del monto)

**Ejemplo de uso:**
```sql
SELECT dbo.CalcularIVA(100.00) AS IVA;  -- Resultado: 12.00
```

---

#### Función 2: TransaccionesPorProveedor (Función de Tabla)

```sql
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
```

**Propósito:** Retornar todas las transacciones asociadas a un proveedor específico.

**Parámetros:**
- `@proveedor_id`: ID del proveedor para filtrar

**Retorna:** Tabla con todas las transacciones del proveedor especificado

**Ejemplo de uso:**
```sql
SELECT * FROM dbo.TransaccionesPorProveedor(1);
```

---

### 3.4 PROCEDIMIENTOS ALMACENADOS

#### Procedimiento 1: InsertarCompra

```sql
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
```

**Propósito:** Registrar una compra de un producto, actualizar el stock e insertar la transacción de forma atómica.

**Parámetros:**
- `@producto_id`: ID del producto a comprar
- `@proveedor_id`: ID del proveedor
- `@cantidad`: Cantidad a comprar
- `@monto`: Monto de la compra

**Características:**
- Valida la existencia del producto y proveedor
- Aumenta el stock del producto
- Registra la transacción como COMPRA
- Usa transacciones para garantizar integridad (ACID)

**Ejemplo de uso:**
```sql
EXEC dbo.InsertarCompra @producto_id = 1, @proveedor_id = 1, @cantidad = 10, @monto = 500.00;
```

---

#### Procedimiento 2: InsertarVenta

```sql
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
```

**Propósito:** Registrar una venta de un producto, reducir el stock e insertar la transacción de forma atómica.

**Parámetros:**
- `@producto_id`: ID del producto a vender
- `@proveedor_id`: ID del proveedor
- `@cantidad`: Cantidad a vender
- `@monto`: Monto de la venta

**Características:**
- Valida la existencia del producto y proveedor
- Valida que hay suficiente stock disponible
- Reduce el stock del producto
- Registra la transacción como VENTA
- Usa transacciones para garantizar integridad (ACID)

**Ejemplo de uso:**
```sql
EXEC dbo.InsertarVenta @producto_id = 1, @proveedor_id = 1, @cantidad = 5, @monto = 250.00;
```

---

### 3.5 TRIGGERS

#### Trigger 1: Auditoría de Transacciones (trg_AuditoriaTransacciones)

```sql
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
```

**Propósito:** Auditar automáticamente todas las operaciones INSERT en la tabla Transacciones, registrando el ID de la transacción, el tipo (COMPRA/VENTA) y la fecha.

**Comportamiento:**
- Se ejecuta AFTER INSERT en Transacciones
- Registra cada nueva transacción en la tabla Auditoria_Transacciones
- Mantiene un historial completo de todas las operaciones

**Tipo:** AFTER INSERT

---

#### Trigger 2: Validación de Stock Negativo (trg_ValidarStockNegativo)

```sql
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
```

**Propósito:** Impedir que el stock de un producto quede en valores negativos al intentar registrar una venta.

**Comportamiento:**
- Se ejecuta AFTER INSERT en Transacciones
- Verifica si es una transacción de tipo VENTA
- Si el stock resulta negativo, cancela la transacción con ROLLBACK
- Lanza una excepción descriptiva

**Tipo:** AFTER INSERT

---

## 4. NOTAS TÉCNICAS

### Buenas prácticas implementadas:

1. **Transacciones ACID:** Los procedimientos utilizan BEGIN TRANSACTION y COMMIT/ROLLBACK para garantizar consistencia de datos.

2. **Validación de datos:** Se valida la existencia de registros relacionados antes de realizar operaciones.

3. **Manejo de errores:** Se utilizan TRY-CATCH para capturar y manejar excepciones.

4. **Auditoría automática:** El trigger de auditoría registra todas las transacciones automáticamente.

5. **Integridad referencial:** Los triggers validan restricciones de negocio (stock no negativo).

6. **Nomenclatura clara:** Se utilizan prefijos para triggers (trg_) y vistas (Vista_) para facilitar identificación.

---

## 5. ESQUEMA RELACIONAL

```
┌─────────────────────┐
│    Productos        │
├─────────────────────┤
│ producto_id (PK)    │
│ nombre              │
│ categoria           │
│ precio              │
│ stock               │
└─────────────────────┘
          │
          │ FK
          │
┌─────────────────────┐         ┌──────────────────────┐
│  Transacciones      │─────────│  Auditoria_Transacc. │
├─────────────────────┤         ├──────────────────────┤
│ transaccion_id (PK) │         │ auditoria_id (PK)    │
│ producto_id (FK)    │         │ transaccion_id (FK)  │
│ proveedor_id (FK)   │         │ tipo                 │
│ fecha               │         │ fecha                │
│ cantidad            │         │ fecha_auditoria      │
│ tipo                │         └──────────────────────┘
│ monto               │
└─────────────────────┘
          │
          │ FK
          │
┌─────────────────────┐
│   Proveedores       │
├─────────────────────┤
│ proveedor_id (PK)   │
│ nombre              │
│ contacto            │
│ ciudad              │
└─────────────────────┘
```

---

## 6. CONCLUSIONES

Se han implementado exitosamente todos los objetos solicitados:

✅ **2 Vistas** - Para consultas optimizadas  
✅ **2 Funciones** - Para cálculos y consultas parametrizadas  
✅ **2 Procedimientos** - Para operaciones transaccionales  
✅ **2 Triggers** - Para auditoría y validación automática  

Todos los objetos siguen buenas prácticas de SQL y proporcionan:
- **Seguridad** mediante validación de datos
- **Integridad** mediante transacciones ACID
- **Automatización** mediante triggers
- **Eficiencia** mediante vistas y funciones optimizadas

---

**Fecha de realización:** 29 de abril de 2026  
**Base de datos:** InventarioProveedores_LL  
**Servidor:** localhost\SQLEXPRESS
