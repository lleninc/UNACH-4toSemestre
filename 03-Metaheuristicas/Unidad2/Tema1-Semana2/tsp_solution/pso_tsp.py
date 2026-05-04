"""
Módulo PSO - Particle Swarm Optimization para TSP
"""
import numpy as np
from typing import List, Tuple, Dict
import time
from tsp_problem import TSPProblem


class PSO_TSP:
    """
    Implementación de Particle Swarm Optimization para resolver el TSP.
    
    En PSO, cada partícula representa una solución (una ruta), y se mueve en el
    espacio de búsqueda basado en su mejor solución y la del enjambre.
    """
    
    def __init__(
        self,
        tsp_problem: TSPProblem,
        num_particles: int = 30,
        num_iterations: int = 100,
        w: float = 0.7,  # Peso de inercia
        c1: float = 1.5,  # Coeficiente cognitivo
        c2: float = 1.5   # Coeficiente social
    ):
        """
        Inicializa PSO para TSP.
        
        Args:
            tsp_problem: Instancia del problema TSP
            num_particles: Número de partículas
            num_iterations: Número de iteraciones
            w: Peso de inercia
            c1: Coeficiente cognitivo
            c2: Coeficiente social
        """
        self.problem = tsp_problem
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        
        self.num_cities = tsp_problem.get_num_cities()
        self.particles = []
        self.velocities = []
        self.pbest = []  # Mejor posición personal
        self.pbest_fitness = []
        self.gbest = None  # Mejor posición global
        self.gbest_fitness = float('inf')
        
        self.fitness_history = []
        self.execution_time = 0
        
    def _initialize_population(self):
        """Inicializa la población de partículas con rutas aleatorias."""
        for _ in range(self.num_particles):
            # Crear una ruta aleatoria
            tour = np.random.permutation(self.num_cities)
            self.particles.append(tour.copy())
            
            # Inicializar velocidad (permutación aleatoria)
            velocity = np.random.permutation(self.num_cities)
            self.velocities.append(velocity.copy())
            
            # Mejor posición personal
            self.pbest.append(tour.copy())
            distance = self.problem.calculate_tour_distance(tour)
            self.pbest_fitness.append(distance)
            
            # Actualizar mejor global si es necesario
            if distance < self.gbest_fitness:
                self.gbest = tour.copy()
                self.gbest_fitness = distance
    
    def _apply_velocity(self, particle: np.ndarray, velocity: np.ndarray) -> np.ndarray:
        """
        Aplica la velocidad a una partícula usando operador de permutación.
        
        Args:
            particle: Ruta actual
            velocity: Velocidad (como permutación)
            
        Returns:
            Nueva ruta después de aplicar velocidad
        """
        # Operador de permutación simplificado: mezcla la ruta
        new_particle = particle.copy()
        
        # Usar velocidad para determinar intercambios
        num_swaps = max(1, int(len(velocity) * 0.3))
        
        for _ in range(num_swaps):
            i, j = np.random.choice(self.num_cities, 2, replace=False)
            new_particle[i], new_particle[j] = new_particle[j], new_particle[i]
        
        return new_particle
    
    def solve(self) -> Dict:
        """
        Ejecuta el algoritmo PSO.
        
        Returns:
            Diccionario con resultados
        """
        start_time = time.time()
        
        print("\n" + "=" * 50)
        print("EJECUTANDO PSO PARA TSP")
        print("=" * 50)
        print(f"Partículas: {self.num_particles}")
        print(f"Iteraciones: {self.num_iterations}")
        print(f"w: {self.w}, c1: {self.c1}, c2: {self.c2}")
        print()
        
        self._initialize_population()
        
        for iteration in range(self.num_iterations):
            for i in range(self.num_particles):
                # Actualizar velocidad
                r1 = np.random.random()
                r2 = np.random.random()
                
                # Aplicar operador PSO modificado
                self.velocities[i] = (
                    self.w * self.velocities[i] +
                    self.c1 * r1 * (self.pbest[i] - self.particles[i]) +
                    self.c2 * r2 * (self.gbest - self.particles[i])
                )
                
                # Aplicar velocidad a la partícula
                self.particles[i] = self._apply_velocity(
                    self.particles[i],
                    self.velocities[i]
                )
                
                # Asegurar que es una permutación válida
                self.particles[i] = np.array(
                    list(set(self.particles[i][:self.num_cities]))
                    + list(set(range(self.num_cities)) - set(self.particles[i][:self.num_cities]))
                )[:self.num_cities]
                
                # Evaluar nueva posición
                distance = self.problem.calculate_tour_distance(self.particles[i])
                
                # Actualizar mejor personal
                if distance < self.pbest_fitness[i]:
                    self.pbest[i] = self.particles[i].copy()
                    self.pbest_fitness[i] = distance
                    
                    # Actualizar mejor global
                    if distance < self.gbest_fitness:
                        self.gbest = self.particles[i].copy()
                        self.gbest_fitness = distance
            
            self.fitness_history.append(self.gbest_fitness)
            
            if (iteration + 1) % 20 == 0:
                print(f"Iteración {iteration + 1}: Mejor distancia = {self.gbest_fitness:.4f}")
        
        self.execution_time = time.time() - start_time
        
        print(f"\nMejor ruta encontrada: {list(self.gbest)}")
        print(f"Distancia total: {self.gbest_fitness:.4f}")
        print(f"Tiempo de ejecución: {self.execution_time:.4f} segundos")
        
        return {
            'algorithm': 'PSO',
            'best_solution': list(self.gbest),
            'best_distance': self.gbest_fitness,
            'iterations': self.num_iterations,
            'execution_time': self.execution_time,
            'fitness_history': self.fitness_history
        }


if __name__ == "__main__":
    problem = TSPProblem()
    pso = PSO_TSP(problem, num_particles=30, num_iterations=100)
    result = pso.solve()
    
    print("\n" + "=" * 50)
    print("RESULTADO PSO")
    print("=" * 50)
    for key, value in result.items():
        if key != 'fitness_history':
            print(f"{key}: {value}")
