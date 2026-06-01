import time
import random
import math
from typing import Tuple, List
from tsp import tour_length, swap_neighbor

def simulated_annealing(D: List[List[float]], max_iters: int = 10000, T0: float = 100.0, alpha: float = 0.995) -> Tuple[List[int], float, int]:
    n = len(D)
    current = list(range(n))
    random.shuffle(current)
    current_cost = tour_length(current, D)
    best = current.copy()
    best_cost = current_cost
    T = T0
    it = 0
    start = time.time()
    while it < max_iters and T > 1e-8:
        neighbor = swap_neighbor(current)
        neighbor_cost = tour_length(neighbor, D)
        delta = neighbor_cost - current_cost
        if delta < 0 or random.random() < math.exp(-delta / T):
            current = neighbor
            current_cost = neighbor_cost
            if current_cost < best_cost:
                best = current.copy()
                best_cost = current_cost
        T *= alpha
        it += 1
    elapsed = time.time() - start
    return best, best_cost, it, elapsed

if __name__ == '__main__':
    print('Run sa module as library')
