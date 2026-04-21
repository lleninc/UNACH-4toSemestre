Use Vuelos
GO
EXEC sp_helpindex 'Vuelos'; -- sp_helpindex muestra los índices existentes en la tabla Vuelos, incluyendo el índice clustered (PK_Vuelos) y cualquier índice no clustered que se haya creado.

CREATE NONCLUSTERED INDEX IX_Vuelos_Destino -- Crea un índice no clustered en la columna destino de la tabla Vuelos para mejorar el rendimiento de las consultas que filtran por destino.
ON Vuelos(destino);

SELECT *
FROM Vuelos
WHERE destino = 'Quito';

-- La consulta SIGUIENTE utiliza el índice IX_Vuelos_Destino para 
-- filtrar los vuelos con destino a Galápagos, lo que mejora el rendimiento 
--de la consulta al evitar un escaneo completo de la tabla.

SELECT * FROM Vuelos WITH (INDEX(IX_Vuelos_Destino)) WHERE destino =
'Galápagos'; 


--USO DE JOIN
SELECT V.destino, 
R.pasajero_nombre
FROM Vuelos V
FULL JOIN Reservas R ON V.vuelo_id = R.vuelo_id; --FULL JOIN muestra todos los registros de ambas tablas, incluso si no hay coincidencias. Si no hay coincidencia, los campos de la tabla sin coincidencia se llenarán con NULL.
INNER JOIN -- muestra solo los registros que tienen coincidencias en ambas tablas. 
            -- Si no hay coincidencia, el registro no se incluirá en el resultado.
LEFT JOIN -- muestra todos los registros de la tabla de la izquierda (Vuelos) y 
          --los registros coincidentes de la tabla de la derecha (Reservas). Si no hay coincidencia, los campos de la tabla de la derecha se llenarán con NULL.
RIGHT JOIN -- muestra todos los registros de la tabla de la derecha (Reservas) y los registros coincidentes de la tabla de la izquierda (Vuelos). Si no hay coincidencia, los campos de la tabla de la izquierda se llenarán con NULL.

--COMMON TABLE EXPRESSIONS (CTE)

SELECT destino FROM Vuelos
WHERE precio > (SELECT AVG(precio) FROM Vuelos);
-- La consulta anterior es equivalente a la siguiente consulta utilizando CTE:

WITH PromedioPrecios AS ( -- CTE para calcular el precio medio de los vuelos
SELECT AVG(precio) as precio_medio FROM Vuelos
)
SELECT V.destino, V.precio
FROM Vuelos V, PromedioPrecios P
WHERE V.precio > P.precio_medio;

-- SUM, COUNT, AVG, MIN, MAX
SELECT COUNT(*) AS TotalVuelos FROM Vuelos; -- Cuenta el número total de vuelos
SELECT SUM(precio) AS SumaPrecios FROM Vuelos; -- Suma el precio de todos los vuelos
SELECT AVG(precio) AS PrecioPromedio FROM Vuelos; -- Calcula el precio promedio de los vuelos
SELECT MIN(precio) AS PrecioMinimo FROM Vuelos; -- Encuentra el precio mínimo de los vuelos
SELECT MAX(precio) AS PrecioMaximo FROM Vuelos; -- Encuentra el precio máximo de los vuelos
SELECT destino, COUNT(*) AS TotalVuelos FROM Vuelos
GROUP BY destino; -- Agrupa los vuelos por destino y cuenta el número de vuelos para cada destino

SELECT
destino,
precio,
RANK() OVER (ORDER BY precio DESC) as ranking_precio,
SUM(precio) OVER () as total_ingresos_empresa --over() sin partición calcula el total de ingresos de la empresa
FROM Vuelos;



