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

