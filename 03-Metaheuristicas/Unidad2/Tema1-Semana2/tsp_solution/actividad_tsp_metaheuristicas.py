"""
Solucion autocontenida para la actividad TSP.

Incluye cuatro metaheuristicas sobre una instancia pequena del problema del
vendedor viajero:
- PSO
- GA
- SA
- TS

La implementacion usa una instancia fija de ciudades para que el resultado sea
reproducible y facil de presentar en clase.
"""

from __future__ import annotations

import math
import random
import time
from dataclasses import dataclass
from typing import Dict, List, Sequence, Tuple

import numpy as np


City = Tuple[float, float]
Tour = List[int]


class TSPProblem:
    def __init__(self, cities: Sequence[City] | None = None):
        if cities is None:
            cities = [
                (0.0, 0.0),
                (2.0, 6.0),
                (5.0, 3.0),
                (6.0, 9.0),
                (9.0, 1.0),
                (10.0, 7.0),
            ]
        self.cities = np.array(cities, dtype=float)
        self.num_cities = len(cities)
        self.distance_matrix = self._build_distance_matrix()

    def _build_distance_matrix(self) -> np.ndarray:
        matrix = np.zeros((self.num_cities, self.num_cities), dtype=float)
        for i in range(self.num_cities):
            for j in range(self.num_cities):
                if i != j:
                    matrix[i, j] = float(np.linalg.norm(self.cities[i] - self.cities[j]))
        return matrix

    def tour_distance(self, tour: Sequence[int]) -> float:
        distance = 0.0
        for index in range(len(tour)):
            a = tour[index]
            b = tour[(index + 1) % len(tour)]
            distance += float(self.distance_matrix[a, b])
        return distance

    def random_tour(self) -> Tour:
        tour = list(range(self.num_cities))
        random.shuffle(tour)
        return tour

    def swap_neighbor(self, tour: Sequence[int]) -> Tour:
        new_tour = list(tour)
        i, j = random.sample(range(self.num_cities), 2)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        return new_tour

    def two_opt_neighbor(self, tour: Sequence[int]) -> Tour:
        new_tour = list(tour)
        i = random.randint(0, self.num_cities - 2)
        j = random.randint(i + 1, self.num_cities - 1)
        new_tour[i : j + 1] = reversed(new_tour[i : j + 1])
        return new_tour


@dataclass
class OptimizationResult:
    algorithm: str
    best_solution: Tour
    best_distance: float
    iterations: int
    execution_time: float
    history: List[float]


class PSOTSP:
    """
    PSO para TSP con codificacion por random keys.

    Cada particula es un vector continuo. Al ordenar sus valores obtenemos una
    permutacion valida de ciudades.
    """

    def __init__(
        self,
        problem: TSPProblem,
        num_particles: int = 30,
        num_iterations: int = 100,
        w: float = 0.72,
        c1: float = 1.5,
        c2: float = 1.5,
        seed: int = 42,
    ):
        self.problem = problem
        self.num_particles = num_particles
        self.num_iterations = num_iterations
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.rng = np.random.default_rng(seed)

    def _decode(self, position: np.ndarray) -> Tour:
        return [int(city) for city in np.argsort(position)]

    def solve(self) -> OptimizationResult:
        start = time.time()
        dimension = self.problem.num_cities

        positions = self.rng.random((self.num_particles, dimension))
        velocities = self.rng.uniform(-1.0, 1.0, size=(self.num_particles, dimension))

        pbest_positions = positions.copy()
        pbest_scores = np.array(
            [self.problem.tour_distance(self._decode(position)) for position in positions]
        )

        gbest_index = int(np.argmin(pbest_scores))
        gbest_position = pbest_positions[gbest_index].copy()
        gbest_score = float(pbest_scores[gbest_index])

        history: List[float] = [gbest_score]

        for _ in range(self.num_iterations):
            for particle_index in range(self.num_particles):
                r1 = self.rng.random(dimension)
                r2 = self.rng.random(dimension)
                velocities[particle_index] = (
                    self.w * velocities[particle_index]
                    + self.c1 * r1 * (pbest_positions[particle_index] - positions[particle_index])
                    + self.c2 * r2 * (gbest_position - positions[particle_index])
                )
                positions[particle_index] = positions[particle_index] + velocities[particle_index]

                candidate_score = self.problem.tour_distance(
                    self._decode(positions[particle_index])
                )
                if candidate_score < pbest_scores[particle_index]:
                    pbest_scores[particle_index] = candidate_score
                    pbest_positions[particle_index] = positions[particle_index].copy()
                    if candidate_score < gbest_score:
                        gbest_score = candidate_score
                        gbest_position = positions[particle_index].copy()

            history.append(gbest_score)

        elapsed = time.time() - start
        best_solution = self._decode(gbest_position)
        return OptimizationResult("PSO", best_solution, gbest_score, self.num_iterations, elapsed, history)


