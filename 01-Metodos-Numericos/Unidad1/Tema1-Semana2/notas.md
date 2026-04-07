# 01-Metodos-Numericos - U1 T1 S2

## Objetivo de la semana
Comprender cómo representan los números las computadoras, por qué aparecen errores de redondeo y qué límites impone la aritmética de máquina al trabajar con métodos numéricos.

---

## Tema 1: Representación de números y aritmética de máquina

### 1.1 Sistemas de numeración y conversión básica

**Idea clave:**
Las computadoras no almacenan los números como los escribimos normalmente; internamente trabajan con un sistema binario basado en 0 y 1.

**Sistemas más comunes:**
- **Decimal:** base 10, el sistema cotidiano.
- **Binario:** base 2, usado por la computadora.
- **Octal y hexadecimal:** útiles para representar información de forma compacta.

**Conversión importante para estudiar:**
- Un número decimal puede expresarse en binario mediante divisiones sucesivas entre 2.
- Un número binario puede convertirse a decimal sumando potencias de 2.

**Ejemplo conceptual:**
Si un número no puede representarse exactamente en binario, la computadora guarda una aproximación.

**Consecuencia práctica:**
No todos los números reales pueden almacenarse de forma exacta.

### Palabras clave de 1.1
- Base numérica
- Binario
- Hexadecimal
- Conversión
- Representación

---

### 1.2 Números de punto flotante

**Definición clave:**
La mayoría de los valores reales se almacenan con formato de punto flotante, que separa un número en tres partes:
- **Signo**
- **Mantisa o significando**
- **Exponente**

**Forma general:**
Un número se expresa como una combinación de signo, mantisa y exponente para cubrir valores muy grandes y muy pequeños.

**Por qué es útil:**
- Permite representar números de magnitudes distintas.
- Hace posible el cálculo científico y de ingeniería.
- Optimiza el espacio de almacenamiento.

**Limitación principal:**
La precisión es finita, así que siempre existe un margen de error.

**Problemas típicos:**
- Pérdida de precisión en operaciones sucesivas.
- Desbordamiento si el número es demasiado grande.
- Subdesbordamiento si el número es demasiado pequeño.

### Palabras clave de 1.2
- Punto flotante
- Mantisa
- Exponente
- Precisión finita
- Desbordamiento
- Subdesbordamiento

---

### 1.3 Redondeo, truncamiento y error de máquina

**Redondeo:**
Consiste en aproximar un número al valor más cercano con cierta cantidad de cifras.

**Truncamiento:**
Consiste en cortar cifras a partir de una posición dada, sin considerar si el siguiente dígito justificaría redondear.

**Error de máquina:**
Es la diferencia entre el valor real y el valor que la computadora puede almacenar o manipular.

**Máquina y precisión:**
- La computadora no trabaja con infinitas cifras decimales.
- El resultado depende del formato de almacenamiento.
- Los errores pueden crecer si se repiten operaciones.

**Idea importante:**
En métodos numéricos no solo importa calcular, sino saber cuánta confianza tiene ese cálculo.

**Ejemplo práctico:**
Si se redondea demasiado pronto, el error puede acumularse y afectar el resultado final.

### Palabras clave de 1.3
- Redondeo
- Truncamiento
- Error de máquina
- Precisión finita
- Acumulación de error

---

## Resumen para estudiar

1. La computadora representa números en binario.
2. El formato de punto flotante divide el número en signo, mantisa y exponente.
3. No todos los números reales se pueden almacenar exactamente.
4. El redondeo y el truncamiento generan error.
5. La precisión de máquina tiene límites.
6. Los errores pequeños pueden acumularse en cálculos largos.

---

## Preguntas rápidas de repaso

1. ¿Por qué la computadora usa binario y no decimal?
2. ¿Qué partes componen un número de punto flotante?
3. ¿Cuál es la diferencia entre redondeo y truncamiento?
4. ¿Qué es el error de máquina?
5. ¿Qué puede pasar si se hacen muchas operaciones con valores aproximados?

---

## Estrategia de estudio

### Antes de la clase
- [ ] Repasa conversiones entre decimal y binario.
- [ ] Aprende la estructura básica del punto flotante.
- [ ] Diferencia redondeo, truncamiento y error de máquina.

