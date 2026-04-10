# 05-Administracion-BD - U1 T1 S2

## Objetivo de la semana
Analizar cómo se controla la concurrencia en bases de datos mediante bloqueos y niveles de aislamiento, y aplicar índices y sentencias avanzadas para optimizar consultas.

## Notas de clase

### 1.3 Control de bloqueos y niveles de aislamiento
El control de bloqueos permite coordinar accesos concurrentes para evitar inconsistencias.

Tipos de bloqueo:
- Compartido (S): permite lectura concurrente.
- Exclusivo (X): permite escritura por una sola transacción mientras otras esperan.

También se maneja granularidad de bloqueo (fila, página o tabla): a menor granularidad, mayor concurrencia.

Niveles de aislamiento SQL:
- Read Uncommitted: permite leer datos no confirmados.
- Read Committed: evita lecturas sucias, pero puede tener lecturas no repetibles.
- Repeatable Read: mantiene consistencia en lecturas repetidas, con posibles anomalías de inserción.
- Serializable: nivel más estricto, equivalente a ejecución secuencial.

La elección del nivel de aislamiento depende del equilibrio entre rendimiento y seguridad de los datos.

### 1.4 Índices y sentencias avanzadas
Un índice es una estructura auxiliar que acelera búsquedas, JOIN, ORDER BY y GROUP BY. Mejora lectura de datos, pero añade costo en INSERT, UPDATE y DELETE.

Tipos principales:
- Índice agrupado (clustered): define el orden físico de la tabla; solo puede haber uno.
- Índice no agrupado (non-clustered): estructura separada con claves y punteros; puede haber varios.

Sentencias avanzadas importantes:
- JOIN: combina información entre tablas relacionadas (INNER, LEFT, RIGHT, FULL).
- Subconsultas: consultas anidadas en WHERE, FROM o SELECT.
- CTE (WITH): mejora legibilidad y reutilización en consultas complejas.
- Consultas recursivas: útiles para jerarquías (organigramas, árboles, rutas).
- Funciones de agregación y ventana: SUM, AVG, COUNT y funciones OVER para análisis sin perder detalle fila a fila.

## Resumen para estudiar
1. Bloqueos y aislamiento protegen la consistencia cuando hay concurrencia.
2. Serializable ofrece máxima seguridad, pero con mayor costo.
3. Los índices aceleran consultas, pero deben diseñarse con criterio.
4. JOIN y subconsultas resuelven consultas multi-tabla de forma flexible.
5. CTE, recursividad y funciones de ventana fortalecen análisis avanzado en SQL.

## Resumen de PRÁCTICA GUIADA 1
La práctica trabaja sobre una base de datos de vuelos y reservas para mostrar cómo la transaccionalidad protege la integridad de los datos.

### Bloque 1: Crear Base de Datos y Registros
```sql
-- Crear base de datos si no existe
IF DB_ID('Vuelos') IS NULL
BEGIN
    CREATE DATABASE Vuelos;
END;
GO

USE Vuelos;
GO

-- Crear Tablas Base
CREATE TABLE Vuelos (
    vuelo_id INT PRIMARY KEY,
    destino VARCHAR(50),
    asientos_disponibles INT,
    precio DECIMAL(10,2)
);

CREATE TABLE Reservas (
    reserva_id INT IDENTITY(1,1) PRIMARY KEY,
    vuelo_id INT,
    pasajero_nombre VARCHAR(100),
    fecha_reserva DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (vuelo_id) REFERENCES Vuelos(vuelo_id)
);

-- Insertar datos de prueba
INSERT INTO Vuelos VALUES (101, 'Galápagos', 2, 150.00), (102, 'Quito', 15, 60.00);
```

### Bloque 2: Transacciones y Propiedades ACID
```sql
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
```

### Bloque 3 y 4: Bloqueos y Niveles de Aislamiento
**Simulación de bloqueos** para demostrar cómo el motor protege la integridad:
- Una actualización abierta impide lecturas o cambios conflictivos hasta cerrar la transacción.
- Se comparan `READ UNCOMMITTED`, `READ COMMITTED`, `REPEATABLE READ` y `SERIALIZABLE`.
- Ejemplo con REPEATABLE READ:
```sql
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRANSACTION;
SELECT * FROM Vuelos WHERE vuelo_id = 103;
```

## Resumen de PRÁCTICA GUIADA 2
La práctica se enfoca en índices y consultas avanzadas usando el mismo escenario de vuelos.

