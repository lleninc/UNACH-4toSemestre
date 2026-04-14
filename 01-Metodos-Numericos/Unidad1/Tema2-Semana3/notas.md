# 01-Metodos-Numericos - U1 T2 S3

## Notas de clase

### 2. Tema 2: Errores numéricos en métodos computacionales

En métodos numéricos no se suele obtener la solución exacta. El objetivo real es aproximar el resultado con un error controlado y entender de dónde proviene ese error.

### 2.1 Caracterización de los errores y cálculo de errores

Un error numérico es la diferencia entre un valor exacto y un valor aproximado.

$$
Error\ absoluto = |x - \tilde{x}|
$$

$$
Error\ relativo = \frac{|x - \tilde{x}|}{|x|}
$$

Donde:
- $x$ es el valor exacto.
- $\tilde{x}$ es el valor aproximado.

#### Tipos de error

| Tipo de error | Descripción | Ejemplo |
|---|---|---|
| Absoluto | Mide la distancia directa entre exacto y aproximado | $|3.1416 - 3.14|$ |
| Relativo | Mide el error respecto al tamaño del valor real | Error en una medida grande o pequeña |
| Porcentual | Error relativo multiplicado por 100 | Se expresa en porcentaje |

$$
Error\ porcentual = \frac{|x - \tilde{x}|}{|x|} \times 100
$$

#### Idea clave

- El error absoluto dice cuánto me equivoqué en valor puro.
- El error relativo dice qué tan grande es la falla comparada con el valor real.
- El error porcentual facilita la interpretación.

### 2.2 Errores por redondeo y truncamiento

Los errores más comunes al calcular con computadora son el redondeo y el truncamiento.

#### Error por redondeo

Ocurre cuando un número se aproxima al valor representable más cercano.

Ejemplo: $3.14159265$ redondeado a 3 decimales da $3.142$.

**Origen:** la computadora no puede representar todos los números reales con precisión infinita.

#### Error por truncamiento

Ocurre cuando se corta un número o una serie en cierto punto sin considerar los términos restantes.

Ejemplo: aproximar una serie infinita usando solo los primeros términos.

**Origen:** el método matemático se detiene antes de alcanzar la solución exacta.

#### Diferencia entre ambos

| Error | Qué hace | Causa principal |
|---|---|---|
| Redondeo | Aproxima al valor más cercano | Representación finita de la máquina |
| Truncamiento | Elimina términos o pasos del cálculo | Detención del procedimiento matemático |

#### Ejemplo breve

Si se aproxima:

$$
e^x = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots
$$

y solo se usan los tres primeros términos, aparece error de truncamiento.

Si además la computadora guarda menos cifras de las necesarias, aparece error de redondeo.

### Puntos clave para estudiar

- Error absoluto, relativo y porcentual son formas distintas de medir la diferencia.
- Redondeo viene de la representación finita de la máquina.
- Truncamiento viene de detener una aproximación antes de tiempo.
- En métodos numéricos casi siempre ambos errores están presentes.

## Quiz

### Pregunta 1: Error absoluto

**Pregunta:** ¿Qué mide el error absoluto?

**Opciones:**
- ✅ **La diferencia directa entre el valor exacto y el aproximado.**
- ❌ El porcentaje de dígitos usados por la computadora.
- ❌ La cantidad de iteraciones de un método.

**Por qué:** el error absoluto solo compara distancia numérica entre ambos valores.

### Pregunta 2: Error relativo

**Pregunta:** ¿Qué expresa el error relativo?

**Opciones:**
- ✅ **El error en relación con el valor exacto.**
- ❌ La suma de todos los errores de un algoritmo.
- ❌ El valor exacto menos el valor aproximado al cuadrado.

**Por qué:** el error relativo normaliza el error para hacerlo comparable.

### Pregunta 3: Redondeo

**Pregunta:** ¿Cuándo aparece el error por redondeo?

**Opciones:**
- ✅ **Cuando un número se aproxima al valor representable más cercano.**
- ❌ Cuando se usan demasiados términos de una serie.
- ❌ Cuando el algoritmo converge muy rápido.

**Por qué:** el redondeo surge por limitar la precisión de representación.

### Pregunta 4: Truncamiento

**Pregunta:** ¿Qué describe mejor el error de truncamiento?

**Opciones:**
- ✅ **Cortar una aproximación antes de incluir todos sus términos o pasos.**
- ❌ Redondear a dos cifras significativas.
- ❌ Convertir un entero a decimal.

**Por qué:** truncar significa detener el cálculo antes de tiempo.

## Actividades

- [ ] Calcular error absoluto, relativo y porcentual en tres ejemplos.
- [ ] Buscar un caso donde el redondeo afecte el resultado final.
- [ ] Explicar con tus palabras la diferencia entre redondeo y truncamiento.
- [ ] Resolver un ejemplo de serie truncada.


## Quiz

## Actividades

