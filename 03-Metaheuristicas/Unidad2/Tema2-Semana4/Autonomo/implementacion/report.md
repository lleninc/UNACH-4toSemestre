# Informe: Implementación y evaluación — Algoritmos de trayectoria (TSP)

Problema: Traveling Salesman Problem (8 nodos) — instanciado aleatoriamente (seed=42).

Resultados (resumen):

| Algoritmo | Runs | Mejor costo | Costo medio | Tiempo medio (s) | Iteraciones media |
|---|---:|---:|---:|---:|---:|
| Simulated Annealing | 5 | 253.2775 | 253.2775 | 0.0219 | 4594.0 |
| Tabu Search | 5 | 253.2775 | 253.2775 | 0.1946 | 2000.0 |

Archivo de datos: `results_experiments.csv` (contiene coste, tiempo y iteraciones por corrida).

Reflexión crítica (≈300 palabras):

En esta actividad se implementaron dos algoritmos de trayectoria para el TSP: Simulated Annealing (SA) y Tabu Search (TS). Ambos métodos exploraron el espacio de soluciones mediante intercambios de posiciones (swap). En las condiciones experimentales (instancia de 8 nodos y parámetros por defecto seleccionados), ambos algoritmos encontraron soluciones con el mismo coste óptimo observado (~253.28) en las repeticiones realizadas. Sin embargo, el comportamiento en tiempo y dinámica de búsqueda mostró diferencias notables.

SA es un enfoque probabilístico que permite aceptar peores soluciones con una probabilidad dependiente de una temperatura decreciente. Esto facilita escapar de mínimos locales y, con una regulación adecuada de la temperatura inicial y la tasa de enfriamiento, converge a soluciones de buena calidad. En nuestros experimentos SA requirió más iteraciones (media ≈4594) aunque el tiempo por iteración es muy bajo, resultando en un tiempo medio total pequeño (≈0.02 s). Esto indica que SA exploró ampliamente el espacio manteniendo operaciones baratas por paso.

TS, por su parte, realiza una búsqueda determinista guiada por una lista tabú que evita volver a movimientos recientes. TS tiende a intensificar la búsqueda alrededor de soluciones prometedoras, pero en nuestra implementación la evaluación exhaustiva del vecindario en cada iteración (calcular coste para todos los swaps) incrementó el coste computacional por iteración, traduciéndose en mayor tiempo medio (≈0.19 s) pese a limitar las iteraciones a 2000. En problemas de mayor tamaño sería crucial optimizar la evaluación incremental de costes y/o reducir el tamaño del vecindario considerado.

Conclusión: Para instancias pequeñas ambos algoritmos pueden ofrecer soluciones comparables en calidad; SA mostró una relación tiempo-calidad más favorable en esta implementación simple. Para escalabilidad y uso práctico conviene: (1) implementar evaluaciones delta para swaps/two-opt para reducir coste por iteración, (2) diseñar criterios adaptativos de parada, y (3) ajustar parámetros (temperatura, tenencia tabú) mediante búsqueda de hiperparámetros. En aplicaciones reales (logística, robótica) la elección dependerá de la necesidad de soluciones rápidas frente a la calidad óptima y de la complejidad del modelo de vecindario.
