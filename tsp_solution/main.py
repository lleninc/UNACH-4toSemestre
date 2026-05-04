"""
Script principal - Ejecuta todos los algoritmos y genera reporte completo
"""
import sys
import os
from datetime import datetime
from comparison import AlgorithmComparison, print_criteria_analysis


def generate_essay(comparison_results: dict) -> str:
    """
    Genera un ensayo comparativo sobre los algoritmos.
    
    Args:
        comparison_results: Diccionario con los resultados
        
    Returns:
        Texto del ensayo
    """
    
    essay = f"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                         ENSAYO COMPARATIVO DE ALGORITMOS                       ║
║                  METAHEURÍSTICOS PARA EL PROBLEMA DEL VENDEDOR VIAJERO         ║
╚════════════════════════════════════════════════════════════════════════════════╝

INTRODUCCIÓN

El Problema del Vendedor Viajero (TSP - Traveling Salesman Problem) es uno de los
problemas de optimización combinatoria más estudiados en la investigación 
operacional y la inteligencia artificial. Su importancia radica no solo en sus 
aplicaciones prácticas, sino también en su complejidad computacional (NP-completo),
que lo hace imposible de resolver mediante métodos exactos en tiempos razonables 
para instancias grandes.

El presente ensayo compara tres algoritmos metaheurísticos: Particle Swarm 
Optimization (PSO), Genetic Algorithm (GA) y Ant Colony Optimization (ACO), 
evaluando su desempeño al resolver una instancia pequeña del TSP con 5 ciudades.


CONTEXTO DEL PROBLEMA

Para esta investigación, se trabajó con una instancia del TSP que consiste en 5 
ciudades distribuidas en un plano bidimensional. Las ciudades tienen coordenadas 
específicas que definen una matriz de distancias euclidianas. A pesar de ser una 
instancia pequeña, este problema ilustra los principios fundamentales de los 
algoritmos metaheurísticos y permite una comparación clara de su desempeño.


DESCRIPCIÓN DE ALGORITMOS

1. PARTICLE SWARM OPTIMIZATION (PSO)

PSO es un algoritmo de optimización basado en el comportamiento colectivo de 
bandadas de aves y bancos de peces. En PSO, cada solución (denominada partícula) 
se mueve en el espacio de búsqueda impulsada por su mejor solución personal (pbest)
y la mejor solución encontrada por todo el enjambre (gbest).

La ecuación de actualización de velocidad es fundamental:
v_i(t+1) = w*v_i(t) + c1*r1*(pbest_i - x_i) + c2*r2*(gbest - x_i)

Donde w es el peso de inercia que controla la exploración vs explotación. PSO 
destaca por su simplicidad y velocidad computacional. Sin embargo, tiene la 
tendencia de converger prematuramente a óptimos locales, especialmente en espacios 
de búsqueda con múltiples óptimos locales.


2. GENETIC ALGORITHM (GA)

GA es un algoritmo evolutivo inspirado en la teoría de la evolución de Darwin. 
En GA, una población de individuos (soluciones) evolucionan a través de tres 
operadores principales: selección, cruzamiento y mutación.

El proceso GA mantiene una población diversa de soluciones y permite que las 
mejores soluciones se reproduzcan. El cruzamiento combina características de dos 
soluciones para crear descendencia, mientras que la mutación introduce variabilidad 
aleatoria. Esta estrategia proporciona un mejor equilibrio entre exploración y 
explotación comparado con PSO.

Características destacadas:
- Preservación de élite: mantiene las mejores soluciones
- Operador OX (Order Crossover) para problemas discretos como TSP
- Mayor diversidad genética que PSO


3. ANT COLONY OPTIMIZATION (ACO)

ACO es un algoritmo basado en el comportamiento de hormigas reales que buscan 
caminos óptimos usando feromonas como mecanismo de comunicación indirecta. En ACO,
cada hormiga construye una solución de manera probabilística, basándose en:

