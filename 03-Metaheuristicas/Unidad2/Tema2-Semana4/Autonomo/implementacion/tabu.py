import time
import random
from typing import List, Tuple
from tsp import tour_length

def swap_move(tour: List[int], i: int, j: int) -> List[int]:
    new = tour.copy()
    new[i], new[j] = new[j], new[i]
    return new

def tabu_search(D: List[List[float]], max_iters: int = 1000, tabu_tenure: int = 7) -> Tuple[List[int], float, int]:
    n = len(D)
    current = list(range(n))
    random.shuffle(current)
    best = current.copy()
    best_cost = tour_length(best, D)
    tabu_list = {}
    it = 0
    start = time.time()
    while it < max_iters:
        neighborhood = []
        for i in range(n-1):
            for j in range(i+1, n):
                neighbor = swap_move(current, i, j)
                cost = tour_length(neighbor, D)
                neighborhood.append((cost, i, j, neighbor))
        neighborhood.sort(key=lambda x: x[0])
        moved = False
        for cost, i, j, neighbor in neighborhood:
            move = (i, j)
            if move not in tabu_list or cost < best_cost:
                current = neighbor
                if cost < best_cost:
                    best = neighbor.copy()
                    best_cost = cost
                tabu_list[move] = it + tabu_tenure
                moved = True
                break
        # decrement / remove expired
        expired = [m for m, expiry in tabu_list.items() if expiry <= it]
        for m in expired:
            del tabu_list[m]
        if not moved:
            break
        it += 1
    elapsed = time.time() - start
    return best, best_cost, it, elapsed

if __name__ == '__main__':
    print('Run tabu module as library')
