import math
import random
from typing import List, Tuple

def euclidean(a: Tuple[float,float], b: Tuple[float,float]) -> float:
    return math.hypot(a[0]-b[0], a[1]-b[1])

def generate_points(n: int, seed: int = None, scale: int = 100) -> List[Tuple[float,float]]:
    if seed is not None:
        random.seed(seed)
    return [(random.random()*scale, random.random()*scale) for _ in range(n)]

def distance_matrix(points: List[Tuple[float,float]]) -> List[List[float]]:
    n = len(points)
    D = [[0.0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                D[i][j] = euclidean(points[i], points[j])
    return D

def tour_length(tour: List[int], D: List[List[float]]) -> float:
    n = len(tour)
    s = 0.0
    for i in range(n):
        a = tour[i]
        b = tour[(i+1)%n]
        s += D[a][b]
    return s

def random_tour(n: int) -> List[int]:
    tour = list(range(n))
    random.shuffle(tour)
    return tour

def swap_neighbor(tour: List[int]) -> List[int]:
    n = len(tour)
    i = random.randrange(n)
    j = random.randrange(n)
    while j == i:
        j = random.randrange(n)
    new = tour.copy()
    new[i], new[j] = new[j], new[i]
    return new

def two_opt_neighbor(tour: List[int]) -> List[int]:
    n = len(tour)
    i = random.randrange(0, n-1)
    j = random.randrange(i+1, n)
    new = tour.copy()
    new[i:j+1] = reversed(new[i:j+1])
    return new
