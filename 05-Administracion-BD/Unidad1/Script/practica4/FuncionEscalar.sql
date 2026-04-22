use Peliculas;

-- funcion escalar para calcular el porcentaje de contenido visto por un usuario
CREATE FUNCTION fn_porcentaje_visualizacion (@vistos INT,@total INT)
RETURNS DECIMAL(5,2)
AS
BEGIN
    IF @total = 0 or @total IS NULL
        RETURN 0;
    RETURN (CAST(@vistos as DECIMAL) / @total) * 100;
END

--prueba de la función con un ejemplo
SELECT dbo.fn_porcentaje_visualizacion (30,100) AS Porcentaje_Visto;

--contenidos y visualizaciones para calcular el porcentaje de visualización real
SELECT 
u.nombre as Usuario,
C.titulo as Pelicula,
H.minutos_vistos,
C.duracion_total_min,
dbo.fn_porcentaje_visualizacion(H.minutos_vistos, C.duracion_total_min) AS Porcentaje_Visto
FROM Historial_Visualizacion H
JOIN Usuarios U ON H.id_usuario = U.id_usuario
JOIN Contenido C ON H.id_contenido = C.id_contenido;

