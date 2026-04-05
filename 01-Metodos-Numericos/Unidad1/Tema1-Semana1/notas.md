# 01-Metodos-Numericos - U1 T1 S1

## Objetivo de la semana
Entender qué son los métodos numéricos, por qué se usan cuando no existe una solución exacta o conviene aproximarla, y dominar las ideas básicas sobre error, precisión y exactitud para trabajar con resultados confiables.

---

## Tema 1: Introducción a los métodos numéricos

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

### Palabras clave de 1.1
- Aproximación
- Iteración
- Solución numérica
- Problema no lineal
- Computación

---

### 1.2 Error, precisión y exactitud

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

**Idea importante para estudiar:**
Un resultado puede ser muy preciso pero no exacto si todos los valores están juntos, pero lejos del valor real.

**Cifras significativas:**
- Indican cuánta confianza hay en un número.
- Ayudan a expresar resultados con el nivel correcto de detalle.
- Evitan dar una falsa sensación de exactitud.

**Criterio práctico para la clase:**
Si el error disminuye, la aproximación mejora; pero hay que revisar si el costo computacional también aumenta.

### Palabras clave de 1.2
- Error absoluto
- Error relativo
- Redondeo
- Truncamiento
- Cifras significativas
- Precisión
- Exactitud

---

## Resumen para estudiar

1. Los métodos numéricos sirven para obtener soluciones aproximadas.
2. Su uso es indispensable cuando la solución exacta no existe o no conviene usarla.
3. Todo método numérico introduce error.
4. Los errores principales son de truncamiento, redondeo y acumulación.
5. Precisión y exactitud no significan lo mismo.
6. El objetivo no es solo calcular, sino controlar la calidad de la aproximación.

---

## Preguntas rápidas de repaso

1. ¿Por qué se usan métodos numéricos en lugar de métodos exactos?
2. ¿Cuál es la diferencia entre error absoluto y error relativo?
3. ¿Qué diferencia hay entre precisión y exactitud?
4. ¿Cómo se produce el error de redondeo?
5. ¿Por qué el análisis de error es tan importante en métodos numéricos?

---

## Estrategia de estudio

### Antes de la clase
- [ ] Lee y memoriza la definición de método numérico.
- [ ] Aprende las fórmulas de error absoluto, relativo y porcentual.
- [ ] Distingue precisión de exactitud con un ejemplo propio.

### Durante la clase
- [ ] Anota ejemplos que use el docente para truncamiento y redondeo.
- [ ] Pregunta cómo se decide si una aproximación es aceptable.
- [ ] Identifica qué criterio de error pide el profesor.

### Después de la clase
- [ ] Resume 1.1 y 1.2 con tus palabras.
- [ ] Resuelve al menos un ejercicio de error absoluto y relativo.
- [ ] Repite las definiciones hasta poder explicarlas sin mirar.

---

## Quiz

## Actividades

