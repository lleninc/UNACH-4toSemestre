# 05-Administracion-BD - U1 T2 S4

## Objetivo de la semana
Analizar el uso de triggers y técnicas de optimización de consultas para mejorar el control automático de eventos y el rendimiento en sistemas de bases de datos.

## Notas de clase

### 2.3 Triggers
Un trigger (disparador) es un bloque de código que se ejecuta automáticamente cuando ocurre un evento en una tabla o vista, como INSERT, UPDATE o DELETE.

Propósitos principales:
- Auditar cambios (quién, cuándo, qué cambió).
- Aplicar reglas de negocio automáticas.
- Mantener consistencia entre tablas relacionadas.

Tipos comunes:
- BEFORE: se ejecuta antes del evento.
- AFTER: se ejecuta después del evento.
- INSTEAD OF: reemplaza la operación original (según motor).

Ejemplo de trigger de auditoría:
```sql
CREATE TRIGGER trg_AuditoriaCliente
ON clientes
AFTER INSERT
AS
BEGIN
	INSERT INTO auditoria_clientes(cliente_id, fecha, accion)
	SELECT id, GETDATE(), 'INSERT'
	FROM inserted;
END;
```

### 2.4 Optimización de consultas, ejercicios de aplicación
Optimizar consultas significa reducir tiempos de respuesta y consumo de recursos al ejecutar SQL.

Buenas prácticas de optimización:
- Crear índices en columnas usadas en filtros y JOIN.
- Evitar SELECT * cuando no se necesitan todas las columnas.
- Usar JOIN explícitos con condiciones claras.
- Revisar planes de ejecución para detectar cuellos de botella.
- Reducir subconsultas costosas cuando una CTE o JOIN sea más eficiente.

Ejemplo comparativo:
```sql
-- Menos óptimo
SELECT *
FROM pedidos p, clientes c
WHERE p.id_cliente = c.id;

-- Más óptimo y legible
SELECT p.id_pedido, c.nombre
FROM pedidos p
INNER JOIN clientes c ON p.id_cliente = c.id;
```

Ejercicios de aplicación sugeridos:
- Medir tiempo de una consulta antes y después de crear un índice.
- Reescribir una consulta con JOIN implícito a JOIN explícito.
- Implementar un trigger de auditoría para cambios de saldo.

## Resumen para estudiar
1. Los triggers ejecutan lógica automáticamente ante eventos en tablas.
2. Son útiles para auditoría, integridad y reglas de negocio automáticas.
3. La optimización busca consultas más rápidas y menos costosas.
4. Índices y buenas prácticas de escritura SQL mejoran rendimiento.
5. Medir antes y después de optimizar permite justificar decisiones técnicas.

## Preguntas rápidas
1. ¿Qué diferencia hay entre un trigger BEFORE y un AFTER?
2. ¿Qué riesgos existen si se usa un trigger sin control?
3. ¿Por qué evitar SELECT * en consultas de producción?
4. ¿Cómo ayuda un índice a acelerar una consulta?
5. ¿Por qué es importante revisar planes de ejecución?

## Quiz

### Pregunta 1: Definición de trigger

**Pregunta:** ¿Qué es un trigger en una base de datos?

**Opciones:**
- ❌ Una tabla temporal creada por el usuario.
- ✅ Un bloque de código que se ejecuta automáticamente ante eventos de datos.
- ❌ Un tipo de índice no agrupado.

**Respuesta correcta:** Un bloque de código que se ejecuta automáticamente ante eventos de datos.

**Explicación breve:**
Los triggers reaccionan a operaciones como INSERT, UPDATE o DELETE sin invocación manual.

### Pregunta 2: Uso de trigger

**Pregunta:** ¿Cuál es un uso común de los triggers?

**Opciones:**
- ❌ Reemplazar todos los procedimientos almacenados.
- ✅ Registrar auditoría de cambios.
- ❌ Crear automáticamente bases de datos nuevas.

**Respuesta correcta:** Registrar auditoría de cambios.

**Explicación breve:**
Un escenario típico es guardar historial de modificaciones para control y trazabilidad.

### Pregunta 3: SELECT *

**Pregunta:** ¿Por qué se recomienda evitar SELECT * en producción?

