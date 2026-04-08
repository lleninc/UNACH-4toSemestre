
-- Crear base de datos si no existe
IF DB_ID('Vuelos') IS NULL
BEGIN
    CREATE DATABASE Vuelos;
END;
GO

USE Vuelos;
GO

-- Crear Tablas Base
CREATE TABLE Vuelos (
    vuelo_id INT PRIMARY KEY,
    destino VARCHAR(50),
    asientos_disponibles INT,
    precio DECIMAL(10,2)
);

CREATE TABLE Reservas (
    reserva_id INT IDENTITY(1,1) PRIMARY KEY,
    vuelo_id INT,
    pasajero_nombre VARCHAR(100),
    fecha_reserva DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (vuelo_id) REFERENCES Vuelos(vuelo_id)
);

-- Insertar datos de prueba
INSERT INTO Vuelos VALUES (101, 'Galápagos', 2, 150.00), (102, 'Quito', 15, 60.00);