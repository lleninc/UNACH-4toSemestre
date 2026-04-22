-- Procedimiento almacenado para modificar un plan de suscripción
CREATE PROCEDURE sp_cambiarplan
    @usuario INT,
    @nuevoplan VARCHAR(20)
AS
BEGIN
    UPDATE Usuarios
    SET suscripcion = @nuevoplan
    WHERE id_usuario = @usuario;
    PRINT 'Suscripción actualizada correctamente';
END;

EXEC sp_cambiarplan @usuario = 1, @nuevoplan = 'Premium';

select * from Usuarios;

-----
