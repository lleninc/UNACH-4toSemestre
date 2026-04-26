# Actividad Autónoma 2

## Errores, condicionamiento y convergencia

**Asignatura:** Métodos Numéricos y Problemas Complejos  
**Unidad:** 1. Fundamentos y errores en el cálculo numérico  
**Tema:** 2. Errores en los métodos numéricos  
**Carrera:** Ciencia de Datos

## Introducción

En el cálculo numérico, los resultados aproximados casi nunca coinciden exactamente con el valor real. Por eso es importante medir la diferencia entre ambos mediante el error absoluto, el error relativo y el error porcentual. Estos indicadores permiten evaluar la precisión de una aproximación y comparar distintos resultados.

## Desarrollo

### 1. Cálculo de errores con π

Dado el valor real de $\pi = 3.1416$ y la aproximación $3.14$:

- Error absoluto:

$$
E_a = |3.1416 - 3.14| = 0.0016
$$

- Error relativo:

$$
E_r = \frac{0.0016}{3.1416} \approx 0.000509
$$

- Error porcentual:

$$
E_p = 0.000509 \times 100 \approx 0.050929\%
$$

**Interpretación:** la aproximación es bastante cercana al valor real, ya que el error es muy pequeño.

---

### 2. Cálculo de errores en la gravedad

Dado el valor teórico $9.81$ y el valor experimental $9.78$:

- Error absoluto:

$$
E_a = |9.81 - 9.78| = 0.03
$$

- Error relativo:

$$
E_r = \frac{0.03}{9.81} \approx 0.003058
$$

- Error porcentual:

$$
E_p = 0.003058 \times 100 \approx 0.305810\%
$$

**Interpretación:** el error es pequeño, pero suficiente para notar una diferencia entre el valor teórico y el medido.

---

### 3. Redondeo y truncamiento

Dado el número real $5.67891$, se pide redondear y truncar a 3 cifras significativas.

- Redondeo a 3 cifras significativas: $5.68$
- Truncamiento a 3 cifras significativas: $5.67$

#### Error del redondeo

$$
E_a = |5.67891 - 5.68| = 0.00109
$$

#### Error del truncamiento

$$
E_a = |5.67891 - 5.67| = 0.00891
$$

**Conclusión:** el redondeo genera menor error que el truncamiento, por lo tanto es más preciso.

---

### 4. Medición de la gravedad por tres equipos

Valor real: $g = 9.81\,m/s^2$

#### Equipo 1: $9.77$

- Error absoluto:

$$
E_a = |9.81 - 9.77| = 0.04
$$

- Error relativo:

$$
E_r = \frac{0.04}{9.81} \approx 0.004077
$$

- Error porcentual:

$$
E_p = 0.004077 \times 100 \approx 0.407747\%
$$

#### Equipo 2: $9.82$

- Error absoluto:

$$
E_a = |9.81 - 9.82| = 0.01
$$

- Error relativo:

$$
E_r = \frac{0.01}{9.81} \approx 0.001019
$$

- Error porcentual:

$$
E_p = 0.001019 \times 100 \approx 0.101937\%
$$

#### Equipo 3: $9.79$

- Error absoluto:

$$
E_a = |9.81 - 9.79| = 0.02
$$

- Error relativo:

$$
E_r = \frac{0.02}{9.81} \approx 0.002039
$$

- Error porcentual:

$$
E_p = 0.002039 \times 100 \approx 0.203874\%
$$

**Conclusión:** el Equipo 2 es el más exacto, porque presenta el menor error absoluto y porcentual.

---

### 5. Medición de la constante de Planck

Valor real:

$$
h = 6.626 \times 10^{-34}\,J\cdot s
$$

#### Grupo 1: $6.610 \times 10^{-34}$

- Error absoluto:

$$
E_a = |6.626 \times 10^{-34} - 6.610 \times 10^{-34}| = 1.6 \times 10^{-36}
$$

- Error relativo:

$$
E_r = \frac{1.6 \times 10^{-36}}{6.626 \times 10^{-34}} \approx 0.002415
$$

- Error porcentual:

$$
E_p = 0.002415 \times 100 \approx 0.241473\%
$$

#### Grupo 2: $6.635 \times 10^{-34}$

- Error absoluto:

$$
E_a = |6.626 \times 10^{-34} - 6.635 \times 10^{-34}| = 9.0 \times 10^{-37}
$$

- Error relativo:

$$
E_r = \frac{9.0 \times 10^{-37}}{6.626 \times 10^{-34}} \approx 0.001358
$$

- Error porcentual:

$$
E_p = 0.001358 \times 100 \approx 0.135829\%
$$

#### Grupo 3: $6.598 \times 10^{-34}$

- Error absoluto:

$$
E_a = |6.626 \times 10^{-34} - 6.598 \times 10^{-34}| = 2.8 \times 10^{-36}
$$

- Error relativo:

$$
E_r = \frac{2.8 \times 10^{-36}}{6.626 \times 10^{-34}} \approx 0.004226
$$

- Error porcentual:

$$
E_p = 0.004226 \times 100 \approx 0.422578\%
$$

**Conclusión:** el Grupo 2 es el más exacto, ya que presenta el menor error.

## Conclusión general

El estudio de errores es esencial en los métodos numéricos porque permite evaluar la calidad de una aproximación. El error absoluto muestra la diferencia directa con el valor real, mientras que el error relativo y el error porcentual ayudan a interpretar esa diferencia en relación con la magnitud del valor. Además, el redondeo suele ser más preciso que el truncamiento.

## Resumen final de resultados

- $\pi$: error absoluto $0.0016$, error relativo $0.000509$, error porcentual $0.050929\%$
- Gravedad: error absoluto $0.03$, error relativo $0.003058$, error porcentual $0.305810\%$
- Redondeo de $5.67891$: error absoluto $0.00109$
- Truncamiento de $5.67891$: error absoluto $0.00891$
- Equipo más exacto en gravedad: Equipo 2
- Grupo más exacto en Planck: Grupo 2
