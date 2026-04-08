-- RESERVA DE VUELO CON CONTROL DE ERRORES 
BEGIN TRANSACTION; -- Iniciar una transacción para asegurar la atomicidad de las operaciones

BEGIN TRY   -- Intentar realizar la reserva
    -- Intentar reservar un vuelo
    INSERT INTO Reservas (vuelo_id, pasajero_nombre) 
    VALUES (101, 'Lenin Lopez');

    UPDATE Vuelos
    SET asientos_disponibles = asientos_disponibles - 1
    WHERE vuelo_id = 101;   

    IF (SELECT asientos_disponibles FROM Vuelos WHERE vuelo_id = 101) < 0
        -- Si no hay asientos disponibles, se lanza un error personalizado  
        THROW 50000, 'No hay asientos disponibles', 1; 

    COMMIT; -- Si todo va bien, se confirma la transacción
    PRINT 'Reserva realizada con éxito';
END TRY -- Si ocurre un error, se captura y se revierte la transacción

BEGIN CATCH -- Capturar cualquier error que ocurra durante la transacción
ROLLBACK; -- Si ocurre un error, se revierte la transacción
PRINT 'Error al realizar la reserva: ' + ERROR_MESSAGE();
END CATCH;  -- Fin del bloque TRY-CATCH

-- Verificar resultados
SELECT * from Reservas WHERE vuelo_id = 101;
SELECT * from Vuelos; 

