# 05-Administracion-BD - U2 T1 S2

## Notas de clase

## Tema 1. Fundamentos de recuperacion

### 1.3. Copias de seguridad y tipos de respaldo

Las copias de seguridad son la primera linea de defensa frente a fallos, perdida de informacion o desastres. Su objetivo es proteger datos y sostener la continuidad operativa.

Tipos principales:

- Full backup: copia completa de toda la base.
	- Ventaja: restauracion directa y rapida.
	- Desventaja: mayor tiempo y almacenamiento.

- Incremental backup: guarda solo cambios desde el ultimo respaldo (full o incremental).
	- Ventaja: menor espacio y rapidez al respaldar.
	- Desventaja: restauracion mas compleja (full + todos los incrementales).

- Differential backup: guarda cambios desde el ultimo full.
	- Ventaja: restauracion mas simple que incremental (full + ultimo diferencial).
	- Desventaja: crece con el tiempo hasta el siguiente full.

Copias fisicas y logicas:

- Fisicas: copian archivos binarios de datos y logs del motor.
- Logicas: exportan estructuras y datos en formato legible (scripts/volcados).

Seleccion del tipo: depende de tamano de BD, ventana de respaldo, almacenamiento y tiempo objetivo de restauracion.

### 1.4. Planificacion de respaldos y estrategias de recuperacion

Planificar respaldos significa definir que respaldar, cuando, donde almacenar y como restaurar en caso de fallo.

Elementos clave del plan:

- Frecuencia: combinacion de full periodico + diferencial/incremental mas frecuente.
- Almacenamiento y retencion: local, nube u otros medios segun costo y normativas.
- RPO (Recovery Point Objective): perdida maxima de datos aceptable.
- RTO (Recovery Time Objective): tiempo maximo permitido para recuperar el servicio.
- Pruebas de restauracion: validar que los respaldos realmente sirven.
- Automatizacion y monitoreo: programar tareas y alertas de fallo.

Ejemplo de estrategia tipica:

- Full semanal.
- Diferencial diario.
- Log de transacciones cada cierto intervalo corto.

Buenas practicas:

- Documentar procedimientos de respaldo/restauracion.
- Usar regla 3-2-1 (3 copias, 2 medios, 1 fuera del sitio).
- Verificar periodicamente integridad y disponibilidad de archivos de respaldo.

## Quiz

### Pregunta 1

**Pregunta:** El monitoreo de respaldos permite:

**Opciones:**
- a. Detectar fallos y cumplimiento del plan. ✓
- b. Evitar consultas complejas.
- c. Reducir tamano de BD.

**Por qué:** Monitorear asegura que los respaldos se ejecuten a su hora, que no fallen silenciosamente y que cumplan el plan de recuperacion definido.

### Pregunta 2

**Pregunta:** La automatizacion de respaldos busca:

**Opciones:**
- a. Reducir la intervencion manual. ✓
- b. Aumentar la complejidad.
- c. Eliminar monitoreo.

**Por qué:** Al automatizar con SQL Agent u otra herramienta, se evitan olvidos humanos y se garantiza consistencia. El monitoreo sigue siendo necesario pero sobre un proceso automático.

### Pregunta 3

**Pregunta:** Que significa la regla 3-2-1 en respaldos?

**Opciones:**
- a. 3 copias en 2 medios y 1 fuera del sitio. ✓
- b. 3 diarios, 2 semanales y 1 mensual.
- c. 3 politicas en 2 servidores y 1 nube.

**Por qué:** La regla 3-2-1 es una buena practica de redundancia: 3 copias (protege contra fallo de 1 o 2), en 2 medios distintos (discos y cintas), y 1 fuera del sitio (ante desastres locales).

### Pregunta 4

**Pregunta:** Un ejemplo de herramienta para copias fisicas en PostgreSQL es:

**Opciones:**
- a. pg_basebackup. ✓
- b. DBCC CHECKDB.
- c. pg_dump.

**Por qué:** pg_basebackup copia los archivos binarios del cluster; pg_dump es logica; DBCC es de SQL Server. Para copia fisica en PostgreSQL, pg_basebackup es la herramienta nativa.

### Pregunta 5

**Pregunta:** Una estrategia de respaldo adecuada debe equilibrar:

**Opciones:**
- a. Diseno de reportes.
- b. CPU, memoria y red.
- c. Seguridad, costo y rapidez. ✓

**Por qué:** Respaldos muy frecuentes son seguros pero costosos; poco frecuentes son baratos pero riesgosos. El balance optimo depende del negocio y sus tolerancias (RPO/RTO).

### Pregunta 6

**Pregunta:** Una copia completa (Full Backup) se caracteriza por:

**Opciones:**
- a. Respaldar toda la base de datos. ✓
- b. Exportar solo procedimientos almacenados.
- c. Respaldar unicamente los datos modificados.

**Por qué:** Un full backup es la copia integra de toda la BD. Los incrementales/diferenciales solo guardan cambios desde el ultimo full.

### Pregunta 7

**Pregunta:** Que ventaja ofrece el respaldo diferencial frente al incremental?

**Opciones:**
- a. No requiere respaldo completo previo.
- b. Es mas rapido para restaurar. ✓
- c. Ocupa menos espacio.

**Por qué:** Para restaurar con diferencial basta full + ultimo diferencial (2 archivos). Con incremental necesitas full + todos los incrementales en orden (muchos archivos), es mas lento.

### Pregunta 8

**Pregunta:** Cuando es mas recomendable usar un respaldo completo?

**Opciones:**
- a. En bases pequenas o antes de una migracion critica. ✓
- b. En sistemas que cambian constantemente durante el dia.
- c. Cuando se necesita ahorrar espacio.

**Por qué:** Full backups son rapidos de restaurar en una sola operacion y permiten partir de cero. Son ideales para eventos criticos (migraciones, cambios mayores) o bases pequenas donde el espacio no es limitante.

### Pregunta 9

**Pregunta:** Que asegura la documentacion en procesos de respaldo?

**Opciones:**
- a. Facilita ejecucion correcta de procedimientos. ✓
- b. Reduce tiempo de consultas SQL.
- c. Elimina necesidad de capacitacion.

**Por qué:** Cuando ocurre un desastre y necesitas restaurar rapido, la documentacion es guia critica. Sin ella, enfrentas retrasos o errores en procedimientos de emergencia.

### Pregunta 10

**Pregunta:** La retencion de respaldos depende de:

**Opciones:**
- a. Recursos y normativas legales. ✓
- b. Motor de BD empleado.
- c. Usuarios conectados.

**Por qué:** Leyes fiscales o de privacidad obligan a guardar datos cierto tiempo. Ademas, el presupuesto de almacenamiento determina cuanto tiempo puedes retener cópias. El motor no impone retencion.

## Actividades

- [ ] Definir un mini plan de respaldos con RPO y RTO para un sistema academico.
- [ ] Comparar con ejemplo numerico el tiempo de restauracion entre incremental y diferencial.
- [ ] Diseñar una politica de retencion de 3 meses local y 1 año externo justificando costo y riesgo.