### Bloque 1: Manejo de Índices
```sql
Use Vuelos
GO
EXEC sp_helpindex 'Vuelos'; -- sp_helpindex muestra los índices existentes en la tabla

CREATE NONCLUSTERED INDEX IX_Vuelos_Destino -- Crea un índice no clustered en la columna destino
ON Vuelos(destino);

SELECT *
FROM Vuelos
WHERE destino = 'Quito';

-- La consulta siguiente utiliza el índice IX_Vuelos_Destino para filtrar
SELECT * FROM Vuelos WITH (INDEX(IX_Vuelos_Destino)) WHERE destino = 'Galápagos'; 
```

### Bloque 2: Manejo de Joins
```sql
-- USO DE JOIN
SELECT V.destino, R.pasajero_nombre
FROM Vuelos V
FULL JOIN Reservas R ON V.vuelo_id = R.vuelo_id; 
-- FULL JOIN: muestra todos los registros de ambas tablas
-- INNER JOIN: solo registros con coincidencias en ambas tablas
-- LEFT JOIN: todos los de la izquierda + coincidencias de la derecha
-- RIGHT JOIN: todos los de la derecha + coincidencias de la izquierda
```

### Bloque 3: Common Table Expressions (CTE) y Subconsultas
```sql
-- Subconsulta (forma desordenada)
SELECT destino FROM Vuelos
WHERE precio > (SELECT AVG(precio) FROM Vuelos);

-- CTE (forma profesional)
WITH PromedioPrecios AS ( -- CTE para calcular el precio medio
SELECT AVG(precio) as precio_medio FROM Vuelos
)
SELECT V.destino, V.precio
FROM Vuelos V, PromedioPrecios P
WHERE V.precio > P.precio_medio;
```

### Bloque 4: Funciones de Agregación y Ventana
```sql
-- SUM, COUNT, AVG, MIN, MAX
SELECT COUNT(*) AS TotalVuelos FROM Vuelos; -- Cuenta el número total
SELECT SUM(precio) AS SumaPrecios FROM Vuelos; -- Suma precios
SELECT AVG(precio) AS PrecioPromedio FROM Vuelos; -- Promedio
SELECT MIN(precio) AS PrecioMinimo FROM Vuelos; -- Mínimo
SELECT MAX(precio) AS PrecioMaximo FROM Vuelos; -- Máximo
SELECT destino, COUNT(*) AS TotalVuelos FROM Vuelos
GROUP BY destino; -- Agrupa por destino

-- Funciones de ventana
SELECT
    destino,
    precio,
    RANK() OVER (ORDER BY precio DESC) as ranking_precio,
    SUM(precio) OVER () as total_ingresos_empresa
FROM Vuelos;
```

## Preguntas rápidas
1. ¿Qué diferencia hay entre bloqueo compartido y exclusivo?
2. ¿Qué riesgo evita el nivel Read Committed?
3. ¿Cuándo conviene usar un índice clustered?
4. ¿Qué ventaja ofrece una CTE frente a subconsultas anidadas?
5. ¿Para qué sirven las funciones de ventana en reportes?

## Quiz

### Pregunta 1: Inconveniente de demasiados índices

**Pregunta:** ¿Cuál es un posible inconveniente de usar demasiados índices?

**Opciones:**
- ❌ Eliminan las claves primarias.
- ✅ Ralentizan operaciones de inserción y actualización.
- ❌ Impiden consultas con filtros.

**Respuesta correcta:** Ralentizan operaciones de inserción y actualización.

**Explicación breve:**
Cada cambio en los datos también debe actualizar los índices asociados; por eso, un exceso de índices puede degradar el rendimiento de escritura.

### Pregunta 2: Concepto de bloqueo

**Pregunta:** ¿Qué es un bloqueo en bases de datos?

**Opciones:**
- ❌ Un error en la ejecución de una consulta.
- ✅ Un mecanismo para coordinar el acceso concurrente y evitar inconsistencias.
- ❌ Un índice creado para optimizar consultas.

**Respuesta correcta:** Un mecanismo para coordinar el acceso concurrente y evitar inconsistencias.

**Explicación breve:**
Los bloqueos controlan cómo múltiples transacciones acceden a los mismos datos para evitar conflictos y mantener la consistencia.

### Pregunta 3: Problema que evitan los bloqueos

