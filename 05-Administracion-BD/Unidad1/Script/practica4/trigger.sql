-- Trigger
CREATE TRIGGER trg_alerta_consumo
ON Historial_Visualizacion
AFTER INSERT
AS
BEGIN 
    INSERT INTO Alertas_Consumo (mensaje)
    SELECT
      'El usuario ' + cast(id_usuario as varchar(50)) + ' supero el limite de visusalizaciones'
    FROM inserted
    WHERE minutos_vistos > 300
END
GO

INSERT INTO Historial_Visualizacion (id_usuario, id_contenido, minutos_vistos)
VALUES (1, 1, 350)
INSERT INTO Historial_Visualizacion (id_usuario, id_contenido, minutos_vistos)
VALUES (2, 2, 250)
INSERT INTO Historial_Visualizacion (id_usuario, id_contenido, minutos_vistos)
VALUES (3, 3, 400)
SELECT * FROM Historial_Visualizacion
select * from Alertas_Consumo

---trigger2
CREATE TRIGGER trg_cambio_suscipcion
ON Usuarios
AFTER UPDATE
AS
BEGIN 
    INSERT INTO Alertas_Consumo (mensaje)
    SELECT
      'El usuario ' + nombre + ' cambio su tipo de suscripcion a '
    FROM inserted
    WHERE suscripcion = 'Premium'
END

UPDATE Usuarios
SET suscripcion = 'Premium'
WHERE id_usuario = 1  

SELECT * FROM Usuarios
SELECT * FROM Alertas_Consumo

--trigger3
CREATE TRIGGER trg_bloquear_eliminacion
ON Contenido
INSTEAD OF DELETE
AS
BEGIN 
    IF EXISTS (
        SELECT * FROM deleted d
        JOIN Historial_Visualizacion h 
        ON d.id_contenido = h.id_contenido
        )
        BEGIN
            PRINT('No se pueden eliminar contenidos')
        END
    ELSE
        BEGIN
            DELETE FROM Contenido
            WHERE id_contenido IN (
                SELECT id_contenido FROM deleted)
        END
END

DELETE FROM Contenido
WHERE id_contenido = 5

INSERT INTO Contenido (
    titulo, tipo, duracion_total_min, es_estreno)
VALUES ('Blanca Nieves', 'Pelicula', 120,0)

select * from Contenido