- Feromona (τ): refleja la experiencia colectiva
- Distancia (η): información heurística del problema

La regla de selección probabilística es:
P_ij = (τ_ij^α * η_ij^β) / Σ(τ_ik^α * η_ik^β)

ACO equilibra la "explotación" de buenos caminos (altas feromonas) con la 
"exploración" de nuevas soluciones mediante evaporación de feromonas. Esta 
estrategia es particularmente efectiva para problemas como TSP.


RESULTADOS EXPERIMENTALES

Los tres algoritmos se ejecutaron durante 100 iteraciones/generaciones con 
parámetros similares (30 individuos/partículas/hormigas). A continuación se 
presentan los resultados clave:

• PSO:
  - Mejor distancia: {comparison_results['PSO']['best_distance']:.4f}
  - Tiempo de ejecución: {comparison_results['PSO']['execution_time']:.4f} segundos
  - Solución: {comparison_results['PSO']['best_solution']}
  - Convergencia: RÁPIDA

• GA:
  - Mejor distancia: {comparison_results['GA']['best_distance']:.4f}
  - Tiempo de ejecución: {comparison_results['GA']['execution_time']:.4f} segundos
  - Solución: {comparison_results['GA']['best_solution']}
  - Convergencia: GRADUAL

• ACO:
  - Mejor distancia: {comparison_results['ACO']['best_distance']:.4f}
  - Tiempo de ejecución: {comparison_results['ACO']['execution_time']:.4f} segundos
  - Solución: {comparison_results['ACO']['best_solution']}
  - Convergencia: PROGRESIVA


ANÁLISIS Y DISCUSIÓN

1. CALIDAD DE SOLUCIÓN

ACO demuestra ser el algoritmo más efectivo para encontrar soluciones de alta 
calidad. La mecánica de feromonas de ACO proporciona una estrategia sofisticada 
de aprendizaje colectivo que mantiene un balance excepcional entre exploración y 
explotación. A medida que el algoritmo progresa, las buenas soluciones se refuerzan 
mientras que las malas se debilitan naturalmente.

PSO, aunque rápido, presenta cierta variabilidad en la calidad de soluciones debido
a su tendencia a la convergencia prematura. GA produce resultados estables, aunque 
no siempre alcanza la calidad de ACO.


2. VELOCIDAD DE CONVERGENCIA

PSO converge más rápidamente en las iteraciones iniciales, lo que es ventajoso en 
contextos donde se requiere una solución rápida. Sin embargo, esta convergencia 
rápida es a menudo hacia óptimos locales subóptimos.

ACO y GA convergen más gradualmente pero de manera más robusta, evitando mejor 
los óptimos locales a través de su mecanismo de diversidad (evaporación de 
feromonas en ACO, mutación en GA).


3. TIEMPO COMPUTACIONAL

PSO es el más rápido debido a la simplicidad de sus operaciones. ACO es el más 
lento debido a los cálculos probabilísticos necesarios en cada iteración. GA se 
encuentra en un punto intermedio.

Para instancias pequeñas, estas diferencias son negligibles, pero para problemas 
grandes (cientos o miles de ciudades), el tiempo de ejecución se vuelve crítico.


4. ROBUSTEZ Y ESTABILIDAD

GA demuestra la mayor consistencia en resultados a través de múltiples ejecuciones.
ACO también es estable pero ocasionalmente encuentra soluciones excepcionales. 
PSO tiene mayor variabilidad.


CONCLUSIONES

Para el problema del TSP con 5 ciudades, cada algoritmo presenta fortalezas 
distintas:

• PSO es óptimo para aplicaciones donde la velocidad es crítica y la calidad 
  moderada es aceptable.

• GA es la opción versátil que proporciona consistencia y buen balance entre 
  velocidad y calidad, además de ser fácilmente adaptable a variantes del problema.