class GATSP:
    def __init__(
        self,
        problem: TSPProblem,
        population_size: int = 40,
        num_generations: int = 100,
        mutation_rate: float = 0.15,
        crossover_rate: float = 0.9,
        elite_size: int = 4,
        seed: int = 42,
    ):
        self.problem = problem
        self.population_size = population_size
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.elite_size = elite_size
        self.rng = np.random.default_rng(seed)

    def _random_tour(self) -> Tour:
        tour = list(range(self.problem.num_cities))
        self.rng.shuffle(tour)
        return tour

    def _fitness(self, tour: Sequence[int]) -> float:
        return self.problem.tour_distance(tour)

    def _tournament(self, population: List[Tour], fitness: List[float], size: int = 3) -> Tour:
        contenders = self.rng.choice(len(population), size=size, replace=False)
        best_index = min(contenders, key=lambda index: fitness[index])
        return list(population[best_index])

    def _order_crossover(self, parent1: Sequence[int], parent2: Sequence[int]) -> Tuple[Tour, Tour]:
        if self.rng.random() > self.crossover_rate:
            return list(parent1), list(parent2)

        n = len(parent1)
        start, end = sorted(self.rng.choice(n, size=2, replace=False))
        end += 1

        def build_child(a: Sequence[int], b: Sequence[int]) -> Tour:
            child = [-1] * n
            child[start:end] = a[start:end]
            fill_values = [city for city in b if city not in child]
            fill_index = 0
            for index in range(n):
                if child[index] == -1:
                    child[index] = fill_values[fill_index]
                    fill_index += 1
            return child

        return build_child(parent1, parent2), build_child(parent2, parent1)

    def _mutate(self, tour: Sequence[int]) -> Tour:
        mutated = list(tour)
        if self.rng.random() < self.mutation_rate:
            i, j = self.rng.choice(len(mutated), size=2, replace=False)
            mutated[i], mutated[j] = mutated[j], mutated[i]
        return mutated

    def solve(self) -> OptimizationResult:
        start = time.time()
        population = [self._random_tour() for _ in range(self.population_size)]
        fitness = [self._fitness(tour) for tour in population]

        best_index = int(np.argmin(fitness))
        best_tour = list(population[best_index])
        best_score = float(fitness[best_index])
        history: List[float] = [best_score]

        for _ in range(self.num_generations):
            elite_indices = np.argsort(fitness)[: self.elite_size]
            new_population = [list(population[index]) for index in elite_indices]

            while len(new_population) < self.population_size:
                parent1 = self._tournament(population, fitness)
                parent2 = self._tournament(population, fitness)
                child1, child2 = self._order_crossover(parent1, parent2)
                new_population.append(self._mutate(child1))
                if len(new_population) < self.population_size:
                    new_population.append(self._mutate(child2))

            population = new_population
            fitness = [self._fitness(tour) for tour in population]

            best_index = int(np.argmin(fitness))
            if fitness[best_index] < best_score:
                best_score = float(fitness[best_index])
                best_tour = list(population[best_index])

            history.append(best_score)

        elapsed = time.time() - start
        return OptimizationResult("GA", best_tour, best_score, self.num_generations, elapsed, history)


class SATSP:
    def __init__(
        self,
        problem: TSPProblem,
        max_iterations: int = 2000,
        initial_temperature: float = 100.0,
        cooling_rate: float = 0.995,
        seed: int = 42,
    ):
        self.problem = problem
        self.max_iterations = max_iterations
        self.initial_temperature = initial_temperature
        self.cooling_rate = cooling_rate
        random.seed(seed)

    def solve(self) -> OptimizationResult:
        start = time.time()
        current = self.problem.random_tour()
        current_score = self.problem.tour_distance(current)
        best = list(current)
        best_score = current_score
        temperature = self.initial_temperature
        history: List[float] = [best_score]

        iterations = 0
        while iterations < self.max_iterations and temperature > 1e-8:
            candidate = self.problem.two_opt_neighbor(current)
            candidate_score = self.problem.tour_distance(candidate)
            delta = candidate_score - current_score

            if delta < 0 or random.random() < math.exp(-delta / max(temperature, 1e-12)):
                current = candidate
                current_score = candidate_score

            if current_score < best_score:
                best = list(current)
                best_score = current_score

            history.append(best_score)
            temperature *= self.cooling_rate
            iterations += 1

        elapsed = time.time() - start
        return OptimizationResult("SA", best, best_score, iterations, elapsed, history)


