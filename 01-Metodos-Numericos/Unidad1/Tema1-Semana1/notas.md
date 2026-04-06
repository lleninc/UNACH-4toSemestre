# 01-Metodos-Numericos - U1 T1 S1

## Objetivo de la semana
Repasar la lectura de las páginas 1 a 14 del Tema 1 para entender qué estudian los métodos numéricos, cómo representan números las computadoras, cómo se hacen conversiones entre bases y por qué aparecen errores de redondeo y precisión.

---

## Tema 1: Introducción a los métodos numéricos y representación numérica

### 1.1 Concepto y utilidad de los métodos numéricos

**Definición clave:**
Los métodos numéricos son procedimientos matemáticos y computacionales que permiten obtener **soluciones aproximadas** a problemas que no siempre pueden resolverse de forma exacta con técnicas algebraicas tradicionales.

**¿Por qué se usan?**
- Porque muchos problemas reales son demasiado complejos para una solución cerrada.
- Porque en ingeniería y ciencia se necesita una respuesta rápida y útil.
- Porque las computadoras trabajan muy bien con aproximaciones iterativas.

**Idea central:**
Un método numérico no busca “la respuesta perfecta”, sino una respuesta **suficientemente buena** dentro de un margen de error aceptable.

**Ejemplos típicos de uso:**
- Encontrar raíces de ecuaciones no lineales.
- Aproximar integrales o derivadas.
- Resolver sistemas de ecuaciones grandes.
- Modelar fenómenos físicos, económicos o de ingeniería.

**Ventaja principal:**
Permiten resolver problemas prácticos donde la solución exacta es difícil, costosa o imposible de obtener.

**Limitación importante:**
Toda aproximación introduce error, por eso el análisis de error es parte esencial del tema.

**Idea complementaria:**
En métodos numéricos, la calidad del resultado depende tanto del procedimiento como de la forma en que la computadora guarda los datos.

### Palabras clave de 1.1
- Aproximación
- Iteración
- Solución numérica
- Problema no lineal
- Computación

---

### 1.2 Sistemas de numeración

**Definición clave:**
Un sistema de numeración es el conjunto de símbolos y reglas que se usan para representar cantidades.

**Sistemas que debes dominar:**
- **Decimal (base 10):** usa los dígitos del 0 al 9.
- **Binario (base 2):** usa los dígitos 0 y 1.
- **Octal (base 8):** usa del 0 al 7.
- **Hexadecimal (base 16):** usa 0 al 9 y A al F.

**Importancia en computación:**
Las computadoras trabajan internamente en binario porque sus circuitos eléctricos manejan dos estados estables: encendido y apagado.

**Conversión decimal a binario:**
- Se divide el número entre 2 de forma sucesiva.
- Los residuos, leídos de abajo hacia arriba, forman el número binario.

**Conversión binario a decimal:**
- Se suman los valores de cada posición multiplicando por potencias de 2.

**Ejemplo corto:**
111011$_2$ = $1\cdot 2^5 + 1\cdot 2^4 + 1\cdot 2^3 + 0\cdot 2^2 + 1\cdot 2^1 + 1\cdot 2^0 = 59_{10}$.

### Palabras clave de 1.2
- Base numérica
- Binario
- Decimal
- Conversión
- Potencias de 2

---

### 1.3 Representación de números fraccionarios

**Definición clave:**
No solo se representan enteros; también se pueden representar fracciones y decimales.

**Conversión decimal fraccionaria a binario:**
- Se multiplica la parte fraccionaria por 2.
- La parte entera obtenida en cada paso forma los bits binarios.
- El proceso continúa hasta obtener precisión suficiente o hasta que el valor se repita.

**Ejemplo exacto:**
0.6875$_{10}$ = 0.1011$_2$.

**Ejemplo aproximado:**
0.65$_{10}$ no termina en binario; su representación es infinita periódica y solo puede almacenarse como aproximación.

**Idea importante:**
Algunas fracciones tienen representación finita en binario y otras no.

### Palabras clave de 1.3
- Fracción binaria
- Parte entera
- Parte fraccionaria
- Aproximación
- Expansión infinita

---

### 1.4 Error, precisión, exactitud y aritmética de máquina

