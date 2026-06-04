CREATE DATABASE ClinicaDB;
GO
USE ClinicaDB;
GO

CREATE TABLE Pacientes (
    PacienteID INT PRIMARY KEY,
    Nombre VARCHAR(100),
    FechaNacimiento DATE
);

CREATE TABLE Atenciones_Medicas (
    AtencionID INT PRIMARY KEY,
    PacienteID INT FOREIGN KEY REFERENCES Pacientes(PacienteID),
    FechaAtencion DATE,
    CostoConsulta DECIMAL(10,2),
    Estado VARCHAR(20),
    VersionFila ROWVERSION
);

INSERT INTO Pacientes VALUES 
(1, 'Carlos Mantilla', '1985-05-12'),
(2, 'Ana Maria Lopez', '1990-09-20'),
(3, 'Luis Fernando Real', '1978-12-02');

INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado) VALUES 
(101, 1, '2026-01-10', 45.00, 'Completada'),
(102, 1, '2026-02-15', 50.00, 'Completada'),
(103, 2, '2026-03-01', 60.00, 'Completada'),
(104, 1, '2026-03-10', 45.00, 'Cancelada'),
(105, 3, '2026-04-12', 55.00, 'Completada'),
(106, 2, '2026-05-18', 60.00, 'Completada');

select * from Pacientes
select * from Atenciones_Medicas

--------------------------------
/*
Desarrolle una función llamada dbo.fn_CalcularNetoPaciente que reciba el PacienteID (INT). 
Debe retornar la suma de CostoConsulta de sus atenciones, omitiendo las que estén 'Cancelada'.
Una vez creada, ejecute:
SELECT CAST(dbo.fn_CalcularNetoPaciente(1) AS INT) AS Ref;
*/
GO
CREATE FUNCTION dbo.fn_CalcularNetoPaciente
(
@PacienteID INT
) RETURNS DECIMAL(10,2)
AS
BEGIN 
    DECLARE @TotalNeto DECIMAL(10,2)
    SELECT @TotalNeto = SUM(CostoConsulta) FROM Atenciones_Medicas
    WHERE PacienteID = @PacienteID and Estado<>'Cancelada';
    RETURN @TotalNeto;
END
GO

SELECT CAST(dbo.fn_CalcularNetoPaciente(1) AS INT) AS Ref;

---------------------------------------------------------------------------------
/*Cree una vista llamada dbo.vw_AtencionesFiltradas sobre la tabla Atenciones_Medicas.
La vista debe seleccionar todas las columnas, pero aplicar un filtro estricto: 
solo debe mostrar los registros cuyo Estado sea exactamente 'Completada'.

Además, agregue la cláusula estructural necesaria para garantizar que ningún usuario pueda modificar 
el estado de una fila a través de la vista si esa modificación provoca que la fila desaparezca del filtro.

Ejecute el siguiente UPDATE para probar su vista:
*/

GO
CREATE VIEW dbo.vw_AtencionesFiltradas
AS
SELECT * FROM Atenciones_Medicas
WHERE Estado = 'Completada'
WITH CHECK OPTION;
GO

UPDATE dbo.vw_AtencionesFiltradas
SET Estado = 'Cancelada'
WHERE AtencionID = 101;

/*Mens. 550, Nivel 16, Estado 1, Línea 79
Error en la inserción o actualización debido a que la 
vista de destino especifica WITH CHECK OPTION o alcanza una vista con esta opción, 
y una o más filas resultantes de la operación no se califican con la restricción CHECK OPTION.
Se terminó la instrucción.
Hora de finalización: 2026-06-02T19:13:48.0153446-05:00*/

-----------------------------------------------------------------------------------------------------

