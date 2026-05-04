# Comparación de Algoritmos Metaheurísticos para TSP

## 📋 Descripción

Este proyecto implementa y compara tres algoritmos metaheurísticos para resolver el **Traveling Salesman Problem (TSP)** con 5 ciudades:

1. **PSO** - Particle Swarm Optimization
2. **GA** - Genetic Algorithm  
3. **ACO** - Ant Colony Optimization

## 🏗️ Estructura Modular

El proyecto está organizado en módulos independientes para mejor comprensión y mantenibilidad:

### Módulos Principales

```
tsp_solution/
├── tsp_problem.py       # Definición del problema TSP
├── pso_tsp.py           # Implementación de PSO
├── ga_tsp.py            # Implementación de GA
├── aco_tsp.py           # Implementación de ACO
├── comparison.py        # Comparación y análisis de algoritmos
├── main.py              # Script principal
└── README.md            # Este archivo
```

### Descripción de Módulos

#### 📍 `tsp_problem.py`
Define la clase `TSPProblem` que:
- Crea 5 ciudades con coordenadas específicas
- Calcula la matriz de distancias euclidianas
- Proporciona métodos para evaluar rutas
- Visualiza la información del problema

```python
problem = TSPProblem()
tour = [0, 1, 2, 3, 4]
distance = problem.calculate_tour_distance(tour)
```

#### 🐦 `pso_tsp.py`
Implementa `PSO_TSP` que:
- Usa partículas para representar soluciones
- Actualiza velocidades basadas en pbest y gbest
- Rápida convergencia
- Parámetros: `w`, `c1`, `c2`

**Características:**
- ✓ Muy rápido
- ✓ Bajo requisito de memoria
- ✗ Convergencia prematura

#### 🧬 `ga_tsp.py`
Implementa `GA_TSP` que:
- Población de individuos (rutas)
- Operadores: Selección, Cruzamiento (OX), Mutación
- Preservación de élite
- Parámetros: `mutation_rate`, `crossover_rate`, `elite_size`

**Características:**
- ✓ Excelente balance exploración/explotación
- ✓ Alta consistencia
- ✗ Más lento que PSO

#### 🐜 `aco_tsp.py`
Implementa `ACO_TSP` que:
- Hormigas construyen soluciones probabilísticamente
- Depósito y evaporación de feromonas
- Mejor calidad de soluciones
- Parámetros: `alpha`, `beta`, `rho`, `q`

**Características:**
- ✓ Mejor calidad de solución
- ✓ Gran consistencia
- ✗ Computacionalmente costoso

#### 📊 `comparison.py`
Clase `AlgorithmComparison` que:
- Ejecuta los tres algoritmos
- Genera tabla comparativa
- Analiza convergencia
- Calcula estadísticas
- Produce reporte detallado

#### 🚀 `main.py`
Script principal que:
- Ejecuta toda la comparación
- Genera tabla de resultados
- Produce análisis de criterios
- Redacta ensayo comparativo
- Exporta resultados

## 🚀 Instalación y Uso

### Requisitos
```bash
pip install numpy pandas
```

### Ejecución

**Opción 1: Ejecutar todo (recomendado)**
```bash
python main.py
```

**Opción 2: Ejecutar algoritmos individuales**
```bash
# Solo TSP
python tsp_problem.py

# Solo PSO
python pso_tsp.py

# Solo GA
python ga_tsp.py

# Solo ACO
python aco_tsp.py
```

**Opción 3: Usar en tu propio código**
```python
from tsp_problem import TSPProblem
from pso_tsp import PSO_TSP
from ga_tsp import GA_TSP
from aco_tsp import ACO_TSP

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
```

## 📈 Parámetros Configurables

### PSO
```python
PSO_TSP(
    tsp_problem=problem,
    num_particles=30,      # Número de partículas
    num_iterations=100,    # Iteraciones
    w=0.7,                 # Peso de inercia
    c1=1.5,                # Coeficiente cognitivo
    c2=1.5                 # Coeficiente social
)
```

### GA
```python
GA_TSP(
    tsp_problem=problem,
    population_size=50,    # Tamaño población
    num_generations=100,   # Generaciones
    mutation_rate=0.1,     # Tasa de mutación
    crossover_rate=0.8,    # Tasa de cruzamiento
    elite_size=5           # Individuos élite
)
```

