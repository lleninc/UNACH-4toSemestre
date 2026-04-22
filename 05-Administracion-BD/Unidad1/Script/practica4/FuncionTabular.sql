-- funcion tabla que muestre todo lo que un usuario ha visto
CREATE FUNCTION fn_historial_usuario (@usuario INT)
RETURNS TABLE
AS
RETURN
(
    SELECT 
       C.titulo,
       H.minutos_vistos,
       H.fecha_vista
    FROM 
        Historial_Visualizacion H
    JOIN 
        Contenido C ON H.id_contenido = C.id_contenido
    WHERE 
        H.id_usuario = @usuario
);

select * from dbo.fn_historial_usuario(2);

select * from historial_visualizacion;

-- funcion tabular para ver disponibilidad de contenido
CREATE FUNCTION fn_tipo_contenido (@tipo VARCHAR(30))
RETURNS TABLE
AS
RETURN
(
    SELECT 
       titulo,
       es_estreno
    FROM 
        Contenido 
    WHERE 
        tipo = @tipo
);

select * from dbo.fn_tipo_contenido('Película');
SELECT * FROM DBO.fn_tipo_contenido('Serie');