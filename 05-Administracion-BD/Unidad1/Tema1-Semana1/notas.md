# 05-Administracion-BD - U1 T1 S1

## Objetivo de la semana
Comprender los fundamentos de la administración de bases de datos, el rol del DBA y el concepto de transacción con sus propiedades ACID.

## Notas de clase

### 1.1 Administración de Bases de Datos, rol y funciones del DBA
La administración de bases de datos es la disciplina que planifica, organiza y controla la información almacenada en un sistema gestor. Su propósito es asegurar que los datos estén disponibles, íntegros, seguros y accesibles para la operación institucional.

El Administrador de Bases de Datos (DBA) es el profesional responsable de garantizar la continuidad, seguridad y rendimiento del entorno de datos.

Funciones principales del DBA:
- Instalar y mantener el sistema gestor de base de datos.
- Diseñar estructuras de almacenamiento y organización de datos.
- Administrar usuarios, roles y permisos.
- Implementar seguridad, respaldos y recuperación.
- Monitorear rendimiento, prevenir fallos y proponer mejoras.

Buenas prácticas recomendadas:
- Políticas periódicas de respaldo y recuperación.
- Control de accesos por usuarios y roles.
- Actualización de parches de seguridad.
- Monitoreo continuo del rendimiento.
- Documentación de procesos y pruebas antes de cambios críticos.

### 1.2 Concepto de transacción y propiedades ACID
Una transacción es una secuencia de operaciones que se ejecuta como una unidad indivisible. Si una parte falla, se revierte todo el proceso para evitar inconsistencias.

Ejemplo típico: una transferencia bancaria debe debitar una cuenta y acreditar otra; si uno de los pasos falla, se aplica ROLLBACK para cancelar toda la operación.

Propiedades ACID:
- Atomicidad: todo se ejecuta o no se ejecuta nada.
- Consistencia: se respetan reglas y restricciones de la base de datos.
- Aislamiento: las transacciones concurrentes no interfieren entre sí.
- Durabilidad: los cambios confirmados permanecen incluso ante fallos.

En SQL, esto se implementa con sentencias como BEGIN TRANSACTION, COMMIT y ROLLBACK.

## Resumen para estudiar
1. La administración de bases de datos asegura disponibilidad, seguridad e integridad de la información.
2. El DBA combina tareas técnicas y de gestión para mantener el sistema confiable.
3. Las buenas prácticas reducen riesgos y mejoran continuidad operativa.
4. Una transacción es una unidad lógica de trabajo que protege consistencia.
5. ACID es el marco clave para transacciones seguras en entornos reales.

## Preguntas rápidas
1. ¿Cuál es la responsabilidad principal de un DBA?
2. ¿Por qué es importante documentar procesos en administración de BD?
3. ¿Qué diferencia hay entre COMMIT y ROLLBACK?
4. ¿Qué garantiza la propiedad de aislamiento?
5. ¿Por qué ACID es crítico en sistemas multiusuario?

## Quiz

### Pregunta 1: Responsabilidad principal del DBA

**Pregunta:** ¿Cuál es la responsabilidad principal de un DBA?

**Opciones:**
- ❌ Diseñar campañas de marketing.
- ✅ Garantizar continuidad, seguridad y rendimiento del entorno de datos.
- ❌ Crear únicamente interfaces gráficas.

**Respuesta correcta:** Garantizar continuidad, seguridad y rendimiento del entorno de datos.

**Explicación breve:**
El DBA administra la base de datos para que los datos estén disponibles, íntegros, seguros y accesibles.

### Pregunta 2: Buenas prácticas del DBA

**Pregunta:** ¿Por qué es importante documentar procesos en administración de BD?

**Opciones:**
- ❌ Para aumentar la cantidad de tablas.
- ✅ Para facilitar mantenimiento, auditoría y recuperación ante fallos.
- ❌ Para evitar el uso de transacciones.

**Respuesta correcta:** Para facilitar mantenimiento, auditoría y recuperación ante fallos.

**Explicación breve:**
La documentación ayuda a reproducir procedimientos, entender cambios y responder mejor ante incidentes.

### Pregunta 3: COMMIT y ROLLBACK

**Pregunta:** ¿Qué diferencia hay entre COMMIT y ROLLBACK?

**Opciones:**
- ✅ COMMIT confirma los cambios y ROLLBACK los deshace.
- ❌ Ambos eliminan los datos de la tabla.
- ❌ ROLLBACK guarda los cambios y COMMIT los cancela.

**Respuesta correcta:** COMMIT confirma los cambios y ROLLBACK los deshace.

**Explicación breve:**
COMMIT hace permanentes los cambios; ROLLBACK revierte la transacción en caso de error.

### Pregunta 4: Aislamiento

**Pregunta:** ¿Qué garantiza la propiedad de aislamiento?

**Opciones:**
- ❌ Que todas las transacciones se ejecuten al mismo tiempo.
- ✅ Que las transacciones concurrentes no interfieran entre sí.
- ❌ Que ninguna transacción pueda hacer lecturas.

**Respuesta correcta:** Que las transacciones concurrentes no interfieran entre sí.

**Explicación breve:**
El aislamiento protege la consistencia evitando que una transacción vea estados intermedios de otra.

### Pregunta 5: Importancia de ACID

**Pregunta:** ¿Por qué ACID es crítico en sistemas multiusuario?

**Opciones:**
- ❌ Porque reemplaza los respaldos.
- ✅ Porque protege consistencia y confiabilidad al ejecutar varias transacciones a la vez.
- ❌ Porque elimina la necesidad de claves primarias.

**Respuesta correcta:** Porque protege consistencia y confiabilidad al ejecutar varias transacciones a la vez.

**Explicación breve:**
ACID asegura transacciones seguras, estables y confiables incluso cuando muchos usuarios trabajan al mismo tiempo.

## Actividades
- [ ] Explicar con tus palabras el rol del DBA en una organización.
- [ ] Identificar dos riesgos si no existen respaldos periódicos.
- [ ] Escribir un ejemplo simple de transacción con COMMIT y ROLLBACK.

