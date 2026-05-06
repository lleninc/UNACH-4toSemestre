--ventana2
BEGIN TRANSACTION;
update contenido
set titulo = 'El Gran Escape'
where id_contenido = 1;


update Usuarios set Nombre = 'Lenin Castro'
where id_usuario = 1;