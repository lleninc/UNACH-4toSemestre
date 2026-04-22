CREATE DATABASE Peliculas;

USE Peliculas;


CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY IDENTITY(1,1),
    nombre VARCHAR(100),
    suscripcion VARCHAR(20), -- 'Gratis', 'Estándar', 'Premium'
    fecha_registro DATE DEFAULT GETDATE()
);

CREATE TABLE Contenido (
    id_contenido INT PRIMARY KEY IDENTITY(1,1),
    titulo VARCHAR(150),
    tipo VARCHAR(20), -- 'Película', 'Serie'
    duracion_total_min INT,
    es_estreno BIT DEFAULT 0 -- 1 para estrenos, 0 para catálogo normal
);

CREATE TABLE Historial_Visualizacion (
    id_historial INT PRIMARY KEY IDENTITY(1,1),
    id_usuario INT,
    id_contenido INT,
    minutos_vistos INT,
    fecha_vista DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_contenido) REFERENCES Contenido(id_contenido)
);

CREATE TABLE Alertas_Consumo (
    id_alerta INT PRIMARY KEY IDENTITY(1,1),
    mensaje VARCHAR(255),
    fecha_alerta DATETIME DEFAULT GETDATE()
);


INSERT INTO Usuarios (nombre, suscripcion) VALUES ('Alicia Durán', 'Premium'), ('Robert Martínez', 'Gratis'), ('Carlos Castillo', 'Estándar');
INSERT INTO Contenido (titulo, tipo, duracion_total_min, es_estreno) 
VALUES ('Los puentes', 'Película', 120, 1), ('Bajo el agua', 'Serie', 45, 0), ('Escape extremo', 'Película', 90, 0);
INSERT INTO Historial_Visualizacion (id_usuario, id_contenido, minutos_vistos) VALUES (1, 1, 60), (2, 2, 45), (1, 3, 10);