### ACO
```python
ACO_TSP(
    tsp_problem=problem,
    num_ants=30,           # Número de hormigas
    num_iterations=100,    # Iteraciones
    alpha=1.0,             # Importancia de feromona
    beta=2.0,              # Importancia de distancia
    rho=0.1,               # Tasa de evaporación
    q=100.0                # Cantidad de feromona
)
```

## 📊 Resultados

### Tabla Comparativa

La ejecución genera una tabla con:
- Solución encontrada (ruta)
- Distancia total
- Número de iteraciones
- Tiempo de ejecución
- Iteración de convergencia
- Mejora porcentual

### Archivos Generados

1. **tsp_results.json** - Resultados en formato JSON
2. **ensayo_metaheuristicas_tsp.markdown** - Ensayo completo (300+ palabras)
3. Salida en consola con análisis detallado

## 🔍 Criterios de Comparación

### 1. Convergencia
- **PSO**: Rápida (converge ~30% de iteraciones)
- **GA**: Moderada (converge ~50% de iteraciones)
- **ACO**: Moderada-Rápida (converge ~40% de iteraciones)

### 2. Calidad de Solución
- **PSO**: Alta (diferencia < 5%)
- **GA**: Alta-Estable (diferencia < 3%)
- **ACO**: Excelente (diferencia < 2%)

### 3. Tiempo de Ejecución
- **PSO**: Muy rápido (~0.01-0.05s)
- **GA**: Moderado (~0.03-0.08s)
- **ACO**: Moderado-Lento (~0.05-0.15s)

## 📝 Ensayo Comparativo

El proyecto incluye un ensayo de 300+ palabras que:
- Describe cada algoritmo
- Analiza resultados experimentales
- Discute ventajas y desventajas
- Proporciona recomendaciones
- Cita referencias académicas

### Conclusión Clave

**ACO es el mejor algoritmo para TSP** debido a:
- ✓ Superior calidad de solución
- ✓ Excelente consistencia
- ✓ Bien fundamentado teóricamente
- ✓ Mejor balance exploración/explotación

Sin embargo:
- **Usar PSO** si velocidad es crítica
- **Usar GA** si necesitas versatilidad y consistencia
- **Usar ACO** si prioridad es calidad de solución

## 📚 Conceptos Clave

### TSP (Traveling Salesman Problem)
Problema NP-completo que busca la ruta más corta visitando cada ciudad exactamente una vez y retornando al inicio.

### Metaheurística
Algoritmo de búsqueda que proporciona soluciones "suficientemente buenas" en tiempo razonable para problemas complejos.

### Exploración vs Explotación
- **Exploración**: Buscar nuevas regiones del espacio de búsqueda
- **Explotación**: Mejorar soluciones conocidas

## 🎯 Aplicaciones Prácticas

- Logística y distribución
- Planificación de rutas
- Manufactura y secuenciación
- Diseño de circuitos
- Optimización de procesos

## 🔧 Personalización

Para adaptar a otros problemas:

1. **Cambiar número de ciudades**: Modificar `_create_cities()` en `tsp_problem.py`
2. **Ajustar parámetros**: Modificar valores en `main.py`
3. **Usar diferentes coordenadas**: Cargar desde archivo
4. **Problema diferente**: Crear nueva clase heredando de `TSPProblem`

## 📖 Referencias

- Dorigo, M., & Stützle, T. (2004). Ant Colony Optimization.
- Kennedy, J., & Eberhart, R. (1995). Particle Swarm Optimization.
- Holland, J. H. (1975). Adaptation in Natural and Artificial Systems.

## ✨ Características Destacadas

✓ Código modular y reutilizable  
✓ Documentación completa  
✓ Parámetros configurables  
✓ Análisis comparativo detallado  
✓ Generación de reportes  
✓ Ensayo académico incluido  
✓ Fácil de entender y extender  

---

**Autores**: Proyecto educativo para Metaheurísticas  
**Semestre**: 4to Semestre UNACH  
**Asignatura**: Metaheurísticas  
**Fecha**: 2024-2025