/*3.Desarrolle un procedimiento almacenado llamado dbo.sp_InscribirAtencion. 
Este objeto debe recibir obligatoriamente los parámetros: 
@Id INT, @PacId INT, @Fecha DATE, @Costo DECIMAL(10,2), @Est VARCHAR(20) 
e insertar esos valores en la tabla Atenciones_Medicas.

Si @Costo es menor a 0, el procedimiento debe lanzar un error intencional (RAISERROR o THROW).
Todo el bloque de inserción debe estar protegido de forma estricta por una estructura de control de excepciones TRY...CATCH. 

Asegure la Atomicidad (ACID): si ocurre cualquier error en el tiempo de ejecución, 
el bloque CATCH debe revertir por completo los cambios realizados utilizando ROLLBACK TRANSACTION. 
Si todo es exitoso, confirme con COMMIT TRANSACTION.
Luego de compilar el procedimiento de forma exitosa, ejecute secuencialmente el siguiente código:

EXEC dbo.sp_InscribirAtencion 107, 2, '2026-06-02', 30.00, 'Completada';

EXEC dbo.sp_InscribirAtencion 108, 1, '2026-06-02', -10.00, 'Completada';

EXEC dbo.sp_InscribirAtencion 109, 3, '2026-06-02', 25.00, 'Completada';

SELECT COUNT(*) AS TotalMonitoreo FROM Atenciones_Medicas;*/

SELECT * FROM Atenciones_Medicas
GO
CREATE PROCEDURE dbo.sp_InscribirAtencion
    @Id INT, @PacId INT, @Fecha DATE, @Costo DECIMAL(10,2), @Est VARCHAR(20) 
AS
BEGIN
    BEGIN TRY
        BEGIN TRANSACTION;
        IF @Costo<0
        BEGIN 
            RAISERROR('COSTO NO DEBE SER NEGATIVO',16,1);
        END
        INSERT INTO Atenciones_Medicas (AtencionID,PacienteID,FechaAtencion,CostoConsulta,Estado)
        VALUES (@Id, @PacId, @Fecha, @Costo, @Est);
        COMMIT TRANSACTION;
    END TRY
    BEGIN CATCH 
        ROLLBACK TRANSACTION;
      
    END CATCH
END

EXEC dbo.sp_InscribirAtencion 107, 2, '2026-06-02', 30.00, 'Completada';

EXEC dbo.sp_InscribirAtencion 108, 1, '2026-06-02', -10.00, 'Completada';

EXEC dbo.sp_InscribirAtencion 109, 3, '2026-06-02', 25.00, 'Completada';

SELECT COUNT(*) AS TotalMonitoreo FROM Atenciones_Medicas;

-----------------------RESULTADO 8-------------------------------------------
-----------------------------------------------------------------------------
/*Desarrolle un disparador (TRIGGER) llamado dbo.tr_PrevenirBajas asociado a la tabla Pacientes que actúe de tipo AFTER DELETE.
El disparador debe interceptar el borrado y evaluar si el o los pacientes eliminados 
(inspeccionando de forma nativa la tabla lógica temporal deleted) cuentan con registros
históricos de citas en la tabla Atenciones_Medicas. 
Si se detecta que al menos uno tiene historial, el trigger debe abortar la operación de raíz ejecutando un ROLLBACK TRANSACTION.

Luego de activar el trigger, ejecute lo siguiente:
BEGIN TRY
    DELETE FROM Pacientes WHERE PacienteID = 1;
END TRY
BEGIN CATCH
    END CATCH;

SELECT COUNT(*) AS ControlTriggers FROM Pacientes;*/
GO
CREATE TRIGGER dbo.tr_PrevenirBajas ON Pacientes
AFTER DELETE AS 
BEGIN
    IF EXISTS (SELECT 1 FROM deleted d
                JOIN Atenciones_Medicas a ON d.PacienteID = a.PacienteID)
    BEGIN
        ROLLBACK TRANSACTION;
    END
END
GO

BEGIN TRY
    DELETE FROM Pacientes WHERE PacienteID = 1;
END TRY
BEGIN CATCH
    END CATCH;

SELECT COUNT(*) AS ControlTriggers FROM Pacientes; --3--

