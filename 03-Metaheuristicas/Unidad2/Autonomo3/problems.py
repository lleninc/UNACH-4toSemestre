import math
import random


class SphereProblem:
    def __init__(self, dim=5, bounds=(-5.12, 5.12)):
        self.dim = dim
        self.bounds = bounds

    def initial_solution(self):
        return [random.uniform(self.bounds[0], self.bounds[1]) for _ in range(self.dim)]

    def neighbor(self, s):
        t = s.copy()
        i = random.randrange(self.dim)
        t[i] += random.gauss(0, 0.5)
        # clip
        t[i] = max(min(t[i], self.bounds[1]), self.bounds[0])
        return t

    def evaluate(self, s):
        return sum(x * x for x in s)


class TSPProblem:
    def __init__(self, cities=None):
        # cities: list of (x,y)
        if cities is None:
            self.cities = [(0, 0), (1, 3), (4, 3), (6, 1), (3, -1)]
        else:
            self.cities = cities
        self.n = len(self.cities)

    def initial_solution(self):
        perm = list(range(self.n))
        random.shuffle(perm)
        return perm

    def neighbor(self, s):
        t = s.copy()
        i, j = random.sample(range(self.n), 2)
        t[i], t[j] = t[j], t[i]
        return t

    def evaluate(self, s):
        dist = 0.0
        for i in range(self.n):
            a = self.cities[s[i]]
            b = self.cities[s[(i + 1) % self.n]]
            dist += math.hypot(a[0] - b[0], a[1] - b[1])
        return dist
