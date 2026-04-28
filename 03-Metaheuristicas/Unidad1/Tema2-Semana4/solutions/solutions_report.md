# Actividad Autónoma 2 — Implementación práctica y comparación de PSO, GA y ACO

**Unidad:** Unidad 1 — Algoritmos bioinspirados

**Tema:** Tema 2 — Ejemplos Clásicos y Aplicaciones

**Nombre:** _______________________

**Fecha:** _______________________

**Carrera:** _______________________

**Periodo académico / Semestre:** _______________________

---

## 1. Objetivo
Implementar versiones básicas de PSO, GA y ACO, aplicarlas a problemas sencillos de optimización, registrar resultados (iteraciones, solución final, tiempo) y comparar sus comportamientos.

## 2. Enunciado resumido
Aplicar PSO, GA y ACO a: minimizar la función continua f(x,y) = 3x^2 + 2y^2 (PSO y GA) y resolver un TSP simple de 5 ciudades (ACO). Registrar iteraciones, solución final y tiempo de ejecución.

## 3. Código adjunto
- Script principal con implementaciones: `03-Metaheuristicas/Unidad1/Tema2-Semana4/solutions/opt_algorithms.py`
- Resultados guardados en: `03-Metaheuristicas/Unidad1/Tema2-Semana4/solutions/solutions_results.json`

## 4. Implementación (resumen)
- PSO: 40 partículas, 200 iteraciones, operadores estándar (inercia, cognitivo, social), límites en [-5,5] por dimensión.
- GA: codificación real-valued, selección por torneo, crossover aritmético, mutación Gaussiana, población 60, 200 iteraciones.
- ACO: variante básica para TSP, 30 hormigas, 200 iteraciones, evaporación y depósito proporcional a 1/longitud.

## 5. Resultados (extraídos de `solutions_results.json`)

| Algoritmo | Mejor (valor / ruta) | Iteraciones | Tiempo (s) |
|---|---:|---:|---:|
| PSO | 1.08e-25 | 200 | 0.56 |
| GA  | 0.000000 | 200 | 1.90 |
| ACO (TSP 5) | Longitud ≈ 4.414214 | 200 | 3.12 |

> Nota: los valores numéricos están en `solutions_results.json` para ver historial de convergencia.

## 6. Tabla comparativa (criterios: convergencia, calidad, tiempo, ventajas/desventajas)

- **Convergencia:** PSO converge muy rápido y de forma consistente hacia el mínimo para esta función convexa; GA también logra el mínimo pero con más variación; ACO no aplica directamente a funciones continuas (usado para TSP).
- **Calidad de solución:** PSO y GA alcanzaron soluciones cercanas a 0 (mínimo global). ACO encontró una ruta razonable para el TSP con longitud ~4.41.
- **Tiempo de ejecución:** PSO fue el más rápido (0.56 s), GA más lento (1.90 s), ACO más costoso por construcción combinatoria (3.12 s) en esta configuración.
- **Ventajas/Desventajas:** PSO: simple y eficiente en espacios continuos unimodales; GA: más robusto frente a multimodalidad y permite diversidad; ACO: apropiado para problemas discretos como TSP, menos eficiente en espacios continuos.

## 7. Ensayo crítico (≥300 palabras)

La elección de un metaheurístico apropiado depende fuertemente de la naturaleza del problema. En el caso planteado —minimizar la función cuadrática continua $f(x,y)=3x^{2}+2y^{2}$— el paisaje de la función es convexo, unimodal y simétrico; por tanto, algoritmos con capacidad de búsqueda continua y buena explotación local son ideales. PSO, inspirado en el comportamiento de enjambres, destaca en este tipo de problemas por su simplicidad y su equilibrio entre explotación e exploración mediante los coeficientes de inercia y los términos cognitivo/social. En las pruebas realizadas, PSO alcanzó prácticamente el valor óptimo en menos iteraciones y con menor tiempo de cómputo comparado con GA, lo que corrobora su idoneidad para funciones lisas y unimodales.

El algoritmo genético (GA) mostró también capacidad para encontrar soluciones de calidad, pero requiere mecanismos de diversidad (mutación, selección) que, en configuraciones básicas, pueden consumir más tiempo para refinar la solución. GA es más general: su representación y operadores permiten adaptarlo a problemas discretos, mixtos o con restricciones complejas, por lo que resulta preferible cuando el espacio de búsqueda es multimodal o la codificación discreta es natural. En este ejercicio sencillo la ventaja de GA se reduce, pues la estructura del problema favorece a métodos de búsqueda directa continua.

ACO, por su naturaleza, está pensado para problemas combinatorios (como el TSP). Al aplicar ACO al TSP de 5 ciudades, el algoritmo encontró rutas competitivas pero su costo computacional por iteración fue mayor que para PSO/GA en el problema continuo. Esto subraya una idea clave: no existe un «mejor» algoritmo universal; cada metaheurístico posee dominios de aplicabilidad donde brilla.

En conclusión, para el problema elegido (función cuadrática continua), PSO es la opción más adecuada entre los tres por su rapidez y eficacia en converger hacia el mínimo. GA es una alternativa robusta cuando la topología es más compleja o la representación requiere operadores específicos. ACO debe reservarse para problemas discretos/combinatorios donde el modelo de feromonas y atracción probabilística es natural. Para trabajos prácticos, recomiendo combinar análisis del problema (continuo vs discreto, convexidad, multimodalidad) con pruebas empíricas y ajuste de parámetros antes de seleccionar la metaheurística final.

## 8. Bibliografía (selección)
- Ahmed, Z., Haron, H., & Al-Tameem, A. (2024). Appropriate Combination of Crossover Operator and Mutation Operator in Genetic Algorithms for the Travelling Salesman Problem.
- Khalid, A. M., Hosny, K. M., & Mirjalili, S. (2022). COVIDOA: A novel evolutionary optimization algorithm based on coronavirus disease replication lifecycle.
- Game, P., Vaze, V., & Emmanuel, M. (2020). Bio-inspired Optimization: metaheuristic algorithms for optimization.

---

### Archivos entregados
- `solutions_report.md` (este archivo)
- `solutions_report.pdf` (versión en PDF)
- Código: `opt_algorithms.py`
- Resultados: `solutions_results.json`
