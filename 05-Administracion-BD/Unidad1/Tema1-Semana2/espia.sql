SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM Vuelos WHERE vuelo_id = 101;

-- este script muestra como una transaccion puede leer 
-- datos no confirmados (dirty read)   
-- En este caso, la transacción intenta leer 
-- el número de asientos disponibles después de que
-- otra transacción ha actualizado ese valor pero 
-- aún no ha confirmado la transacción.   


SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SELECT * FROM Vuelos WHERE vuelo_id = 101;

-- este script muestra como una transaccion puede leer  
-- datos confirmados (read committed)
-- En este caso, la transacción intenta leer    
-- el número de asientos disponibles después de que se 
-- actualizó ese valor pero aún no se ha confirmado la transacción. 

SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;

SELECT * FROM Vuelos WHERE vuelo_id= 103;
COMMIT;

-- este script muestra como una transaccion puede leer  
-- datos confirmados y bloquea las filas leídas (repeatable read)
-- En este caso, la transacción intenta leer
-- el número de asientos disponibles después de que se actualizó ese valor pero aún no se
-- ha confirmado la transacción. Además, bloquea la fila para
-- evitar que otras transacciones modifiquen ese valor 
--hasta que se confirme o se cancele la transacción actual.


SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRANSACTION;

SELECT * FROM Vuelos WHERE precio < 100;
COMMIT;
-- este script muestra como una transaccion puede leer  
-- datos confirmados y bloquea un rango de filas (serializable) 
-- En este caso, la transacción intenta leer
-- los vuelos con precio menor a 100 después de que se actualizó ese valor pero aún no se ha confirmado la transacción. Además, bloquea el rango de filas que cumplen esa condición para evitar que otras transacciones modifiquen esos valores 
-- hasta que se confirme o se cancele la transacción actual.
