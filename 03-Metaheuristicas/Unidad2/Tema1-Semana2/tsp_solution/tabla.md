# Tabla de resultados TSP

Resumen de 3 corridas por algoritmo sobre la instancia de 6 ciudades usada en `actividad_tsp_metaheuristicas.py`.

| Algoritmo | Calidad de la solución (distancia) | Tiempo de ejecución promedio | Variabilidad del tiempo (desv. est.) | Número de iteraciones | Variabilidad de resultados (desv. est. de la distancia) |
|---|---:|---:|---:|---:|---:|
| PSO | 32.1825 | 0.2638 s | 0.0341 s | 100 | 0.0000 |
| GA  | 32.1825 | 0.9367 s | 0.3058 s | 100 | 0.0000 |
| SA  | 32.1825 | 0.0350 s | 0.0102 s | 2000 | 0.0000 |
| TS  | 32.1825 | 0.9082 s | 0.1618 s | 1000 | 0.0000 |

## Observación

En esta instancia pequeña del TSP, los cuatro algoritmos alcanzaron la misma mejor distancia en las corridas evaluadas, por lo que la variabilidad de la calidad fue nula. La diferencia principal aparece en el tiempo de ejecución y en el número de iteraciones requeridas por cada técnica.

## Ventajas y desventajas por tipo de algoritmo

| Tipo de algoritmo | Ventajas | Desventajas |
|---|---|---|
| Bioinspirados (PSO y GA) | Son flexibles, fáciles de adaptar a otros problemas de optimización y suelen explorar mejor el espacio de búsqueda gracias a la cooperación entre soluciones. | Pueden requerir ajuste de parámetros y, en algunos casos, tardan más en estabilizarse o converger que los métodos de trayectoria. |
| De trayectoria (SA y TS) | Suelen ser más simples de implementar, trabajan bien con soluciones vecinas y pueden dar resultados muy buenos en problemas combinatorios como TSP. | Pueden quedar atrapados en óptimos locales o depender mucho de la solución inicial y de la estrategia de vecindad. |

## Ensayo: adaptación a distintos contextos

La elección del tipo de algoritmo depende mucho del contexto del problema y de las restricciones operativas. En logística, por ejemplo, suelen aparecer problemas de rutas de reparto, diseño de recorridos, asignación de vehículos y programación de entregas. En este tipo de escenarios, los algoritmos de trayectoria como SA y TS resultan atractivos cuando se necesita una solución rápida y razonable sobre una ruta concreta, porque exploran vecindarios cercanos y pueden mejorar de forma progresiva una propuesta inicial. Sin embargo, cuando el problema es más amplio, con muchas rutas posibles, múltiples depósitos o restricciones dinámicas, los algoritmos bioinspirados como PSO y GA suelen adaptarse mejor porque exploran más el espacio de búsqueda y pueden manejar mejor la diversidad de soluciones. Para logística de escala media o grande, un GA bien ajustado suele ser especialmente útil por su capacidad de combinar rutas parciales prometedoras y conservar diversidad poblacional.

En robótica, la situación cambia un poco. Si el objetivo es planificar trayectorias, evitar obstáculos o reconfigurar movimientos en tiempo real, los métodos de trayectoria tienen una ventaja importante: trabajan de forma iterativa sobre soluciones vecinas y pueden integrarse con facilidad a planes locales. SA puede ser útil para refinar trayectorias, mientras que TS puede evitar que el robot vuelva a rutas ya exploradas. Aun así, en robótica móvil o en navegación con múltiples objetivos, los bioinspirados pueden ser más robustos cuando se requiere buscar entre muchas alternativas simultáneamente. PSO es especialmente interesante cuando se necesita coordinación de múltiples agentes o ajuste continuo de parámetros, porque su lógica de “enjambre” se adapta bien a espacios de búsqueda complejos.

En asignación de recursos, como distribución de personal, selección de tareas o planificación de producción, los algoritmos bioinspirados suelen destacar. GA es muy apropiado para problemas con muchas combinaciones discretas, porque permite recombinar buenas soluciones y conservar las mejores mediante elitismo. PSO también puede ser útil cuando la asignación puede representarse de manera continua o híbrida. Por otro lado, SA y TS funcionan bien si existe una solución inicial sólida y se desea mejorarla con rapidez, pero pueden ser menos eficaces si el espacio de búsqueda es muy grande o si las restricciones son altamente cambiantes.

En conclusión, no existe un algoritmo universalmente mejor. Para logística, GA y TS suelen ofrecer un buen balance entre calidad y practicidad; para robótica, SA y TS son útiles en refinamiento local, mientras que PSO puede destacar en escenarios cooperativos o dinámicos; y para asignación de recursos, GA suele ser la opción más sólida por su flexibilidad. La decisión final debe considerar el tamaño del problema, el tiempo disponible y si se prioriza exploración global o ajuste local.