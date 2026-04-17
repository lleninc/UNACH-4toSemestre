# 05-Administracion-BD - U1 T2 S3

## Objetivo de la semana
Comprender el uso de vistas, funciones y procedimientos almacenados para encapsular consultas, reutilizar lógica y mejorar la seguridad y mantenibilidad en bases de datos.

## Notas de clase

### 2.1 Vistas y Funciones
Una vista es una tabla virtual definida por una consulta SQL. No almacena datos propios (salvo vistas materializadas en motores específicos), sino que muestra resultados de tablas base.

Ventajas principales de las vistas:
- Simplifican consultas complejas para usuarios finales.
- Mejoran seguridad al exponer solo columnas o filas necesarias.
- Ayudan a estandarizar reportes y acceso a información.

Ejemplo de vista:
```sql
CREATE VIEW Vista_Clientes AS
SELECT nombre, ciudad
FROM clientes;
```

Las funciones son bloques reutilizables de código SQL que retornan resultados.

Tipos frecuentes:
- Funciones escalares: devuelven un único valor.
- Funciones de tabla: devuelven un conjunto de filas.

Ejemplo de función escalar:
```sql
CREATE FUNCTION calcular_descuento(@precio DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
	RETURN @precio * 0.10;
END;
```

### 2.2 Procedimientos almacenados
Un procedimiento almacenado es un conjunto de instrucciones SQL guardado en el servidor para ejecutar tareas de forma repetible y controlada.

Características clave:
- Puede incluir lógica condicional y manejo de errores.
- Puede recibir parámetros de entrada y devolver resultados.
- Se usa para encapsular reglas de negocio en la capa de datos.

Beneficios:
- Reduce tráfico entre aplicación y servidor.
- Facilita mantenimiento al centralizar lógica.
- Permite controlar permisos sobre acciones críticas.

Ejemplo de procedimiento:
```sql
CREATE PROCEDURE ActualizarSaldo
	@cliente_id INT,
	@valor DECIMAL(10,2)
AS
BEGIN
	UPDATE cuentas
	SET saldo = saldo + @valor
	WHERE cliente_id = @cliente_id;
END;
```

## Resumen para estudiar
1. Las vistas simplifican consultas y mejoran seguridad al abstraer tablas base.
2. Las funciones permiten reutilizar cálculos o lógica SQL de manera consistente.
3. Los procedimientos almacenados encapsulan procesos completos en la base de datos.
4. El uso combinado de vistas, funciones y procedimientos mejora orden y mantenibilidad.
5. Diseñar correctamente estos objetos reduce errores y facilita evolución del sistema.

## Preguntas rápidas
1. ¿Qué diferencia existe entre una tabla física y una vista?
2. ¿Cuándo conviene usar una función escalar y cuándo una función de tabla?
3. ¿Qué ventaja de seguridad ofrecen las vistas?
4. ¿Por qué un procedimiento almacenado reduce tráfico de red?
5. ¿Qué tipo de lógica conviene encapsular en procedimientos?

## Quiz

### Pregunta 1: Concepto de vista

**Pregunta:** ¿Qué es una vista en bases de datos?

**Opciones:**
- ❌ Una copia física completa de una tabla.
- ✅ Una tabla virtual definida por una consulta.
- ❌ Un índice para acelerar búsquedas.

**Respuesta correcta:** Una tabla virtual definida por una consulta.

**Explicación breve:**
La vista presenta resultados de tablas base sin duplicar físicamente los datos.

### Pregunta 2: Función escalar

**Pregunta:** ¿Qué devuelve una función escalar?

**Opciones:**
- ✅ Un único valor.
- ❌ Siempre una tabla con varias filas.
- ❌ Un procedimiento ejecutable.

**Respuesta correcta:** Un único valor.

**Explicación breve:**
La función escalar se usa para cálculos puntuales como porcentajes, conversiones o validaciones simples.

### Pregunta 3: Procedimiento almacenado

**Pregunta:** ¿Cuál es una ventaja de usar procedimientos almacenados?

**Opciones:**
- ❌ Elimina la necesidad de claves primarias.
- ✅ Centraliza lógica de negocio en el servidor.
- ❌ Reemplaza automáticamente todas las tablas.

**Respuesta correcta:** Centraliza lógica de negocio en el servidor.

**Explicación breve:**
Permite mantener procesos comunes en un solo lugar, facilitando control y mantenimiento.

### Pregunta 4: Seguridad con vistas

**Pregunta:** ¿Cómo aportan seguridad las vistas?

**Opciones:**
- ✅ Permiten mostrar solo columnas o filas autorizadas.
- ❌ Bloquean cualquier consulta SELECT.
- ❌ Sustituyen el control de usuarios.

**Respuesta correcta:** Permiten mostrar solo columnas o filas autorizadas.

**Explicación breve:**
Las vistas actúan como capa de acceso limitada sobre tablas sensibles.

### Pregunta 5: Reutilización de lógica

**Pregunta:** ¿Qué combinación mejora más la reutilización en SQL?

**Opciones:**
- ❌ Solo crear tablas temporales.
- ✅ Definir funciones y procedimientos para tareas repetitivas.
- ❌ Evitar completamente el uso de objetos de BD.

**Respuesta correcta:** Definir funciones y procedimientos para tareas repetitivas.

**Explicación breve:**
Estos objetos evitan duplicar código y disminuyen fallos por inconsistencias entre consultas.

## Actividades
- [ ] Crear una vista que muestre únicamente columnas públicas de una tabla de clientes.
- [ ] Diseñar una función escalar para calcular IVA sobre un precio.
- [ ] Implementar un procedimiento almacenado para registrar un pago y actualizar saldo.