**Pregunta:** ¿Qué problema evita el uso de bloqueos en bases de datos?

**Opciones:**
- ❌ Reducción de almacenamiento.
- ❌ Creación automática de índices.
- ✅ Actualizaciones perdidas.

**Respuesta correcta:** Actualizaciones perdidas.

**Explicación breve:**
Los bloqueos evitan que dos transacciones modifiquen el mismo dato al mismo tiempo y sobrescriban cambios, lo que previene pérdidas de actualización.

### Pregunta 4: Definición de índice

**Pregunta:** ¿Qué es un índice en bases de datos?

**Opciones:**
- ❌ Una restricción que impide valores duplicados.
- ❌ Una tabla que almacena transacciones temporales.
- ✅ Una estructura que acelera búsquedas y consultas.

**Respuesta correcta:** Una estructura que acelera búsquedas y consultas.

**Explicación breve:**
Un índice es una estructura auxiliar que mejora el rendimiento de lectura en consultas y búsquedas sobre columnas específicas.

### Pregunta 5: Nivel Serializable

**Pregunta:** El nivel Serializable garantiza:

**Opciones:**
- ✅ Que las transacciones se comporten como si se ejecutaran secuencialmente.
- ❌ La eliminación inmediata de bloqueos al finalizar una consulta.
- ❌ La creación automática de vistas materializadas.

**Respuesta correcta:** Que las transacciones se comporten como si se ejecutaran secuencialmente.

**Explicación breve:**
Serializable es el nivel de aislamiento más estricto y evita anomalías de concurrencia al forzar un comportamiento equivalente a ejecución en serie.

## Actividades
- [ ] Comparar los cuatro niveles de aislamiento con un ejemplo.
- [ ] Proponer en qué columnas crearías índices para una tabla de pedidos.
- [ ] Escribir una consulta con JOIN y otra con función de ventana.

## Quiz

### Pregunta 1: Índices excesivos

**Pregunta:** ¿Cuál es un posible inconveniente de usar demasiados índices?

**Opciones:**
- ❌ Eliminan las claves primarias.
- ✅ Ralentizan operaciones de inserción y actualización.
- ❌ Impiden consultas con filtros.

**Respuesta correcta:** Ralentizan operaciones de inserción y actualización.

**Explicación breve:**
Cada cambio en los datos también debe actualizar los índices asociados.

### Pregunta 2: Bloqueos

**Pregunta:** ¿Qué es un bloqueo en bases de datos?

**Opciones:**
- ❌ Un error en la ejecución de una consulta.
- ✅ Un mecanismo para coordinar el acceso concurrente y evitar inconsistencias.
- ❌ Un índice creado para optimizar consultas.

**Respuesta correcta:** Un mecanismo para coordinar el acceso concurrente y evitar inconsistencias.

**Explicación breve:**
Los bloqueos controlan cómo múltiples transacciones acceden a los mismos datos para evitar conflictos.

### Pregunta 3: Problema que evitan los bloqueos

**Pregunta:** ¿Qué problema evita el uso de bloqueos en bases de datos?

**Opciones:**
- ❌ Reducción de almacenamiento.
- ❌ Creación automática de índices.
- ✅ Actualizaciones perdidas.

**Respuesta correcta:** Actualizaciones perdidas.

**Explicación breve:**
Los bloqueos evitan que dos transacciones sobrescriban el mismo dato al mismo tiempo.

### Pregunta 4: CTE

**Pregunta:** ¿Qué ventaja ofrece una CTE frente a una subconsulta anidada?

**Opciones:**
- ❌ Hace que la consulta sea más difícil de leer.
- ✅ Mejora la legibilidad y reutilización de la lógica.
- ❌ Elimina la necesidad de usar SELECT.

**Respuesta correcta:** Mejora la legibilidad y reutilización de la lógica.

**Explicación breve:**
Una CTE permite organizar mejor consultas complejas y reutilizar resultados intermedios.

### Pregunta 5: Serializable

**Pregunta:** El nivel Serializable garantiza:

**Opciones:**
- ✅ Que las transacciones se comporten como si se ejecutaran secuencialmente.
- ❌ La eliminación inmediata de bloqueos al finalizar una consulta.
- ❌ La creación automática de vistas materializadas.

**Respuesta correcta:** Que las transacciones se comporten como si se ejecutaran secuencialmente.

**Explicación breve:**
Serializable es el nivel de aislamiento más estricto y evita anomalías de concurrencia.

