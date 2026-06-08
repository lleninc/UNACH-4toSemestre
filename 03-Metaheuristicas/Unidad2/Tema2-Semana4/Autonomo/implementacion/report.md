# Informe: Implementación y evaluación — Algoritmos de trayectoria (TSP)

Problema: Traveling Salesman Problem (8 nodos) — instanciado aleatoriamente (seed=42).

Resultados (resumen):

| Algoritmo | Runs | Mejor costo | Costo medio | Tiempo medio (s) | Iteraciones media |
|---|---:|---:|---:|---:|---:|
| Simulated Annealing | 5 | 253.2775 | 253.2775 | 0.0219 | 4594.0 |
| Tabu Search | 5 | 253.2775 | 253.2775 | 0.1946 | 2000.0 |

Archivo de datos: `results_experiments.csv` (contiene coste, tiempo y iteraciones por corrida).

**Análisis comparativo**

A continuación se presenta un análisis comparativo entre los algoritmos más relevantes para el problema TSP, tomando como referencia los resultados obtenidos (SA y TS) y un contexto general con métodos comunes (Nearest Neighbor, 2-opt, Genetic Algorithm).

| Algoritmo | Precisión (calidad) | Eficiencia (tiempo/recursos) | Robustez (consistencia/ajuste de parámetros) |
|---|---:|---:|---:|
| Simulated Annealing (SA) | Alta — buena capacidad para escapar de mínimos locales | Alta — bajo coste por iteración, requiere más iteraciones | Media — sensible a temperatura y programación de enfriamiento |
| Tabu Search (TS) | Alta — intensificación local efectiva | Media-Baja — costo por iteración mayor si se examina todo el vecindario | Alta — estable si se ajusta la tenencia tabú y el vecindario |
| Nearest Neighbor (heurística golosa) | Baja-Media — rápida pero suele quedar lejos del óptimo | Muy alta — extremadamente rápido | Baja — depende fuertemente del nodo inicial |
| 2-opt (mejora local) | Media-Alta — mejora sustancial sobre heurísticas golosas | Alta — operaciones baratas por intercambio local | Media — puede quedarse en óptimos locales sin estrategia global |
| Genetic Algorithm (GA) | Variable-Alta — buena exploración con operadores adecuados | Media-Baja — coste adicional por población y operadores | Media — requiere ajuste de población, crossover y mutación |

Análisis de diferencias (precisión, eficiencia, robustez):

- Precisión: métodos que combinan búsqueda global y mejora local (por ejemplo GA con 2-opt, o SA con enfriamiento lento) tienden a producir mejores soluciones para instancias pequeñas y medianas. En nuestros experimentos SA y TS alcanzaron la misma mejor solución observada, lo que confirma que ambos pueden lograr alta precisión si están bien parametrizados.
- Eficiencia: SA mostró menor tiempo total en esta implementación porque cada iteración es muy barata; TS consumió más tiempo debido a la evaluación más amplia del vecindario. Heurísticas simples (Nearest Neighbor) son extremadamente rápidas pero sacrifican calidad.
- Robustez: TS puede ofrecer comportamientos más predecibles cuando la tenencia tabú y el esquema de vecindario están bien definidos; SA necesita cuidado en la selección de temperatura inicial y tasa de enfriamiento para evitar tanto convergencia prematura como exploración excesiva.

Recomendaciones prácticas:

- Para prototipos rápidos y restricciones de tiempo usar Nearest Neighbor + 2-opt como pipeline: la heurística inicial es veloz y 2-opt mejora la calidad con bajo coste.
- Para búsqueda de soluciones de mayor calidad usar SA o TS con evaluaciones delta (two‑opt delta) para reducir coste por iteración.
- Para problemas reales grandes considerar metaheurísticas híbridas (GA+local search, ACO con intensificación) y automatizar la búsqueda de hiperparámetros.

**Reflexión crítica (≈300 palabras)**

Los algoritmos de trayectoria y las metaheurísticas aplicadas al TSP tienen una relevancia directa en problemas reales de logística, robótica y planificación de recursos, porque ofrecen un equilibrio práctico entre calidad de solución y coste computacional. En logística, por ejemplo, rutas de reparto y recolección requieren soluciones cercanas al óptimo en tiempos limitados: aquí, una combinación de heurística inicial (Nearest Neighbor) seguida de una mejora local (2-opt/3-opt) puede proporcionar rutas útiles en segundos, mientras que métodos más costosos (GA, ACO, TS) pueden reservarse para windows de optimización nocturna o planificación estratégica donde el tiempo no es tan crítico.

En robótica la planificación de trayectorias tiene además restricciones geométricas y dinámicas (obstáculos, cinemática del robot) que convierten el problema en variantes del TSP o en problemas de ruteo con restricciones. Las metaheurísticas son valiosas porque permiten incorporar restricciones adicionales en la evaluación de soluciones y explorar espacios de alta dimensionalidad donde métodos exactos no son prácticos. Sin embargo, en entornos con fuerte requerimiento en tiempo real, es común usar políticas híbridas: planificador rápido para emergencia y optimizador off-line para refinar trayectorias.

En planificación de recursos (asignación de tareas, secuenciación de máquinas), la robustez y la consistencia son tan importantes como la calidad puntual de la solución; aquí, TS puede ser preferible por su capacidad para intensificar y diversificar controladamente, mientras que SA o GA aportan flexibilidad para escapar de mínimos locales en espacios complejos.

Finalmente, la aplicabilidad práctica exige más que un buen algoritmo: requiere modelado realista, evaluaciones delta para eficiencia, validación con datos reales y pipelines automatizados para ajuste de parámetros. Las decisiones entre velocidad y calidad, la tolerancia a subóptimos y la necesidad de explicabilidad condicionan la elección del método en cada dominio. En resumen, las metaheurísticas aportan herramientas potentes y flexibles, pero su éxito en la práctica depende tanto de su implementación eficiente como de una integración cuidadosa con las restricciones y procesos operativos del problema a resolver.
