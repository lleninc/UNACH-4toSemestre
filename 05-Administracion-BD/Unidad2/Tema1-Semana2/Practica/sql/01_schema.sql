USE SistemaVentas;
GO

IF OBJECT_ID('dbo.Productos', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Productos (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(50) NOT NULL,
        Precio DECIMAL(10,2) NOT NULL,
        FechaRegistro DATETIME NOT NULL DEFAULT GETDATE()
    );
END
GO

IF OBJECT_ID('dbo.Clientes', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Clientes (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        Nombre VARCHAR(80) NOT NULL,
        Ciudad VARCHAR(60) NOT NULL,
        FechaRegistro DATETIME NOT NULL DEFAULT GETDATE()
    );
END
GO

IF OBJECT_ID('dbo.Ventas', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.Ventas (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        ClienteId INT NOT NULL,
        FechaVenta DATETIME2 NOT NULL DEFAULT SYSDATETIME(),
        Total DECIMAL(12,2) NOT NULL DEFAULT 0,
        Canal VARCHAR(20) NOT NULL DEFAULT 'Web',
        Estado VARCHAR(20) NOT NULL DEFAULT 'Registrada',
        CONSTRAINT FK_Ventas_Clientes FOREIGN KEY (ClienteId) REFERENCES dbo.Clientes(Id)
    );
END
GO

IF OBJECT_ID('dbo.DetalleVenta', 'U') IS NULL
BEGIN
    CREATE TABLE dbo.DetalleVenta (
        Id INT IDENTITY(1,1) PRIMARY KEY,
        VentaId INT NOT NULL,
        ProductoId INT NOT NULL,
        Cantidad INT NOT NULL,
        PrecioUnitario DECIMAL(10,2) NOT NULL,
        Subtotal DECIMAL(12,2) NOT NULL,
        CONSTRAINT FK_DetalleVenta_Ventas FOREIGN KEY (VentaId) REFERENCES dbo.Ventas(Id),
        CONSTRAINT FK_DetalleVenta_Productos FOREIGN KEY (ProductoId) REFERENCES dbo.Productos(Id)
    );
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Clientes)
BEGIN
    INSERT INTO dbo.Clientes (Nombre, Ciudad)
    VALUES
        ('Ana Torres', 'Quito'),
        ('Luis Mendez', 'Guayaquil'),
        ('Maria Paredes', 'Cuenca'),
        ('Carlos Vega', 'Ambato'),
        ('Sofia Castro', 'Manta'),
        ('Jorge Ruiz', 'Loja'),
        ('Daniela Perez', 'Riobamba'),
        ('Pedro Cardenas', 'Machala');
END
GO

IF NOT EXISTS (SELECT 1 FROM dbo.Productos)
BEGIN
    INSERT INTO dbo.Productos (Nombre, Precio)
    VALUES
        ('Laptop', 1200.00),
        ('Mouse', 25.00),
        ('Teclado', 45.00),
        ('Monitor', 300.00),
        ('Audifonos', 35.00),
        ('Webcam', 60.00),
        ('Impresora', 150.00),
        ('Parlantes', 80.00),
        ('Silla Ergonomica', 220.00),
        ('Disco SSD 1TB', 95.00),
        ('Router', 70.00),
        ('Tablet', 250.00);
END
GO
