# 01-Metodos-Numericos - U1 T2 S4

## Notas de clase

### 2. Tema 2: Control del error y comportamiento de los métodos numéricos

Esta semana se estudia cómo los errores se transmiten en los cálculos y por qué algunos métodos son más confiables que otros.

### 2.3 Propagación de errores

La propagación de errores ocurre cuando un error pequeño en los datos de entrada se amplifica o se modifica durante las operaciones matemáticas.

#### Idea general

Si un dato inicial tiene error, cada operación posterior puede conservarlo, reducirlo o amplificarlo.

#### Operaciones simples

Si $z = x + y$ o $z = x - y$, el error absoluto de la salida puede crecer con la suma de los errores de entrada.

Si $z = x \cdot y$ o $z = x / y$, el error relativo suele ser más útil para analizar el efecto.

#### Intuición práctica

- En sumas y restas, importa el error absoluto.
- En productos y cocientes, importa mucho el error relativo.
- Si dos números muy parecidos se restan, puede ocurrir cancelación catastrófica.

#### Cancelación catastrófica

Sucede cuando se restan números casi iguales y se pierde mucha información significativa.

Ejemplo conceptual:

$$
1.000001 - 1.000000 = 0.000001
$$

Si se redondea demasiado, el resultado puede perder precisión.

### 2.4 Estabilidad, condicionamiento y convergencia

Estos tres conceptos ayudan a decidir si un método numérico realmente conviene usar.

#### Estabilidad

Un método es estable si los errores de redondeo o perturbaciones pequeñas no crecen de forma descontrolada durante el proceso.

**Idea práctica:** un método estable “tolera” pequeñas perturbaciones.

#### Condicionamiento

El condicionamiento describe qué tan sensible es un problema a cambios pequeños en los datos de entrada.

- **Problema bien condicionado:** pequeñas variaciones en la entrada producen pequeñas variaciones en la salida.
- **Problema mal condicionado:** pequeñas variaciones en la entrada producen cambios grandes en la salida.

**Importante:** el condicionamiento depende del problema, no del algoritmo.

#### Convergencia

Un método converge cuando sus aproximaciones se acercan al valor exacto conforme se repite el proceso.

#### Comparación rápida

| Concepto | Se refiere a | Pregunta clave |
|---|---|---|
| Estabilidad | Algoritmo | ¿El método controla bien los errores intermedios? |
| Condicionamiento | Problema | ¿El problema amplifica perturbaciones? |
| Convergencia | Proceso iterativo | ¿Las aproximaciones se acercan a la solución? |

#### Relación entre los tres

- Un problema mal condicionado puede ser difícil incluso con un método estable.
- Un método inestable puede arruinar un problema que sí estaba bien condicionado.
- La convergencia indica si el método está progresando hacia la solución.

### Puntos que suelen preguntar en quiz

- La propagación de errores muestra cómo un error inicial afecta el resultado final.
- Cancelación catastrófica aparece al restar números muy cercanos.
- Estabilidad es propiedad del algoritmo.
- Condicionamiento es propiedad del problema.
- Convergencia describe el comportamiento de una sucesión de aproximaciones.

## Quiz

### Pregunta 1: Propagación de errores

**Pregunta:** ¿Qué es la propagación de errores?

**Opciones:**
- ✅ **El proceso por el cual errores pequeños en la entrada afectan resultados posteriores.**
- ❌ La forma en que una calculadora imprime decimales.
- ❌ El número de iteraciones necesarias para graficar una función.

**Por qué:** los errores no desaparecen; pueden cambiar de tamaño a lo largo del cálculo.

### Pregunta 2: Cancelación catastrófica

**Pregunta:** ¿Cuándo ocurre la cancelación catastrófica?

**Opciones:**
- ✅ **Cuando se restan números casi iguales y se pierde precisión.**
- ❌ Cuando se suman dos números muy grandes.
- ❌ Cuando un método converge muy rápido.

**Por qué:** la resta de números casi iguales elimina cifras significativas útiles.

### Pregunta 3: Estabilidad

**Pregunta:** ¿Qué significa que un método sea estable?

**Opciones:**
- ✅ **Que pequeños errores no se amplifican de manera descontrolada.**
- ❌ Que siempre produce la solución exacta.
- ❌ Que funciona solo con números enteros.

**Por qué:** la estabilidad se relaciona con el control del error durante el procedimiento.

### Pregunta 4: Condicionamiento

**Pregunta:** ¿Qué describe el condicionamiento?

**Opciones:**
- ✅ **La sensibilidad del problema ante pequeños cambios en los datos.**
- ❌ La velocidad con la que una computadora ejecuta el código.
- ❌ El orden de las iteraciones de un método.

**Por qué:** el condicionamiento pertenece al problema matemático, no al algoritmo.

### Pregunta 5: Convergencia

**Pregunta:** ¿Qué indica la convergencia?

**Opciones:**
- ✅ **Que las aproximaciones se acercan a la solución real.**
- ❌ Que el resultado final siempre será exacto.
- ❌ Que el método usa redondeo interno.

**Por qué:** converger significa acercarse progresivamente al valor buscado.

## Actividades

- [ ] Dar un ejemplo de error que se propaga en una suma o producto.
- [ ] Explicar la diferencia entre estabilidad y condicionamiento.
- [ ] Identificar un caso de cancelación catastrófica.
- [ ] Escribir cuándo dirías que un método converge.


## Quiz

## Actividades

