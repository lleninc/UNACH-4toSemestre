"""
Módulo TSP Problem - Define el problema del vendedor viajero
"""
import numpy as np
from typing import Tuple, List
import math

class TSPProblem:
    """
    Clase que define un problema de TSP (Traveling Salesman Problem)
    con 5 ciudades.
    """
    
    def __init__(self, seed: int = 42):
        """
        Inicializa el problema TSP con 5 ciudades.
        
        Args:
            seed: Semilla para reproducibilidad
        """
        np.random.seed(seed)
        self.num_cities = 5
        self.cities = self._create_cities()
        self.distance_matrix = self._calculate_distances()
        
    def _create_cities(self) -> np.ndarray:
        """
        Crea 5 ciudades con coordenadas aleatorias.
        
        Returns:
            Array de coordenadas (x, y) de las ciudades
        """
        cities = np.array([
            [0, 0],      # Ciudad 0
            [10, 5],     # Ciudad 1
            [15, 15],    # Ciudad 2
            [5, 20],     # Ciudad 3
            [20, 10]     # Ciudad 4
        ], dtype=float)
        
        print("=" * 50)
        print("CIUDADES DEL PROBLEMA TSP")
        print("=" * 50)
        for i, city in enumerate(cities):
            print(f"Ciudad {i}: ({city[0]:.1f}, {city[1]:.1f})")
        print()
        
        return cities
    
    def _calculate_distances(self) -> np.ndarray:
        """
        Calcula la matriz de distancias euclidianas entre todas las ciudades.
        
        Returns:
            Matriz de distancias (NxN)
        """
        n = self.num_cities
        distances = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                if i != j:
                    distances[i][j] = self._euclidean_distance(
                        self.cities[i], 
                        self.cities[j]
                    )
        
        return distances
    
    @staticmethod
    def _euclidean_distance(point1: np.ndarray, point2: np.ndarray) -> float:
        """
        Calcula la distancia euclidiana entre dos puntos.
        
        Args:
            point1: Primera coordenada
            point2: Segunda coordenada
            
        Returns:
            Distancia euclidiana
        """
        return np.sqrt(np.sum((point1 - point2) ** 2))
    
    def calculate_tour_distance(self, tour: List[int]) -> float:
        """
        Calcula la distancia total de una ruta.
        
        Args:
            tour: Lista de índices de ciudades representando la ruta
            
        Returns:
            Distancia total de la ruta
        """
        total_distance = 0
        n = len(tour)
        
        for i in range(n):
            current_city = tour[i]
            next_city = tour[(i + 1) % n]  # Regresa a la ciudad inicial
            total_distance += self.distance_matrix[current_city][next_city]
        
        return total_distance
    
    def get_distance_matrix(self) -> np.ndarray:
        """Retorna la matriz de distancias."""
        return self.distance_matrix
    
    def get_cities(self) -> np.ndarray:
        """Retorna las coordenadas de las ciudades."""
        return self.cities
    
    def get_num_cities(self) -> int:
        """Retorna el número de ciudades."""
        return self.num_cities
    
    def print_distance_matrix(self):
        """Imprime la matriz de distancias."""
        print("=" * 50)
        print("MATRIZ DE DISTANCIAS")
        print("=" * 50)
        
        # Encabezado
        print("       ", end="")
        for j in range(self.num_cities):
            print(f"C{j:2d}    ", end="")
        print()
        
        # Filas
        for i in range(self.num_cities):
            print(f"C{i}  ", end="")
            for j in range(self.num_cities):
                print(f"{self.distance_matrix[i][j]:6.2f} ", end="")
            print()
        print()


if __name__ == "__main__":
    # Prueba del módulo
    problem = TSPProblem()
    problem.print_distance_matrix()
    
    # Ejemplo de ruta
    tour = [0, 1, 2, 3, 4]
    distance = problem.calculate_tour_distance(tour)
    print(f"\nRuta de ejemplo: {tour}")
    print(f"Distancia total: {distance:.2f}")