**Opciones:**
- ❌ Porque no permite usar WHERE.
- ✅ Porque trae columnas innecesarias y puede degradar rendimiento.
- ❌ Porque bloquea permanentemente la tabla.

**Respuesta correcta:** Porque trae columnas innecesarias y puede degradar rendimiento.

**Explicación breve:**
Seleccionar solo columnas requeridas reduce E/S, memoria y tráfico de datos.

### Pregunta 4: Índices

**Pregunta:** ¿Qué efecto principal tiene un índice bien diseñado?

**Opciones:**
- ✅ Acelerar búsquedas y filtros frecuentes.
- ❌ Eliminar restricciones de integridad.
- ❌ Evitar totalmente el uso de JOIN.

**Respuesta correcta:** Acelerar búsquedas y filtros frecuentes.

**Explicación breve:**
El índice reduce el número de lecturas para localizar registros solicitados.

### Pregunta 5: Optimización basada en evidencia

**Pregunta:** ¿Qué práctica valida mejor una optimización de consulta?

**Opciones:**
- ❌ Suponer que siempre será más rápida por cambiar sintaxis.
- ✅ Comparar métricas y plan de ejecución antes y después.
- ❌ Eliminar todas las cláusulas JOIN.

**Respuesta correcta:** Comparar métricas y plan de ejecución antes y después.

**Explicación breve:**
Optimizar requiere medir impacto real para confirmar que la mejora es efectiva y estable.

### Pregunta 6: DSN y seguridad

**Pregunta:** ¿Cuál es una característica importante del uso de DSN en seguridad?

**Opciones:**
- ❌ Elimina la necesidad de drivers.
- ✅ Permite ocultar contraseñas al no almacenarlas en texto plano.
- ❌ Evita el uso de puertos.

**Respuesta correcta:** Permite ocultar contraseñas al no almacenarlas en texto plano.

**Explicación breve:**
Un DSN puede centralizar la configuración de conexión y ayudar a proteger credenciales mediante mecanismos de almacenamiento más seguros.

### Pregunta 7: Cadena de conexión

**Pregunta:** ¿Cuál es la finalidad de una cadena de conexión?

**Opciones:**
- ❌ Registrar eventos de la base de datos.
- ❌ Proporcionar acceso remoto seguro.
- ✅ Especificar los parámetros para establecer una conexión a la base de datos.

**Respuesta correcta:** Especificar los parámetros para establecer una conexión a la base de datos.

**Explicación breve:**
La cadena de conexión reúne datos como servidor, base de datos, usuario y contraseña para que la aplicación pueda conectarse correctamente.

### Pregunta 8: Puerto por defecto de MySQL

**Pregunta:** ¿Cuál es el puerto por defecto utilizado por MySQL para las conexiones?

**Opciones:**
- ❌ 1433
- ✅ 3306
- ❌ 5432

**Respuesta correcta:** 3306

**Explicación breve:**
MySQL usa el puerto 3306 de manera predeterminada para aceptar conexiones de clientes.

### Pregunta 9: Conexiones remotas en PostgreSQL

**Pregunta:** ¿Qué archivo debe modificarse en PostgreSQL para permitir conexiones remotas?

**Opciones:**
- ❌ config.ini
- ❌ postgresql.exe
- ✅ pg_hba.conf

**Respuesta correcta:** pg_hba.conf

**Explicación breve:**
El archivo pg_hba.conf controla qué hosts y usuarios pueden conectarse a PostgreSQL, por lo que se ajusta para permitir acceso remoto.

### Pregunta 10: Parámetro charset

**Pregunta:** ¿Cuál es el propósito del parámetro 'charset' en una cadena de conexión?

**Opciones:**
- ❌ Definir el tipo de red utilizada para la conexión.
- ❌ Limitar el tamaño de la base de datos.
- ✅ Especificar el conjunto de caracteres usado para la conexión.

**Respuesta correcta:** Especificar el conjunto de caracteres usado para la conexión.

**Explicación breve:**
El parámetro charset indica la codificación que usará la conexión para interpretar correctamente texto y caracteres especiales.

## Actividades
- [ ] Crear un trigger de auditoría para registrar cambios en una tabla de cuentas.
- [ ] Comparar una consulta con SELECT * frente a una consulta de columnas específicas.
- [ ] Proponer un índice para una consulta frecuente y justificar su elección.

