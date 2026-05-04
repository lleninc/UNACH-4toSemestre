# 🚀 Quick Start Guide - TSP Metaheurísticas

## ⚡ Inicio Rápido (5 minutos)

### 1️⃣ Ejecutar Todo
```bash
cd tsp_solution
python main.py
```

Esto ejecutará los tres algoritmos y generará todos los resultados.

### 2️⃣ Ver Resultados
```bash
# Abrir en navegador
RESULTADOS.html

# O leer en consola
type ensayo_metaheuristicas_tsp.markdown

# O ver JSON
type tsp_results.json
```

---

## 📚 Estructura del Proyecto

```
tsp_solution/
├── tsp_problem.py              # Define el problema TSP
├── pso_tsp.py                  # PSO - Particle Swarm Optimization
├── ga_tsp.py                   # GA - Genetic Algorithm
├── aco_tsp.py                  # ACO - Ant Colony Optimization
├── comparison.py               # Comparación y análisis
├── main.py                     # Script principal
│
├── README.md                   # Documentación completa
├── RESULTADOS.md               # Resumen de resultados (Markdown)
├── RESULTADOS.html             # Visualización interactiva (HTML)
├── QUICKSTART.md               # Este archivo
│
├── tsp_results.json            # Resultados en JSON
├── ensayo_metaheuristicas_tsp.markdown  # Ensayo de 300+ palabras
└── __init__.py                 # Paquete Python
```

---

## 🎯 Usar en Tu Código

### Opción 1: Importar como Módulo

```python
from tsp_solution import TSPProblem, PSO_TSP, GA_TSP, ACO_TSP

# Crear problema
problem = TSPProblem()

# Ejecutar PSO
pso = PSO_TSP(problem)
result_pso = pso.solve()

# Ejecutar GA
ga = GA_TSP(problem)
result_ga = ga.solve()

# Ejecutar ACO
aco = ACO_TSP(problem)
result_aco = aco.solve()

# Ver resultados
print(result_pso['best_distance'])
print(result_ga['best_distance'])
print(result_aco['best_distance'])
```

### Opción 2: Copiar y Adaptar

Cada módulo funciona independientemente:

```python
from pso_tsp import PSO_TSP
from tsp_problem import TSPProblem

problem = TSPProblem()
pso = PSO_TSP(problem, num_particles=50, num_iterations=200)
result = pso.solve()
```

---

## 🔧 Personalizar Parámetros

### PSO
```python
pso = PSO_TSP(
    tsp_problem=problem,
    num_particles=30,      # Más = mejor exploración pero más lento
    num_iterations=100,    # Más = más tiempo de búsqueda
    w=0.7,                 # Inercia: < 0.5 = explotación, > 0.9 = exploración
    c1=1.5,                # Coeficiente cognitivo
    c2=1.5                 # Coeficiente social
)
```

### GA
```python
ga = GA_TSP(
    tsp_problem=problem,
    population_size=50,    # Más = mejor diversidad
    num_generations=100,   # Más = más generaciones
    mutation_rate=0.1,     # Probabilidad de mutación (0-1)
    crossover_rate=0.8,    # Probabilidad de cruzamiento (0-1)
    elite_size=5           # Individuos élite a preservar
)
```

### ACO
```python
aco = ACO_TSP(
    tsp_problem=problem,
    num_ants=30,           # Número de hormigas
    num_iterations=100,    # Iteraciones
    alpha=1.0,             # Importancia de feromona (más = sigue feromonas)
    beta=2.0,              # Importancia de distancia (más = prefiere cercanas)
    rho=0.1,               # Evaporación de feromona (0-1)
    q=100.0                # Cantidad de feromona depositada
)
```

---

## 📊 Entender los Resultados

Cada `solve()` retorna un diccionario:

```python
result = {
    'algorithm': 'PSO',           # Nombre del algoritmo
    'best_solution': [1,4,2,3,0], # Mejor ruta encontrada
    'best_distance': 61.2276,     # Distancia total
    'iterations': 100,            # Número de iteraciones
    'execution_time': 0.3659,     # Tiempo en segundos
    'fitness_history': [...]      # Histórico de mejora
}
```

### Analizar Convergencia

```python
import matplotlib.pyplot as plt

# Graficar convergencia
plt.plot(result['fitness_history'])
plt.xlabel('Iteración')
plt.ylabel('Distancia')
plt.title(f"Convergencia {result['algorithm']}")
plt.show()
```

---

## ❓ FAQ