### Durante la clase
- [ ] Anota ejemplos de conversión que use el profesor.
- [ ] Pregunta cómo afecta la precisión a un algoritmo numérico.
- [ ] Identifica cuándo se habla de error acumulado.

### Después de la clase
- [ ] Explica con tus palabras por qué existen límites de precisión.
- [ ] Haz conversiones simples entre bases.
- [ ] Resume la relación entre representación numérica y error.

---

## Quiz

### Pregunta 1: Punto flotante de 32 bits

**Pregunta:** En precisión simple (32 bits) de punto flotante, al signo le corresponde:

**Opciones:**
- ✅ 1 bit.
- ❌ 23 bits.
- ❌ 8 bits.

**Respuesta correcta:** 1 bit.

**Explicación breve:**
En IEEE 754 de 32 bits: 1 bit para signo, 8 bits para exponente y 23 bits para mantisa.

### Pregunta 2: Definición de byte

**Pregunta:** Un byte está compuesto por:

**Opciones:**
- ❌ 10 bits
- ✅ 8 bits
- ❌ 2 bits

**Respuesta correcta:** 8 bits.

**Explicación breve:**
Un byte es la unidad básica de almacenamiento y equivale a 8 bits.

### Pregunta 3: Magnitud con signo en 8 bits

**Pregunta:** En el sistema de magnitud con signo, el número 12 representado en 8 bits, sería:

**Opciones:**
- ✅ 00001100
- ❌ 10001000
- ❌ 00001110

**Respuesta correcta:** 00001100.

**Explicación breve:**
Para un número positivo, el bit de signo es 0 y la magnitud de 12 en binario es 0001100, por eso queda 00001100.

### Pregunta 4: Primer bit en magnitud con signo

**Pregunta:** En el sistema de magnitud con signo, el primer bit corresponde:

**Opciones:**
- ✅ Al signo
- ❌ A la base 2
- ❌ A un exponente

**Respuesta correcta:** Al signo.

**Explicación breve:**
El primer bit indica el signo del número: 0 para positivo y 1 para negativo.

### Pregunta 5: Estructura de punto flotante

**Pregunta:** La representación estándar de un número en punto flotante posee:

**Opciones:**
- ❌ Entero, Fracción, Exponente.
- ✅ Signo, Mantisa, Exponente.
- ❌ Precisión, Rango, Base.

**Respuesta correcta:** Signo, Mantisa, Exponente.

**Explicación breve:**
La estructura estándar separa el número en signo, exponente y mantisa (o significando).

### Pregunta 6: Verdadero o falso

**Afirmación:** El método de Müller utiliza una aproximación lineal (una recta) que pasa por dos puntos para estimar la siguiente aproximación de la raíz.

**Respuesta correcta:** Falso.

**Explicación breve:**
El método de Müller usa una aproximación cuadrática (una parábola) construida con tres puntos, no una recta de dos puntos.

### Pregunta 7: Verdadero o falso

**Afirmación:** El método de Bairstow está diseñado específicamente para encontrar las raíces de polinomios, extrayendo factores cuadráticos de forma iterativa.

**Respuesta correcta:** Verdadero.

**Explicación breve:**
Bairstow es un método iterativo orientado a polinomios que busca factores cuadráticos para obtener raíces reales y complejas.

### Pregunta 8: Verdadero o falso

**Afirmación:** Una ventaja del método de Müller es que, incluso partiendo de estimaciones iniciales reales, puede converger a raíces complejas.

**Respuesta correcta:** Verdadero.

**Explicación breve:**
Al usar una aproximación cuadrática, el método de Müller puede generar iteraciones en el plano complejo y converger a raíces complejas.

### Pregunta 9: Verdadero o falso

**Afirmación:** Para iniciar el método de Müller, se necesitan únicamente dos puntos iniciales.

**Respuesta correcta:** Falso.

**Explicación breve:**
El método de Müller requiere tres puntos iniciales para construir la aproximación cuadrática (parábola).

### Pregunta 10: Verdadero o falso

**Afirmación:** Para iniciar el método de Müller, no requiere el cálculo de la derivada de la función, a diferencia del método de Newton-Raphson.

**Respuesta correcta:** Verdadero.

**Explicación breve:**
Müller utiliza interpolación cuadrática con valores de la función, mientras que Newton-Raphson sí necesita la derivada.

## Actividades

