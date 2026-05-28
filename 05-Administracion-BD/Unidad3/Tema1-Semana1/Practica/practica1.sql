CREATE DATABASE Nodo_Matriz;
CREATE DATABASE Nodo_Norte;
CREATE DATABASE Nodo_Seguro;

---------------------------------------------------------
--Fragmento horizontal 1, estudiantes de la sede Riobamba-
---------------------------------------------------------
USE Nodo_Matriz;
CREATE TABLE Estudiantes_Riobamba (
ID_Est INT PRIMARY KEY,
Nombre VARCHAR(50),
Ciudad VARCHAR(50) CHECK (Ciudad = 'Riobamba'),
Carrera VARCHAR(50)
);

---------------------------------------------------------
--Fragmento Horizontal 2, estudiantes de la sede Quito --
---------------------------------------------------------
USE Nodo_Norte;
CREATE TABLE Estudiantes_Quito (
ID_Est INT PRIMARY KEY,
Nombre VARCHAR(50),
Ciudad VARCHAR(50) CHECK (Ciudad = 'Quito'),
Carrera VARCHAR(50)
);
GO

---------------------------------------------------------
--4. Fragmentación Vertical 1, datos académicos --
---------------------------------------------------------


USE Nodo_Matriz;
CREATE TABLE Expediente_Academico (
ID_Est INT PRIMARY KEY,
Record_Academico DECIMAL(4,2),
Asistencias INT
);

---------------------------------------------------------
--5. Fragmentación Vertical 2, datos financieros --
---------------------------------------------------------


USE Nodo_Seguro;
CREATE TABLE Expediente_Financiero (
ID_Est INT PRIMARY KEY, -- Clave primaria necesaria para el RECONSTRUIR con JOIN
Valor_Matricula DECIMAL(6,2),
Estado_Cuenta VARCHAR(20)
);
GO

---------------------------------------------------------
--6. Reconstrucción de la Fragmentación Horizontal usando UNION ALL --
---------------------------------------------------------

USE Nodo_Matriz;
GO
CREATE VIEW V_Estudiantes_Global AS
SELECT * FROM Nodo_Matriz.dbo.Estudiantes_Riobamba
UNION ALL
SELECT * FROM Nodo_Norte.dbo.Estudiantes_Quito;
GO

---------------------------------------------------------
--7. Reconstrucción de la Fragmentación Vertical usando JOIN --
---------------------------------------------------------

CREATE VIEW V_Expediente_Completo AS
SELECT A.ID_Est, A.Record_Academico, A.Asistencias,
F.Valor_Matricula, F.Estado_Cuenta
FROM Nodo_Matriz.dbo.Expediente_Academico A
INNER JOIN Nodo_Seguro.dbo.Expediente_Financiero F ON A.ID_Est =
F.ID_Est;
GO

---------------------------------------------------------
--8. Insertar datos en los fragmentos --
---------------------------------------------------------
INSERT INTO Nodo_Matriz.dbo.Estudiantes_Riobamba 
VALUES (102,'Lenin Lopez','Riobamba', 'ING');

INSERT INTO Nodo_Norte.dbo.Estudiantes_Quito 
VALUES (102,'Nariana Perez','Quito', 'ING');


INSERT INTO Nodo_Matriz.dbo.Expediente_Academico 
VALUES (101,9.5,100)

INSERT INTO Nodo_Seguro.dbo.Expediente_Financiero 
VALUES (102,250.50,'Matriculado')



SELECT * FROM V_Estudiantes_Global
SELECT * FROM V_Expediente_Completo

---------------------------------------------------------
--   9. Consultar las vistas --
---------------------------------------------------------