**Definición clave:**
El error es la diferencia entre un valor real o verdadero y un valor aproximado obtenido por cálculo o medición.

**Fórmulas útiles:**
- Error absoluto: `|valor verdadero - valor aproximado|`
- Error relativo: `error absoluto / |valor verdadero|`
- Error porcentual: `error relativo * 100`

**Tipos de error que debes reconocer:**

| Tipo de error | Qué significa | Ejemplo |
|---|---|---|
| **Error de truncamiento** | Aparece al reemplazar un proceso infinito por uno finito | Cortar una serie o una iteración antes de tiempo |
| **Error de redondeo** | Surge al limitar cifras decimales o significativas | Usar 3.1416 en lugar de π |
| **Error por datos iniciales** | El dato de entrada ya viene con imprecisión | Medidas tomadas con instrumentos poco precisos |
| **Error acumulado** | Se va sumando durante varios pasos de cálculo | Repetir operaciones aproximadas en un algoritmo iterativo |

**Precisión vs exactitud:**
- **Precisión**: qué tan cerca están entre sí varios resultados.
- **Exactitud**: qué tan cerca está el resultado del valor verdadero.

**Aritmética de máquina:**
- La computadora trabaja con un número limitado de cifras.
- No todos los números reales pueden representarse exactamente.
- Cuando un número excede la capacidad del formato, aparece desbordamiento.
- Cuando un número es demasiado pequeño, puede aparecer subdesbordamiento.

**Cifras significativas:**
- Indican cuánta confianza hay en un número.
- Ayudan a expresar resultados con el nivel correcto de detalle.
- Evitan dar una falsa sensación de exactitud.

### Palabras clave de 1.4
- Error absoluto
- Error relativo
- Redondeo
- Truncamiento
- Cifras significativas
- Precisión
- Exactitud
- Desbordamiento
- Subdesbordamiento

---

## Ejercicios resueltos

### Ejercicio 1: Convertir 15$_{10}$ a binario

**Procedimiento:**
1. $15 \div 2 = 7$ residuo $1$
2. $7 \div 2 = 3$ residuo $1$
3. $3 \div 2 = 1$ residuo $1$
4. $1 \div 2 = 0$ residuo $1$

**Resultado:**
15$_{10}$ = 1111$_2$

### Ejercicio 2: Convertir 17$_{10}$ a binario

**Procedimiento:**
1. $17 \div 2 = 8$ residuo $1$
2. $8 \div 2 = 4$ residuo $0$
3. $4 \div 2 = 2$ residuo $0$
4. $2 \div 2 = 1$ residuo $0$
5. $1 \div 2 = 0$ residuo $1$

**Resultado:**
17$_{10}$ = 10001$_2$

### Ejercicio 3: Convertir 8$_{10}$ a binario

**Procedimiento:**
1. $8 \div 2 = 4$ residuo $0$
2. $4 \div 2 = 2$ residuo $0$
3. $2 \div 2 = 1$ residuo $0$
4. $1 \div 2 = 0$ residuo $1$

**Resultado:**
8$_{10}$ = 1000$_2$

### Ejercicio 4: Convertir 0.75$_{10}$ a binario

**Procedimiento:**
1. $0.75 \times 2 = 1.50$ → parte entera: $1$
2. $0.50 \times 2 = 1.00$ → parte entera: $1$

**Resultado:**
0.75$_{10}$ = 0.11$_2$

### Ejercicio 5: Convertir 0.25$_{10}$ a binario

**Procedimiento:**
1. $0.25 \times 2 = 0.50$ → parte entera: $0$
2. $0.50 \times 2 = 1.00$ → parte entera: $1$

**Resultado:**
0.25$_{10}$ = 0.01$_2$

### Idea para recordar
En números enteros, se divide entre 2 y se leen residuos hacia arriba; en fracciones, se multiplica por 2 y se leen los bits en el orden en que aparecen.

---

## Resumen para estudiar

1. Los métodos numéricos sirven para obtener soluciones aproximadas.
2. Su uso es indispensable cuando la solución exacta no existe o no conviene usarla.
3. Las computadoras usan sistemas de numeración, sobre todo binario.
4. Las conversiones entre decimal y binario son básicas para el tema.
5. Algunas fracciones tienen representación binaria exacta y otras solo aproximada.
6. Todo método numérico introduce error.
7. Los errores principales son de truncamiento, redondeo y acumulación.
8. Precisión y exactitud no significan lo mismo.
9. El objetivo no es solo calcular, sino controlar la calidad de la aproximación.