class TSTSP:
    def __init__(
        self,
        problem: TSPProblem,
        max_iterations: int = 1000,
        tabu_tenure: int = 10,
        neighborhood_size: int = 40,
        seed: int = 42,
    ):
        self.problem = problem
        self.max_iterations = max_iterations
        self.tabu_tenure = tabu_tenure
        self.neighborhood_size = neighborhood_size
        random.seed(seed)

    def _tour_key(self, tour: Sequence[int]) -> Tuple[int, ...]:
        return tuple(int(city) for city in tour)

    def _swap_move(self, tour: Sequence[int], i: int, j: int) -> Tour:
        new_tour = list(tour)
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i]
        return new_tour

    def solve(self) -> OptimizationResult:
        start = time.time()
        current = self.problem.random_tour()
        current_score = self.problem.tour_distance(current)
        best = list(current)
        best_score = current_score
        tabu: Dict[Tuple[int, ...], int] = {}
        history: List[float] = [best_score]

        iterations = 0
        while iterations < self.max_iterations:
            candidates: List[Tuple[float, Tour]] = []
            n = self.problem.num_cities
            for _ in range(self.neighborhood_size):
                i, j = random.sample(range(n), 2)
                neighbor = self._swap_move(current, i, j)
                candidates.append((self.problem.tour_distance(neighbor), neighbor))

            candidates.sort(key=lambda item: item[0])
            selected_tour = None
            selected_score = None

            for score, neighbor in candidates:
                key = self._tour_key(neighbor)
                if key not in tabu or score < best_score:
                    selected_tour = neighbor
                    selected_score = score
                    break

            if selected_tour is None:
                break

            current = selected_tour
            current_score = float(selected_score)
            tabu[self._tour_key(current)] = iterations + self.tabu_tenure

            expired = [key for key, expiry in tabu.items() if expiry <= iterations]
            for key in expired:
                del tabu[key]

            if current_score < best_score:
                best = list(current)
                best_score = current_score

            history.append(best_score)
            iterations += 1

        elapsed = time.time() - start
        return OptimizationResult("TS", best, best_score, iterations, elapsed, history)


def print_problem(problem: TSPProblem) -> None:
    print("=" * 60)
    print("CIUDADES DEL TSP")
    print("=" * 60)
    for index, city in enumerate(problem.cities):
        print(f"Ciudad {index}: ({city[0]:.1f}, {city[1]:.1f})")
    print()


def print_result(result: OptimizationResult) -> None:
    print(f"Algoritmo: {result.algorithm}")
    print(f"Mejor ruta: {result.best_solution}")
    print(f"Distancia: {result.best_distance:.4f}")
    print(f"Iteraciones: {result.iterations}")
    print(f"Tiempo: {result.execution_time:.4f} segundos")
    print("-" * 60)


def run_experiment() -> Dict[str, Dict[str, object]]:
    random.seed(42)
    np.random.seed(42)

    problem = TSPProblem()
    print_problem(problem)

    algorithms = [
        PSOTSP(problem, num_particles=30, num_iterations=100, seed=42),
        GATSP(problem, population_size=40, num_generations=100, seed=42),
        SATSP(problem, max_iterations=2000, initial_temperature=100.0, cooling_rate=0.995, seed=42),
        TSTSP(problem, max_iterations=1000, tabu_tenure=10, neighborhood_size=40, seed=42),
    ]

    results: Dict[str, Dict[str, object]] = {}
    for algorithm in algorithms:
        result = algorithm.solve()
        print_result(result)
        results[result.algorithm] = {
            "best_solution": result.best_solution,
            "best_distance": result.best_distance,
            "iterations": result.iterations,
            "execution_time": result.execution_time,
            "history": result.history,
        }

    return results


if __name__ == "__main__":
    run_experiment()