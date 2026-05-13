import os
import random
from datetime import datetime

import pyodbc

SERVER = os.getenv('SQL_SERVER', 'FRANCIS')
DATABASE = os.getenv('SQL_DATABASE', 'SistemaVentas')
DRIVER = os.getenv('SQL_DRIVER', 'ODBC Driver 17 for SQL Server')
USE_TRUSTED = os.getenv('SQL_TRUSTED_CONNECTION', 'yes').lower() in {'1', 'true', 'yes', 'si'}
SQL_USERNAME = os.getenv('SQL_USERNAME', '')
SQL_PASSWORD = os.getenv('SQL_PASSWORD', '')
BACKUP_DIR = os.getenv(
    'SQL_BACKUP_DIR',
    r'E:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\05-Administracion-BD\Unidad2\Tema1-Semana2\Practica\Backups',
)


def connection_string(database: str | None = None) -> str:
    target_database = database or DATABASE
    parts = [f'Driver={{{DRIVER}}}', f'Server={SERVER}', f'Database={target_database}', 'TrustServerCertificate=yes']
    if USE_TRUSTED or not SQL_USERNAME:
        parts.append('Trusted_Connection=yes')
    else:
        parts.append(f'Uid={SQL_USERNAME}')
        parts.append(f'Pwd={SQL_PASSWORD}')
    return ';'.join(parts) + ';'


def get_connection(database: str | None = None):
    return pyodbc.connect(connection_string(database), autocommit=False)


def _run_statements(cursor, statements):
    for statement in statements:
        cursor.execute(statement)


def ensure_schema(connection):
    cursor = connection.cursor()
    statements = [
        """
        IF OBJECT_ID('dbo.Productos', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Productos (
                Id INT IDENTITY(1,1) PRIMARY KEY,
                Nombre VARCHAR(50) NOT NULL,
                Precio DECIMAL(10,2) NOT NULL,
                FechaRegistro DATETIME NOT NULL DEFAULT GETDATE()
            );
        END
        """,
        """
        IF OBJECT_ID('dbo.Clientes', 'U') IS NULL
        BEGIN
            CREATE TABLE dbo.Clientes (
                Id INT IDENTITY(1,1) PRIMARY KEY,
                Nombre VARCHAR(80) NOT NULL,
                Ciudad VARCHAR(60) NOT NULL,
                FechaRegistro DATETIME NOT NULL DEFAULT GETDATE()
            );
        END
        """,
        """
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
        """,
        """
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
        """,
        """
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
        """,
        """
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
        """,
    ]
    _run_statements(cursor, statements)
    connection.commit()


def get_dashboard_stats(connection):
    cursor = connection.cursor()
    stats = {}
    cursor.execute('SELECT COUNT(*) FROM dbo.Productos')
    stats['productos'] = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM dbo.Clientes')
    stats['clientes'] = cursor.fetchone()[0]
    cursor.execute('SELECT COUNT(*) FROM dbo.Ventas')
    stats['ventas'] = cursor.fetchone()[0]
    cursor.execute('SELECT COALESCE(SUM(Total), 0) FROM dbo.Ventas')
    stats['ingresos'] = float(cursor.fetchone()[0] or 0)
    return stats


def seed_random_sale(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT Id FROM dbo.Clientes ORDER BY NEWID()')
    clientes = [row[0] for row in cursor.fetchall()]
    cursor.execute('SELECT Id, Precio FROM dbo.Productos ORDER BY NEWID()')
    productos = [(row[0], float(row[1])) for row in cursor.fetchall()]
    if not clientes or not productos:
        raise RuntimeError('No hay clientes o productos cargados')

    cliente_id = random.choice(clientes)
    detalle_cantidad = random.randint(1, 4)
    fecha = datetime.now()
    canal = random.choice(['Web', 'Tienda', 'WhatsApp'])

    cursor.execute(
        'INSERT INTO dbo.Ventas (ClienteId, FechaVenta, Total, Canal, Estado) OUTPUT INSERTED.Id VALUES (?, ?, ?, ?, ?)',
        cliente_id,
        fecha,
        0,
        canal,
        'Registrada',
    )
    venta_id = cursor.fetchone()[0]

    subtotales = []
    for _ in range(detalle_cantidad):
        producto_id, precio = random.choice(productos)
        cantidad = random.randint(1, 3)
        subtotal = round(precio * cantidad, 2)
        subtotales.append(subtotal)
        cursor.execute(
            'INSERT INTO dbo.DetalleVenta (VentaId, ProductoId, Cantidad, PrecioUnitario, Subtotal) VALUES (?, ?, ?, ?, ?)',
            venta_id,
            producto_id,
            cantidad,
            precio,
            subtotal,
        )

    total = round(sum(subtotales), 2)
    cursor.execute('UPDATE dbo.Ventas SET Total = ? WHERE Id = ?', total, venta_id)
    connection.commit()
    return {'venta_id': venta_id, 'total': total, 'canal': canal, 'fecha': fecha.isoformat(sep=' ', timespec='seconds')}


def get_backup_history(connection, limit=50):
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT TOP (?)
            bs.backup_finish_date,
            bs.type,
            bs.name,
            CAST(bs.backup_size / 1024.0 / 1024.0 AS DECIMAL(18,2)) AS backup_size_mb,
            bmf.physical_device_name
        FROM msdb.dbo.backupset bs
        LEFT JOIN msdb.dbo.backupmediafamily bmf ON bs.media_set_id = bmf.media_set_id
        WHERE bs.database_name = ?
        ORDER BY bs.backup_finish_date DESC;
        """,
        limit,
        DATABASE,
    )
    rows = []
    for row in cursor.fetchall():
        rows.append(
            {
                'fecha': row.backup_finish_date.strftime('%Y-%m-%d %H:%M:%S') if row.backup_finish_date else '',
                'tipo': {'D': 'FULL', 'I': 'DIFF', 'L': 'LOG'}.get(row.type, row.type),
                'nombre': row.name,
                'tamano_mb': float(row.backup_size_mb or 0),
                'archivo': row.physical_device_name,
            }
        )
    return rows
