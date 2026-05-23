# Autonomo 3 — Metaheurísticas: Simulated Annealing vs Tabu Search

## Resumen

Implementé versiones básicas de Simulated Annealing (SA) y Tabu Search (TS) en Python y preparé un script para ejecutar experimentos sobre dos problemas: la función Sphere (dim=5) y un TSP reducido (5 ciudades). El script `run_experiments.py` ejecuta varios ensayos y guarda los resultados en `results_autonomo3.csv`.

## Tabla comparativa

| Problema | Algoritmo | Iteraciones promedio | Tiempo promedio (s) | Mejor valor promedio | Comentarios |
|---|---:|---:|---:|---:|---|
| Sphere5 | SA | 1240.8 | 0.0121 | 0.1176 | Mejoró de forma gradual; sensible a la temperatura inicial |
| Sphere5 | TS | 480.8 | 2.9944 | 0.000016 | Muy robusto en este caso y más estable para el continuo simple |
| TSP5 | SA | 278.0 | 0.0052 | 15.7585 | Convergió rápido, pero quedó atrapado en el mismo costo |
| TSP5 | TS | 211.8 | 1.2206 | 15.7585 | Desempeño estable; útil para problemas combinatorios |

Los valores corresponden al promedio de 5 corridas guardadas en `results_autonomo3.csv`.

## Análisis comparativo (criterios)

- Eficiencia: medir tiempos de ejecución promedio por algoritmo y problema.
- Calidad de la solución: comparar el mejor valor obtenido en varias corridas.
- Robustez: variación (desviación estándar) entre corridas.
- Facilidad de implementación: comentario cualitativo sobre complejidad de código.

## Ensayo crítico (SA vs TS)

Simulated Annealing (SA) y Tabu Search (TS) son dos técnicas metaheurísticas con enfoques conceptualmente diferentes para abordar problemas de optimización. SA se inspira en el proceso físico de enfriamiento, permitiendo aceptar soluciones peores con cierta probabilidad controlada por una temperatura que decrece. Esta propiedad hace que SA sea capaz de escapar de óptimos locales durante las primeras iteraciones, ya que la probabilidad de aceptar peores soluciones es más alta con temperaturas elevadas. A medida que la temperatura disminuye, la búsqueda se vuelve más explotadora. Una ventaja de SA es su simplicidad: la implementación básica requiere un generador de vecinos y una función de aceptación basada en temperatura, lo que facilita adaptarlo a problemas continuos y combinatorios. Sin embargo, SA depende fuertemente de la programación de la temperatura (T0, alfa) y puede necesitar muchos parámetros y tiempo para converger a soluciones de alta calidad.

Tabu Search, por su parte, es un algoritmo de trayectoria que explora sistemáticamente el espacio de soluciones manteniendo una memoria (lista tabu) de movimientos o soluciones recientes para evitar ciclos inmediatos. TS suele trabajar bien en problemas combinatorios como el TSP, donde los movimientos discretos (por ejemplo, intercambios) pueden ser fácilmente representados y penalizados temporalmente. TS es muy efectiva para intensificación (mejorar alrededor de buenas regiones) y, con una buena gestión de la memoria y criterios de aspiración, puede encontrar soluciones de alta calidad rápidamente. Su principal limitación es la gestión de la estructura tabu y la necesidad de diseñar operadores de vecindario eficientes; además, la implementación puede ser más compleja que la de SA.

En términos de aplicación, SA es preferible cuando el espacio de búsqueda es continuo o cuando se desea una implementación sencilla y flexible, y cuando un plan de temperatura bien calibrado es factible. TS destaca en problemas combinatorios estructurados (ruteo, asignación) donde evitar ciclos y priorizar movimientos prometedores es ventajoso.

En resumen, SA ofrece simplicidad y buena capacidad para escapar de óptimos locales con el coste de sensibilidad a parámetros, mientras que TS ofrece control más directo sobre la trayectoria de búsqueda y suele rendir mejor en problemas combinatorios, a costa de una implementación y ajuste de memoria más cuidadosos.
