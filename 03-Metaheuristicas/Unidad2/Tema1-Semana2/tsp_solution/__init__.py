"""
Paquete TSP Solution - Comparación de Metaheurísticas

Este paquete contiene implementaciones de PSO, GA y ACO para resolver el TSP.
"""

__version__ = "1.0.0"
__author__ = "Estudiante UNACH"

from .tsp_problem import TSPProblem
from .pso_tsp import PSO_TSP
from .ga_tsp import GA_TSP
from .aco_tsp import ACO_TSP

__all__ = ['TSPProblem', 'PSO_TSP', 'GA_TSP', 'ACO_TSP']