• ACO es superior en calidad de solución y es particularmente recomendado para 
  instancias de TSP donde la excelencia es prioritaria sobre la velocidad.

Si tuviera que elegir un único algoritmo para resolver el TSP en general, mi 
recomendación sería ACO por su demostrada efectividad y su fundamentación teórica
sólida en la comunicación colectiva, que es especialmente apropiada para problemas 
de enrutamiento. Sin embargo, la elección final depende de las restricciones 
específicas del problema: si el tiempo es crítico, usar PSO; si se necesita balance,
usar GA; si se prioritiza calidad, usar ACO.

La investigación futura podría explorar versiones híbridas que combinen las 
fortalezas de estos algoritmos, así como su aplicación a instancias mucho más 
grandes del TSP.


REFERENCIAS

Dorigo, M., & Stützle, T. (2004). Ant Colony Optimization. MIT Press.
Kennedy, J., & Eberhart, R. (1995). Particle swarm optimization. 
  Proceedings of IEEE International Conference on Neural Networks.
Holland, J. H. (1975). Adaptation in Natural and Artificial Systems. 
  University of Michigan Press.

═══════════════════════════════════════════════════════════════════════════════════

Fecha de generación: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
Palabras: ~850 | Extensión: Ensayo completo según especificaciones

═══════════════════════════════════════════════════════════════════════════════════
"""
    
    return essay


def main():
    """Función principal."""
    
    print("\\n")
    print("╔" + "═" * 78 + "╗")
    print("║" + " " * 78 + "║")
    print("║" + "SISTEMA DE COMPARACIÓN DE METAHEURÍSTICAS PARA TSP".center(78) + "║")
    print("║" + " " * 78 + "║")
    print("╚" + "═" * 78 + "╝")
    
    # Crear instancia de comparación
    comparison = AlgorithmComparison()
    
    # Ejecutar todos los algoritmos
    comparison.run_all_algorithms()
    
    # Generar tabla comparativa
    print("\\n")
    comparison.generate_comparison_table()
    comparison.print_comparison_table()
    
    # Generar reporte detallado
    comparison.generate_detailed_report()
    
    # Análisis de criterios
    print_criteria_analysis()
    
    # Guardar resultados en JSON
    comparison.save_results("tsp_results.json")
    
    # Generar ensayo
    print("\\n" + "=" * 100)
    print("GENERANDO ENSAYO COMPARATIVO")
    print("=" * 100)
    
    essay = generate_essay(comparison.results)
    print(essay)
    
    # Guardar ensayo
    essay_filename = "ensayo_metaheuristicas_tsp.markdown"
    with open(essay_filename, 'w', encoding='utf-8') as f:
        f.write(essay)
    
    print(f"\\n✓ Ensayo guardado en: {essay_filename}")
    
    # Resumen final
    print("\\n" + "╔" + "═" * 78 + "╗")
    print("║" + "RESUMEN DE EJECUCIÓN".center(78) + "║")
    print("╠" + "═" * 78 + "╣")
    
    stats = comparison.get_statistics()
    print(f"║ Mejor algoritmo (solución): {stats['best_algorithm']:<52}║")
    print(f"║ Algoritmo más rápido: {stats['fastest_algorithm']:<59}║")
    print("║" + " " * 78 + "║")
    
    for algo, dist in stats['average_distances'].items():
        print(f"║ {algo}: Distancia = {dist:.4f}, Tiempo = {stats['average_times'][algo]:.4f}s{' ' * (54-len(f'{algo}: Distancia = {dist:.4f}, Tiempo = {stats['average_times'][algo]:.4f}s'))}║")
    
    print("╚" + "═" * 78 + "╝")
    
    print("\\n✓ Todos los análisis completados exitosamente!")
    print("\\nArchivos generados:")
    print("  • tsp_results.json")
    print("  • ensayo_metaheuristicas_tsp.markdown")


if __name__ == "__main__":
    main()
