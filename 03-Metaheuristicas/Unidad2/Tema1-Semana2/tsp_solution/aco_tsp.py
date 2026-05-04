"""
Módulo ACO - Ant Colony Optimization para TSP
"""
import numpy as np
from typing import List, Dict, Tuple
import time
from tsp_problem import TSPProblem


class ACO_TSP:
    """
    Implementación de Ant Colony Optimization para resolver el TSP
    En ACO, las hormigas exploran rutas y depositan feromonas que atraen
    a otras hormigas a seguir caminos mejores.
    """
    
    def __init__(
        self,
        tsp_problem: TSPProblem,
        num_ants: int = 30,
        num_iterations: int = 100,
        alpha: float = 1.0,  # Importancia de feromona
        beta: float = 2.0,   # Importancia de distancia
        rho: float = 0.1,    # Tasa de evaporación
        q: float = 100.0     # Cantidad de feromona depositada
    ):
        """
        Inicializa ACO para TSP.
        
        Args:
            tsp_problem: Instancia del problema TSP
            num_ants: Número de hormigas
            num_iterations: Número de iteraciones
            alpha: Importancia de la feromona
            beta: Importancia de la distancia
            rho: Tasa de evaporación de feromona
            q: Cantidad de feromona depositada
        """
        self.problem = tsp_problem
        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        
        self.num_cities = tsp_problem.get_num_cities()
        self.distance_matrix = tsp_problem.get_distance_matrix()
        
        # Inicializar feromonas
        self.pheromone = np.ones((self.num_cities, self.num_cities)) / self.num_cities
        
        self.best_path = None
        self.best_distance = float('inf')
        
        self.fitness_history = []
        self.execution_time = 0
    
    def _construct_solution(self) -> Tuple[List[int], float]:
        """
        Una hormiga construye una solución (ruta).
        
        Returns:
            Tupla (ruta, distancia)
        """
        unvisited = set(range(self.num_cities))
        
        # Empezar desde una ciudad aleatoria
        current_city = np.random.randint(0, self.num_cities)
        path = [current_city]
        unvisited.remove(current_city)
        
        # Construir ruta
        while unvisited:
            next_city = self._select_next_city(current_city, unvisited)
            path.append(next_city)
            unvisited.remove(next_city)
            current_city = next_city
        
        # Calcular distancia
        distance = self.problem.calculate_tour_distance(path)
        
        return path, distance
    
    def _select_next_city(self, current_city: int, unvisited: set) -> int:
        """
        Selecciona la siguiente ciudad según la regla probabilística de ACO.
        
        Args:
            current_city: Ciudad actual
            unvisited: Conjunto de ciudades no visitadas
            
        Returns:
            Siguiente ciudad
        """
        probabilities = []
        cities_list = list(unvisited)
        
        # Calcular probabilidades
        for city in cities_list:
            # Feromona
            pheromone_level = self.pheromone[current_city][city] ** self.alpha
            
            # Distancia (inversa)
            distance = self.distance_matrix[current_city][city]
            if distance == 0:
                distance = 0.0001
            distance_factor = (1.0 / distance) ** self.beta
            
            probability = pheromone_level * distance_factor
            probabilities.append(probability)
        
        # Normalizar probabilidades
        total_prob = sum(probabilities)
        if total_prob == 0:
            return cities_list[np.random.randint(0, len(cities_list))]
        
        probabilities = np.array(probabilities) / total_prob
        
        # Seleccionar ciudad según probabilidades
        next_city = np.random.choice(cities_list, p=probabilities)
        
        return next_city
    
    def _update_pheromone(self, paths: List[List[int]], distances: List[float]):
        """
        Actualiza la matriz de feromonas después de una iteración.
        
        Args:
            paths: Lista de rutas de las hormigas
            distances: Lista de distancias de las rutas
        """
        # Evaporación de feromona
        self.pheromone *= (1 - self.rho)
        
        # Depositar feromona
        for path, distance in zip(paths, distances):
            pheromone_deposited = self.q / distance
            
            for i in range(len(path)):
                current_city = path[i]
                next_city = path[(i + 1) % len(path)]
                
                self.pheromone[current_city][next_city] += pheromone_deposited
                self.pheromone[next_city][current_city] += pheromone_deposited
    
    def solve(self) -> Dict:
        """
        Ejecuta el algoritmo ACO.
        
        Returns:
            Diccionario con resultados
        """
        start_time = time.time()
        
        print("\n" + "=" * 50)
        print("EJECUTANDO ACO PARA TSP")
        print("=" * 50)
        print(f"Hormigas: {self.num_ants}")
        print(f"Iteraciones: {self.num_iterations}")
        print(f"Alpha: {self.alpha}, Beta: {self.beta}")
        print(f"Rho (evaporación): {self.rho}, Q: {self.q}")
        print()
        
        for iteration in range(self.num_iterations):
            paths = []
            distances = []
            
            # Cada hormiga construye una solución
            for _ in range(self.num_ants):
                path, distance = self._construct_solution()
                paths.append(path)
                distances.append(distance)
                
                # Actualizar mejor solución
                if distance < self.best_distance:
                    self.best_distance = distance
                    self.best_path = path.copy()
            
            # Actualizar feromona
            self._update_pheromone(paths, distances)
            
            self.fitness_history.append(self.best_distance)
            
            if (iteration + 1) % 20 == 0:
                print(f"Iteración {iteration + 1}: Mejor distancia = {self.best_distance:.4f}")
        
        self.execution_time = time.time() - start_time
        
        print(f"\nMejor ruta encontrada: {self.best_path}")
        print(f"Distancia total: {self.best_distance:.4f}")
        print(f"Tiempo de ejecución: {self.execution_time:.4f} segundos")
        
        return {
            'algorithm': 'ACO',
            'best_solution': self.best_path,
            'best_distance': self.best_distance,
            'iterations': self.num_iterations,
            'execution_time': self.execution_time,
            'fitness_history': self.fitness_history
        }


if __name__ == "__main__":
    problem = TSPProblem()
    aco = ACO_TSP(problem, num_ants=30, num_iterations=100)
    result = aco.solve()
    
    print("\n" + "=" * 50)
    print("RESULTADO ACO")
    print("=" * 50)
    for key, value in result.items():
        if key != 'fitness_history':
            print(f"{key}: {value}")
