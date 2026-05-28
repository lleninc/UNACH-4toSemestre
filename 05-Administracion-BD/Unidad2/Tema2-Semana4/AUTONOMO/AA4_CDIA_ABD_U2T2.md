# Actividad Autonoma 4

**Asignatura:** Administracion de Bases de Datos  
**Unidad:** 2 - Recuperacion avanzada de bases de datos  
**Tema:** Recuperacion en gestores de BD  
**Caso propuesto:** Tienda de ropa  

## 1. Objetivo

Analizar e implementar mecanismos de recuperacion en gestores de bases de datos, incluyendo logs de transacciones, planes de recuperacion ante desastres y buenas practicas de recuperacion, mediante un caso practico basado en una base de datos de tienda de ropa.

## 2. Base de datos propuesta

Se plantea una base de datos llamada **TiendaRopa_DB** con las tablas:

- `Categorias`
- `Clientes`
- `Productos`
- `Ventas`
- `DetalleVenta`

Esta estructura permite simular operaciones reales de una tienda de ropa, como el registro de clientes, el control de inventario y el detalle de ventas.

## 3. Logs de transacciones

En SQL Server el log de transacciones se activa de forma nativa y se aprovecha mejor cuando la base trabaja con el modelo de recuperacion **FULL**. Para este caso se realiza lo siguiente:

1. Crear la base de datos y configurar el modelo FULL.
2. Ejecutar transacciones con `INSERT`, `UPDATE` y `DELETE`.
3. Demostrar `UNDO` con `ROLLBACK TRAN`.
4. Demostrar `REDO` con `COMMIT TRAN` y restauracion desde backup de log.

### Ejemplo de UNDO

Una transaccion modifica inventario y elimina un producto, pero antes del `COMMIT` se ejecuta `ROLLBACK`. El resultado es que SQL Server deshace todos los cambios de esa transaccion.

### Ejemplo de REDO

Una transaccion confirmada con `COMMIT` queda registrada en el log. Si ocurre una falla, la restauracion desde el backup completo mas los backups de log permite reconstruir el estado hasta un punto exacto con `RESTORE LOG ... WITH STOPAT`.

## 4. Metodo de recuperacion ante desastres

### Escenario de desastre

Para la tienda de ropa se propone el siguiente escenario:

- falla del disco donde vive la base de datos, o
- borrado accidental de registros en `Productos` o `DetalleVenta`.

### Metodo 1: Log shipping en SQL Server

El log shipping permite copiar y restaurar automaticamente backups de log desde el servidor primario a un servidor secundario. Es util para tener un servidor listo para asumir la operacion con una perdida minima de datos.

### Metodo 2: PITR en PostgreSQL

El Point-in-Time Recovery permite volver la base a un momento exacto usando WAL y restauracion hasta una hora o transaccion especifica. Es una tecnica especialmente util cuando se requiere recuperar datos antes de un error puntual.

### Plan DRP basico

**RPO propuesto:** 15 minutos  
**RTO propuesto:** 1 hora  
**Roles:**

- Administrador de BD: ejecuta restauracion y valida integridad.
- Responsable de infraestructura: verifica almacenamiento, red y respaldo.
- Usuario clave del negocio: valida que ventas e inventario quedaron correctos.

**Procedimiento resumido:**

1. Detectar el incidente y detener cambios sobre la base afectada.
2. Identificar el ultimo backup completo y el ultimo backup de log valido.
3. Restaurar la base en un entorno alterno o secundario.
4. Aplicar los logs hasta el punto de recuperacion requerido.
5. Validar tablas criticas, inventario y ventas.
6. Reactivar el servicio y documentar el incidente.

## 5. Buenas practicas de recuperacion

| Practica | Estándar / referencia | Beneficio |
|---|---|---|
| Estrategia 3-2-1 de respaldos | ISO/IEC 27001, NIST | Reduce la probabilidad de perder todos los respaldos al mismo tiempo. |
| Pruebas periodicas de restauracion | COBIT DSS04 | Confirma que los backups realmente son recuperables. |
| Uso de modelo FULL y backups de log | SQL Server / WAL en PostgreSQL | Permite recuperar hasta un punto exacto y minimizar perdida de datos. |
| Control de accesos y separacion de funciones | ISO/IEC 27001, Ley Organica de Proteccion de Datos Personales del Ecuador | Evita borrados accidentales o manipulacion no autorizada. |
| Monitoreo y alertas de respaldo | NIST SP 800-34 | Detecta fallos de backup antes de que ocurra una contingencia real. |

Estas practicas fortalecen la seguridad y la continuidad operativa porque reducen el tiempo de indisponibilidad, mejoran la confiabilidad de la restauracion y disminuyen el impacto de errores humanos o fallos tecnicos.

## 6. Caso practico de recuperacion en DBMS

### SQL Server

La restauracion puntual se realiza con `RESTORE DATABASE ... WITH NORECOVERY` y luego `RESTORE LOG ... WITH STOPAT`. Este metodo es practico cuando se dispone de backups completos y de log ordenados.

### PostgreSQL

La recuperacion puntual usa WAL y parametros como `recovery_target_time`. El servidor se levanta desde el respaldo y avanza hasta la hora exacta solicitada.

### Comparacion

- SQL Server es mas directo cuando ya existe una politica de backups completos y de log bien automatizada.
- PostgreSQL ofrece una recuperacion puntual muy flexible si la archivacion de WAL esta correctamente configurada.
- Para este escenario, ambos sirven, pero SQL Server resulta mas sencillo de demostrar en laboratorio con `STOPAT`, mientras que PostgreSQL destaca por la granularidad del WAL.

## 7. Conclusiones

La base de datos de tienda de ropa permite mostrar de forma practica el uso del log de transacciones, la recuperacion ante errores y la necesidad de un DRP formal. El uso combinado de backups completos, backups de log y pruebas de restauracion hace posible recuperar el servicio con una perdida minima de informacion.

## 8. Archivos entregables

- `AA4_CDIA_ABD_U2T2.sql`: script con la base de datos, transacciones y ejemplos de recuperacion.
- Este archivo Markdown puede exportarse a PDF para cumplir el formato de entrega solicitado.