---

## Preguntas rápidas de repaso

1. ¿Por qué se usan métodos numéricos en lugar de métodos exactos?
2. ¿Qué dígitos usa el sistema binario?
3. ¿Cómo se convierte un número decimal a binario?
4. ¿Cuál es la diferencia entre una representación binaria exacta y una aproximada?
5. ¿Cuál es la diferencia entre error absoluto y error relativo?
6. ¿Qué diferencia hay entre precisión y exactitud?
7. ¿Cómo se produce el error de redondeo?
8. ¿Por qué el análisis de error es tan importante en métodos numéricos?

---

## Estrategia de estudio

### Antes de la clase
- [ ] Lee y memoriza la definición de método numérico.
- [ ] Repasa los sistemas decimal y binario.
- [ ] Practica una conversión decimal a binario y una binaria a decimal.
- [ ] Aprende las fórmulas de error absoluto, relativo y porcentual.
- [ ] Distingue precisión de exactitud con un ejemplo propio.

### Durante la clase
- [ ] Anota ejemplos que use el docente para truncamiento y redondeo.
- [ ] Observa cuándo una fracción tiene representación exacta y cuándo no.
- [ ] Pregunta cómo se decide si una aproximación es aceptable.
- [ ] Identifica qué criterio de error pide el profesor.

### Después de la clase
- [ ] Resume 1.1 y 1.2 con tus palabras.
- [ ] Resuelve ejercicios de conversiones entre decimal y binario.
- [ ] Resuelve al menos un ejercicio de error absoluto y relativo.
- [ ] Repite las definiciones hasta poder explicarlas sin mirar.

---

## Quiz

### Pregunta 1: Sistema binario

**Pregunta:** En el sistema binario se utilizan:

**Opciones:**
- ❌ Los dígitos 1 y 2
- ❌ Dígitos del 0 al 9
- ✅ Los dígitos 0 y 1

**Respuesta correcta:** Los dígitos 0 y 1.

**Explicación breve:**
El sistema binario es la base de funcionamiento de las computadoras y solo usa dos símbolos para representar toda la información: 0 y 1.

### Pregunta 2: Conversión a binario

**Pregunta:** La representación binaria del número 27$_{10}$ es:

**Opciones:**
- ❌ 10011$_2$
- ❌ 11010$_2$
- ✅ 11011$_2$

**Respuesta correcta:** 11011$_2$.

**Explicación breve:**
27 en decimal se descompone como $16 + 8 + 2 + 1$, por eso en binario se escribe 11011.

### Pregunta 3: Conversión a decimal

**Pregunta:** La representación en sistema decimal del número 111011$_2$ es:

**Opciones:**
- ✅ 59$_{10}$
- ❌ 79$_{10}$
- ❌ 69$_{10}$

**Respuesta correcta:** 59$_{10}$.

**Explicación breve:**
111011$_2$ = $32 + 16 + 8 + 2 + 1 = 59$.

### Pregunta 4: Conversión a binario de un decimal fraccionario

**Pregunta:** La representación binaria del número 0.6875$_{10}$ es:

**Opciones:**
- ✅ 0.1011$_2$
- ❌ 0.1101$_2$
- ❌ 0.1110$_2$

**Respuesta correcta:** 0.1011$_2$.

**Explicación breve:**
0.6875 = $1/2 + 0/4 + 1/8 + 1/16$, por eso en binario se escribe 0.1011.

### Pregunta 5: Aproximación binaria

**Pregunta:** La representación binaria del número 0.65$_{10}$ es aproximadamente:

**Opciones:**
- ✅ $(0.1011111\ldots)_2$
- ❌ $(0.1110011\ldots)_2$
- ❌ $(0.1010011\ldots)_2$

**Respuesta correcta:** $(0.1011111\ldots)_2$.

**Explicación breve:**
0.65 no tiene representación binaria finita exacta; su forma en base 2 es una expansión infinita periódica aproximada.

## Actividades

