BEGIN TRANSACTION;
UPDATE Vuelos SET asientos_disponibles = 2 WHERE vuelo_id = 101;
COMMIT;
ROLLBACK;


INSERT INTO Vuelos VALUES (103, 'Miami', 3, 200.00);

SELECT * FROM Vuelos; -- Este SELECT mostrará que el vuelo 103 no se ha insertado debido al ROLLBACK.

UPDATE Vuelos SET precio = 350.00 WHERE vuelo_id = 103;

INSERT INTO Vuelos VALUES (104, 'Cuenca', 20, 50.00);