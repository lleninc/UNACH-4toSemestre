-- procedimiento para insertar una nueva película y generar una alerta si es un estreno
CREATE PROCEDURE sp_RegistrarPeliculas
    @titulo VARCHAR(150),
    @tipo VARCHAR(20),
    @duracion INT,
    @es_estreno BIT
AS
BEGIN
    -- Insertar el nuevo contenido
    INSERT INTO Contenido (titulo, tipo, duracion_total_min, es_estreno)
    VALUES (@titulo, @tipo, @duracion, @es_estreno);
    
    -- Si es un estreno, generar una alerta
    IF @es_estreno = 1
    BEGIN
        INSERT INTO Alertas_Consumo (mensaje)
        VALUES ('Nuevo estreno disponible: ' + @titulo+' ya esta en la plataforma!');
    END
END;

select * from Contenido;
select * from Alertas_Consumo;

-- Ejecutar el procedimiento para agregar una nueva película
EXEC sp_RegistrarPeliculas 'Titanic', 'Película', 110, 1;

--tambien puede 