------------------------------------------------------------------------------------
/*La administración de la clínica exige automatizar una regla de consistencia financiera directamente en 
la estructura de la tabla Atenciones_Medicas mediante una restricción de verificación (CHECK CONSTRAINT) llamada CK_LogicaFinanciera.

Si el Estado de la atención es 'Cancelada', el CostoConsulta obligatoriamente debe ser igual a 0.
Si el Estado de la atención es 'Completada' o 'Pendiente', el CostoConsulta estrictamente debe ser mayor a 0.

Al intentar aplicar la restricción directamente con un ALTER TABLE, 
el motor de SQL Server generará un error. Usted debe resolver este conflicto de forma lógica 
y una vez corregido ejecute el siguiente bloque de pruebas:

BEGIN TRY
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (110, 2, '2026-06-02', 0.00, 'Cancelada');
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (111, 1, '2026-06-02', 0.00, 'Completada');
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (112, 3, '2026-06-02', 35.00, 'Pendiente');
    PRINT 'ÉXITO TOTAL';
END TRY
BEGIN CATCH
    PRINT 'VIOLACIÓN DETECTADA: ' + ERROR_MESSAGE();
END CATCH;

SELECT COUNT(*) AS ControlCheck FROM Atenciones_Medicas WHERE AtencionID >= 110;*/
GO
ALTER TABLE Atenciones_Medicas
ADD CONSTRAINT CK_LogicaFinanciera
CHECK ((CostoConsulta= 0 AND Estado ='Cancelada') OR
        (CostoConsulta>0 AND (Estado ='Completada' OR Estado = 'Pendiente')))
GO


BEGIN TRY
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (110, 2, '2026-06-02', 0.00, 'Cancelada');
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (111, 1, '2026-06-02', 0.00, 'Completada');
    INSERT INTO Atenciones_Medicas (AtencionID, PacienteID, FechaAtencion, CostoConsulta, Estado)
    VALUES (112, 3, '2026-06-02', 35.00, 'Pendiente');
    PRINT 'ÉXITO TOTAL';
END TRY
BEGIN CATCH
    PRINT 'VIOLACIÓN DETECTADA: ' + ERROR_MESSAGE();
END CATCH;

SELECT COUNT(*) AS ControlCheck FROM Atenciones_Medicas WHERE AtencionID >= 110;--3--

---------------------------------------------------------------------------------------------------------
/*
Usted debe simular un escenario real de administración y recuperación de fallas en su servidor local utilizando la base de datos ClinicaDB. 
Siga estrictamente la siguiente secuencia cronológica de pasos en su archivo SQL:

1.    Asegure el modelo de recuperación ejecutando:*/

ALTER DATABASE ClinicaDB SET RECOVERY FULL;
--2.    Cree un directorio en su disco local (por ejemplo C:\Backup\) y genere un Respaldo Completo inicial limpiando contenedores previos.
BACKUP DATABASE ClinicaDB
TO DISK = 'C:\Backups\ClinicaDB_Full.bak'
WITH FORMAT, MEDIANAME = 'FullClinicaDB', NAME = 'Full Backup de ClinicaDB';
GO
--3.    Inserte un nuevo paciente para simular la operación:
INSERT INTO Pacientes (PacienteID, Nombre, FechaNacimiento) VALUES (50, 'Estudiante Evaluado', '2000-01-01');
--4.    Genere un Respaldo Diferencial que capture este último cambio.
BACKUP DATABASE ClinicaDB
TO DISK = 'C:\Backups\ClinicaDB_Diff.bak'
WITH DIFFERENTIAL, NAME = 'Diferencial ClinicaDB Estudiante Evaluado';
GO

--5.    Ejecute este borrado masivo accidental:
DELETE FROM Atenciones_Medicas;
/*6.    Levantar la base de datos desde la base master utilizando la secuencia de comandos RESTORE correcta. 
Debe recuperar el sistema hasta el punto exacto del Paso 4 (recuperando al paciente 50 y salvando 
las atenciones médicas originales del borrado del Paso 5)*/

USE master

RESTORE DATABASE ClinicaDB
FROM DISK = 'C:\Backups\ClinicaDB_Full.bak'
WITH NORECOVERY, REPLACE;
GO

--SCRIPT: Restaurar el Backup DIFERENCIAL (Trae los datos del mediod�a)
RESTORE DATABASE ClinicaDB
FROM DISK = 'C:\Backups\ClinicaDB_Diff.bak'
WITH RECOVERY;
GO


--Una vez que la base de datos sea declarada nuevamente en línea y funcional, ejecute la siguiente consulta de validación:

SELECT (SELECT COUNT(*) FROM Pacientes) + (SELECT COUNT(*) FROM Atenciones_Medicas) AS SumaControl;