### ¿Cómo cambiar el número de ciudades?
Edita `tsp_problem.py`:
```python
def _create_cities(self) -> np.ndarray:
    cities = np.array([
        [0, 0],      # Añade o modifica ciudades aquí
        [10, 5],
        ...
    ])
```

### ¿Cómo usar diferentes coordenadas?
```python
def _create_cities(self) -> np.ndarray:
    import pandas as pd
    df = pd.read_csv('ciudades.csv')  # x, y
    return df[['x', 'y']].values
```

### ¿Por qué los resultados varían?
Los algoritmos tienen componentes aleatorios. Para reproducibilidad:
```python
import numpy as np
np.random.seed(42)

problem = TSPProblem(seed=42)
pso = PSO_TSP(problem)  # Mismo resultado cada ejecución
```

### ¿Cuál es el mejor algoritmo?
- **Velocidad:** PSO
- **Balance:** GA  
- **Calidad:** ACO

Depende de tus necesidades.

### ¿Cómo comparar algoritmos?
```python
from comparison import AlgorithmComparison

comp = AlgorithmComparison()
comp.run_all_algorithms()
comp.print_comparison_table()
stats = comp.get_statistics()
```

---

## 🎓 Conceptos Clave

### TSP (Traveling Salesman Problem)
Problema NP-completo: encontrar la ruta más corta visitando cada ciudad una sola vez.

### Metaheurística
Algoritmo que busca soluciones "suficientemente buenas" rápidamente, sin garantía de optimalidad.

### Convergencia
El momento en que el algoritmo deja de mejorar significativamente la solución.

### Exploración vs Explotación
- **Exploración:** Buscar nuevas áreas
- **Explotación:** Mejorar soluciones conocidas

---

## 🐍 Código de Ejemplo Completo

```python
#!/usr/bin/env python3
"""Ejemplo completo de comparación TSP"""

from tsp_solution import TSPProblem, PSO_TSP, GA_TSP, ACO_TSP
import time

# 1. Crear problema
print("Creando problema TSP...")
problem = TSPProblem()

# 2. Ejecutar algoritmos
print("\nEjecutando algoritmos...")

start = time.time()
pso = PSO_TSP(problem, num_particles=30, num_iterations=100)
result_pso = pso.solve()
time_pso = time.time() - start

start = time.time()
ga = GA_TSP(problem, population_size=50, num_generations=100)
result_ga = ga.solve()
time_ga = time.time() - start

start = time.time()
aco = ACO_TSP(problem, num_ants=30, num_iterations=100)
result_aco = aco.solve()
time_aco = time.time() - start

# 3. Comparar resultados
print("\n" + "="*50)
print("RESULTADOS")
print("="*50)

results = {
    'PSO': result_pso,
    'GA': result_ga,
    'ACO': result_aco
}

for algo_name, result in results.items():
    print(f"\n{algo_name}:")
    print(f"  Ruta: {result['best_solution']}")
    print(f"  Distancia: {result['best_distance']:.4f}")
    print(f"  Tiempo: {result['execution_time']:.4f}s")

# 4. Encontrar mejor
best_algo = min(results.items(), key=lambda x: x[1]['best_distance'])[0]
fastest_algo = min(results.items(), key=lambda x: x[1]['execution_time'])[0]

print(f"\n✓ Mejor solución: {best_algo}")
print(f"✓ Más rápido: {fastest_algo}")
```

---

## 📖 Más Información

- **README.md** - Documentación completa del proyecto
- **RESULTADOS.html** - Visualización interactiva en navegador
- **RESULTADOS.md** - Resumen detallado en Markdown
- **ensayo_metaheuristicas_tsp.txt** - Análisis académico completo

---

## 🤝 Contribuir

Puedes extender el proyecto:

1. **Añadir más algoritmos:** Crear `sa_tsp.py` para Simulated Annealing
2. **Mejorar visualización:** Añadir gráficos de convergencia
3. **Aumentar instancias:** TSP con 100+ ciudades
4. **Optimizar código:** Vectorización NumPy

---

## ✅ Checklist

- [x] Implementar PSO
- [x] Implementar GA
- [x] Implementar ACO
- [x] Comparación
- [x] Tabla de resultados
- [x] Ensayo académico (300+ palabras)
- [x] Documentación
- [x] Visualización HTML
- [x] Ejemplos de código

---

**¡Listo para usar!** 🎉

Cualquier pregunta, revisa los archivos incluidos o el código fuente.

---

*Proyecto de Metaheurísticas | UNACH - 4to Semestre*
