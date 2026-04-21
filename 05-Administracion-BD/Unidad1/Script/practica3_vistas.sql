

-- Agregar registros BD Vuelos
INSERT INTO Vuelos (vuelo_id, destino, asientos_disponibles, precio)
VALUES 
(103, 'Cuenca', 20, 45.00),
(104, 'Manta', 5, 85.00),
(105, 'Guayaquil', 0, 55.00), -- Vuelo lleno para probar filtros
(106, 'Coca', 10, 120.00);


-- Agregamos varias reservas para diferentes vuelos
-- Nota: Asegúrate de que los vuelo_id existan en la tabla Vuelos
INSERT INTO Reservas (vuelo_id, pasajero_nombre)
VALUES 
(101, 'Ana García'),     -- Galápagos
(101, 'Luis Pérez'),      -- Galápagos (aquí se acabarán los cupos)
(102, 'María López'),     -- Quito
(103, 'Carlos Ruiz'),     -- Cuenca
(103, 'Diana Soler'),     -- Cuenca
(104, 'Elena Vera'),      -- Manta
(106, 'Roberto Gómez');   -- Coca

CREATE VIEW Vista_Disponibilidad_vuelos AS
SELECT 
destino AS [Destino del VIaje],
asientos_disponibles AS [CUpos Libre],
precio AS [Costo Vuelo]
FROM Vuelos

-- Consulta la vista para mostrar la disponibilidad de vuelos, incluyendo el destino, los asientos disponibles y el costo del vuelo. 

SELECT * FROM Vista_Disponibilidad_vuelos; 


---VISTAS ACTUALIZABLES
-- La siguiente vista es actualizable porque se basa en una sola tabla (Vuelos) y no incluye funciones de agregación, GROUP BY, ni JOINs.
CREATE VIEW Vista_Actualizable_Precios AS
SELECT vuelo_id, destino, precio
FROM Vuelos;
-- Puedes actualizar el precio de un vuelo a través de la vista, lo que también actualizará el precio en la tabla Vuelos.
UPDATE Vista_Actualizable_Precios
SET precio = 99.00
WHERE vuelo_id = 103; -- Esto actualizará el precio del vuelo con ID 103 en la tabla Vuelos a 60.00 

select * from Vuelos where vuelo_id = 103; -- Verifica que el precio se haya actualizado correctamente en la tabla Vuelos.

--VISTA DE INSERCIÓN
CREATE VIEW Vista_Insertar_destinos1 AS
SELECT vuelo_id, precio 
FROM Vuelos

INSERT INTO Vista_Insertar_destinos1 
(vuelo_id, destino, precio)
VALUES 
(107, 'Baños', 15.00); 

CREATE VIEW Vista_Eliminacion_Vuelos AS
SELECT * FROM Vuelos
WHERE precio < 50;

DELETE FROM Vista_Eliminacion_Vuelos -- Esto eliminará todos los vuelos con un precio inferior a 50 de la tabla Vuelos, ya que la vista se basa en la tabla Vuelos y permite la eliminación de registros que cumplen con la condición especificada en la vista.
where precio < 50; -- Asegúrate de que la condición en la cláusula WHERE coincida con la condición definida en la vista para eliminar los registros correctos.

