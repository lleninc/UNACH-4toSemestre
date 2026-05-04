"""
Módulo GA - Genetic Algorithm para TSP
"""
import numpy as np
from typing import List, Tuple, Dict
import time
from tsp_problem import TSPProblem


class GA_TSP:
    """
    Implementación de Algoritmo Genético para resolver el TSP.
    
    En GA, cada individuo representa una solución (una ruta), y se evolucionan
    a través de selección, cruzamiento y mutación.
    """
    
    def __init__(
        self,
        tsp_problem: TSPProblem,
        population_size: int = 50,
        num_generations: int = 100,
        mutation_rate: float = 0.1,
        crossover_rate: float = 0.8,
        elite_size: int = 5
    ):
        """
        Inicializa GA para TSP.
        
        Args:
            tsp_problem: Instancia del problema TSP
            population_size: Tamaño de la población
            num_generations: Número de generaciones
            mutation_rate: Tasa de mutación
            crossover_rate: Tasa de cruzamiento
            elite_size: Número de individuos élite a preservar
        """
        self.problem = tsp_problem
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        
        self.num_cities = tsp_problem.get_num_cities()
        self.population = []
        self.fitness = []
        
        self.best_individual = None
        self.best_fitness = float('inf')
        
        self.fitness_history = []
        self.execution_time = 0
    
    def _initialize_population(self):
        """Inicializa la población con rutas aleatorias."""
        self.population = []
        self.fitness = []
        
        for _ in range(self.population_size):
            tour = np.random.permutation(self.num_cities)
            self.population.append(tour.copy())
            
            distance = self.problem.calculate_tour_distance(tour)
            self.fitness.append(distance)
            
            # Actualizar mejor individual
            if distance < self.best_fitness:
                self.best_fitness = distance
                self.best_individual = tour.copy()
    
    def _calculate_fitness(self, tour: np.ndarray) -> float:
        """
        Calcula la distancia de una ruta.
        
        Args:
            tour: Ruta
            
        Returns:
            Distancia total
        """
        return self.problem.calculate_tour_distance(tour)
    
    def _selection(self) -> List[np.ndarray]:
        """
        Selecciona individuos para reproducción usando selección por torneo.
        
        Returns:
            Lista de individuos seleccionados
        """
        selected = []
        tournament_size = 3
        
        for _ in range(self.population_size):
            # Torneo
            indices = np.random.choice(
                self.population_size,
                tournament_size,
                replace=False
            )
            
            # Seleccionar el mejor del torneo
            best_idx = indices[0]
            for idx in indices[1:]:
                if self.fitness[idx] < self.fitness[best_idx]:
                    best_idx = idx
            
            selected.append(self.population[best_idx].copy())
        
        return selected
    
    def _crossover(self, parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Realiza cruzamiento OX (Order Crossover).
        
        Args:
            parent1: Primer padre
            parent2: Segundo padre
            
        Returns:
            Dos hijos
        """
        if np.random.random() > self.crossover_rate:
            return parent1.copy(), parent2.copy()
        
        # OX Crossover
        start = np.random.randint(0, self.num_cities - 1)
        end = np.random.randint(start + 1, self.num_cities)
        
        child1 = np.full(self.num_cities, -1)
        child2 = np.full(self.num_cities, -1)
        
        # Copiar segmento del padre
        child1[start:end] = parent1[start:end]
        child2[start:end] = parent2[start:end]
        
        # Llenar el resto
        def fill_child(child, parent, other_parent):
            pos = end
            parent_pos = end
            
            for _ in range(self.num_cities - (end - start)):
                # Encontrar elemento del otro padre que no está en child
                while other_parent[parent_pos % self.num_cities] in child:
                    parent_pos += 1
                
                child[pos % self.num_cities] = other_parent[parent_pos % self.num_cities]
                parent_pos += 1
                pos += 1
        
        fill_child(child1, parent1, parent2)
        fill_child(child2, parent2, parent1)
        
        return child1, child2
    
    def _mutate(self, tour: np.ndarray) -> np.ndarray:
        """
        Realiza mutación de intercambio (Swap Mutation).
        
        Args:
            tour: Ruta
            
        Returns:
            Ruta mutada
        """
        mutated = tour.copy()
        
        if np.random.random() < self.mutation_rate:
            # Intercambiar dos ciudades aleatorias
            i, j = np.random.choice(self.num_cities, 2, replace=False)
            mutated[i], mutated[j] = mutated[j], mutated[i]
        
        return mutated
    
    def solve(self) -> Dict:
        """
        Ejecuta el algoritmo genético.
        
        Returns:
            Diccionario con resultados
        """
        start_time = time.time()
        
        print("\n" + "=" * 50)
        print("EJECUTANDO GA PARA TSP")
        print("=" * 50)
        print(f"Población: {self.population_size}")
        print(f"Generaciones: {self.num_generations}")
        print(f"Tasa de mutación: {self.mutation_rate}")
        print(f"Tasa de cruzamiento: {self.crossover_rate}")
        print(f"Tamaño élite: {self.elite_size}")
        print()
        
        self._initialize_population()
        
        for generation in range(self.num_generations):
            # Seleccionar individuos
            selected = self._selection()
            
            # Crear nueva población mediante cruzamiento y mutación
            new_population = []
            new_fitness = []
            
            # Preservar élite
            elite_indices = np.argsort(self.fitness)[:self.elite_size]
            for idx in elite_indices:
                new_population.append(self.population[idx].copy())
                new_fitness.append(self.fitness[idx])
            
            # Generar resto de población
            while len(new_population) < self.population_size:
                # Seleccionar dos padres
                parent1 = selected[np.random.randint(0, len(selected))]
                parent2 = selected[np.random.randint(0, len(selected))]
                
                # Cruzamiento
                child1, child2 = self._crossover(parent1, parent2)
                
                # Mutación
                child1 = self._mutate(child1)
                if len(new_population) < self.population_size:
                    child2 = self._mutate(child2)
                
                # Añadir a nueva población
                new_population.append(child1)
                new_fitness.append(self._calculate_fitness(child1))
                
                if len(new_population) < self.population_size:
                    new_population.append(child2)
                    new_fitness.append(self._calculate_fitness(child2))
            
            # Actualizar población
            self.population = new_population[:self.population_size]
            self.fitness = new_fitness[:self.population_size]
            
            # Actualizar mejor individual
            best_idx = np.argmin(self.fitness)
            if self.fitness[best_idx] < self.best_fitness:
                self.best_fitness = self.fitness[best_idx]
                self.best_individual = self.population[best_idx].copy()
            
            self.fitness_history.append(self.best_fitness)
            
            if (generation + 1) % 20 == 0:
                print(f"Generación {generation + 1}: Mejor distancia = {self.best_fitness:.4f}")
        
        self.execution_time = time.time() - start_time
        
        print(f"\nMejor ruta encontrada: {list(self.best_individual)}")
        print(f"Distancia total: {self.best_fitness:.4f}")
        print(f"Tiempo de ejecución: {self.execution_time:.4f} segundos")
        
        return {
            'algorithm': 'GA',
            'best_solution': list(self.best_individual),
            'best_distance': self.best_fitness,
            'iterations': self.num_generations,
            'execution_time': self.execution_time,
            'fitness_history': self.fitness_history
        }


if __name__ == "__main__":
    problem = TSPProblem()
    ga = GA_TSP(problem, population_size=50, num_generations=100)
    result = ga.solve()
    
    print("\n" + "=" * 50)
    print("RESULTADO GA")
    print("=" * 50)
    for key, value in result.items():
        if key != 'fitness_history':
            print(f"{key}: {value}")
