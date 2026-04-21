BEGIN TRANSACTION;
BEGIN TRY
    -- Intentamos restar el asiento
    UPDATE Vuelos SET asientos_disponibles = asientos_disponibles - 1 WHERE vuelo_id = 101;

    -- Si los asientos son menores a 0, forzamos un error
    IF (SELECT asientos_disponibles FROM Vuelos WHERE vuelo_id = 101) < 0
        THROW 50000, 'Error: No hay más asientos.', 1;

    COMMIT; -- Si todo está bien, guardamos
    PRINT 'Reserva exitosa';
END TRY
BEGIN CATCH
    ROLLBACK; -- Si algo falló (como el THROW), deshacemos todo
    PRINT 'Transacción cancelada: ' + ERROR_MESSAGE();
END CATCH;