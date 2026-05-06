--vENTANA1

SET DEADLOCK_PRIORITY HIGH;
BEGIN TRANSACTION;
UPDATE Usuarios
SET Nombre = 'Lenin'
WHERE id_usuario = 1;

UPDATE Contenido set titulo = 'Minions'
WHERE id_contenido = 1;

SELECT * FROM Contenido