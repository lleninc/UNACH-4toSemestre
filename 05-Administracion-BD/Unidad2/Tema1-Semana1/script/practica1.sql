ALTER TABLE Usuarios
ADD CONSTRAINT chk_suscripcion 
CHECK (Suscripcion IN ('Gratis', 'Premium', 'Estándar'));

INSERT INTO Usuarios (Nombre, Suscripcion) VALUES 
('Juan Pérez', 'VIP'),
('María Gómez', 'Premium'),
('Carlos López', 'Estándar');

delete from Usuarios where Nombre = 'Juan Pérez';


ALTER TABLE Contenido
ADD CONSTRAINT chk_duracion
CHECK (duracion_total_min > 0);

insert into Contenido (titulo, duracion_total_min,es_estreno) 
values ('Blanca nieves','Pelicula' -30);

select * from Usuarios;

---- VALIDAR SI EL CONTROL MULTIVERSION (MVCC) ESTÁ ACTIVADO EN LA BASE DE DATOS PELICULAS
BEGIN TRANSACTION
update Usuarios set suscripcion = 'Premium' where id_usuario = 6;
rollback;