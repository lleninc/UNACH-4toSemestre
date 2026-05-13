# 05-Administracion-BD - U2 T1 S1

## Notas de clase

## Tema 1. Fundamentos de recuperacion

### 1.1. Estrategias de consistencia

La consistencia garantiza que cada transaccion lleve la base de datos de un estado valido a otro estado valido, respetando reglas de integridad como claves primarias, foraneas, restricciones CHECK y reglas de negocio.

La consistencia forma parte del modelo ACID:

- Atomicidad: todo o nada.
- Consistencia: las reglas de integridad no se rompen.
- Aislamiento: las transacciones concurrentes no interfieren.
- Durabilidad: los cambios confirmados persisten aun con fallos.

Estrategias comunes para mantener consistencia:

- Disenar el esquema con restricciones claras de integridad.
- Aplicar validaciones automaticas en el SGBD (constraints y triggers).
- Disenar transacciones que respeten atomicidad y aislamiento.
- Evitar cambios parciales cuando ocurre un error (rollback).

Idea clave: la consistencia conecta la logica del negocio con la confiabilidad tecnica de la base de datos.

### 1.2. Control de concurrencia

El control de concurrencia es el conjunto de tecnicas para que varias transacciones simultaneas no produzcan inconsistencias.

Objetivo principal: preservar el aislamiento en ejecucion concurrente para que el resultado sea equivalente a una ejecucion en serie.

Metodos principales:

- Locking: bloqueos compartidos para lectura y exclusivos para escritura.
- Timestamp ordering: orden logico por marcas de tiempo.
- MVCC: multiples versiones para lecturas consistentes mientras otras transacciones escriben.
- Deteccion y prevencion de deadlocks.

Anomalias clasicas de concurrencia:

- Lectura sucia (dirty read): leer datos no confirmados.
- Lectura no repetible: leer dos veces el mismo dato y obtener valores distintos.
- Lectura fantasma: la misma consulta devuelve nuevas filas en una segunda ejecucion.

Niveles de aislamiento y relacion:

- `READ COMMITTED`: evita lecturas sucias.
- `REPEATABLE READ`: evita lecturas no repetibles.
- `SERIALIZABLE`: evita lecturas fantasma.

## Quiz

### Pregunta 1

**Pregunta:** Cual es el objetivo principal del control de concurrencia?

**Opciones:**
- a. Permitir que varias transacciones modifiquen el mismo dato simultaneamente.
- b. Reducir el tamano fisico de la base de datos.
- c. Preservar la aislacion de las transacciones concurrentes. ✓

**Por qué:** El control de concurrencia existe precisamente para que multiples usuarios puedan trabajar sin generarse inconsistencias. Si se permitiera modificacion simultanea sin control, los datos se corrompirian.

### Pregunta 2

**Pregunta:** En SQL Server, para evitar anomalias de concurrencia se recomienda:

**Opciones:**
- a. Permitir lecturas no confirmadas.
- b. Deshabilitar los bloqueos por completo.
- c. Usar niveles de aislamiento adecuados. ✓

**Por qué:** Los niveles de aislamiento (READ COMMITTED, REPEATABLE READ, SERIALIZABLE) ofrecen diferentes grados de proteccion. Elegir el nivel correcto segun el negocio es la practica recomendada.

### Pregunta 3

**Pregunta:** Si una transaccion no cumple las restricciones de integridad, el sistema debe:

**Opciones:**
- a. Guardar los datos parcialmente.
- b. Rechazar la transaccion completa. ✓
- c. Ajustar automaticamente los valores.

**Por qué:** Uno de los principios ACID es la atomicidad: una transaccion es "todo o nada". Si falla una restriccion, toda la transaccion debe revertirse para mantener la consistencia.

### Pregunta 4

**Pregunta:** Cual de los siguientes metodos utiliza bloqueos para gestionar la concurrencia?

**Opciones:**
- a. Timestamp Ordering.
- b. MVCC.
- c. Locking. ✓

**Por qué:** Locking (bloqueos) es el mecanismo mas directo: bloquea compartido para lectura, exclusivo para escritura, impidiendo modificaciones simultaneas del mismo dato.

### Pregunta 5

**Pregunta:** La consistencia es una de las propiedades del modelo:

**Opciones:**
- a. ACID. ✓
- b. ETL.
- c. CRUD.

**Por qué:** ACID es el modelo fundamental de transacciones confiables. Consistencia es la "C" en ACID, garantiza que las reglas de integridad se respeten.

### Pregunta 6

**Pregunta:** Que anomalia ocurre cuando una transaccion obtiene diferentes valores en dos lecturas del mismo dato?

**Opciones:**
- a. Lectura sucia.
- b. Lectura no repetible. ✓
- c. Lectura fantasma.

**Por qué:** "No repetible" significa que el dato cambio entre dos lecturas. Si lees salario=1000 y luego lees salario=1200, otro proceso lo modifico en medio.

### Pregunta 7

**Pregunta:** Cual de estas propiedades ACID asegura que las transacciones concurrentes no interfieran?

**Opciones:**
- a. Aislamiento. ✓
- b. Atomicidad.
- c. Consistencia.

**Por qué:** Aislamiento (la "I" en ACID) permite que transacciones concurrentes se ejecuten como si fueran en serie, sin verse mutuamente sus cambios intermedios.

### Pregunta 8

**Pregunta:** Un mecanismo de control de concurrencia eficaz debe equilibrar:

**Opciones:**
- a. Rapidez de hardware y consumo energetico.
- b. Diseno grafico y usabilidad.
- c. Consistencia y eficiencia. ✓

**Por qué:** Si el control es muy estricto (SERIALIZABLE), bloquea mucho y es lento. Si es muy laxo, permite anomalias. El balance optimo depende del negocio.

### Pregunta 9

**Pregunta:** El problema en el que dos transacciones esperan indefinidamente recursos bloqueados entre si se llama:

**Opciones:**
- a. Starvation.
- b. Deadlock. ✓
- c. Phantom Read.

**Por qué:** Deadlock es el ciclo de bloqueos: T1 espera un recurso que T2 tiene, T2 espera un recurso que T1 tiene. El sistema debe detectarlo y romper el ciclo.

### Pregunta 10

**Pregunta:** Cual es el rol de la consistencia dentro de ACID?

**Opciones:**
- a. Garantizar mayor velocidad de consultas.
- b. Permitir fallos parciales en transacciones.
- c. Asegurar que los datos respeten las reglas de negocio. ✓

**Por qué:** La consistencia conecta la logica del negocio (restricciones, integridad referencial) con la ejecucion tecnica de la transaccion. Sin ella, los datos quedan corrupto.

## Actividades

- [ ] Explicar con un ejemplo la diferencia entre lectura sucia, no repetible y fantasma.
- [ ] Investigar que nivel de aislamiento usa SQL Server por defecto y sus implicaciones.
- [ ] Crear una tabla con `PRIMARY KEY`, `FOREIGN KEY` y `CHECK` y probar que rompe la transaccion cuando se viola una regla.

