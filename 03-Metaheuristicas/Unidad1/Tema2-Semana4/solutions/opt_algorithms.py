"""Simple implementations of PSO, GA and ACO for a 2D continuous test function.
Saves results to JSON and prints a comparison table.
"""
import time
import json
import math
import random
from typing import List, Tuple
import numpy as np

# Objective function: f(x,y) = 3x^2 + 2y^2 (minimize)

def objective(sol: Tuple[float, float]) -> float:
    x, y = sol
    return 3*x*x + 2*y*y

# PSO implementation
class PSO:
    def __init__(self, n_particles=30, iters=100, bounds=((-5,5),(-5,5)), w=0.7, c1=1.5, c2=1.5):
        self.n = n_particles
        self.iters = iters
        self.bounds = bounds
        self.w = w
        self.c1 = c1
        self.c2 = c2

    def run(self):
        dim = 2
        x = np.array([np.random.uniform(self.bounds[i][0], self.bounds[i][1], self.n) for i in range(dim)]).T
        v = np.zeros_like(x)
        pbest = x.copy()
        pbest_val = np.array([objective(tuple(p)) for p in pbest])
        gbest_idx = np.argmin(pbest_val)
        gbest = pbest[gbest_idx].copy()

        start = time.time()
        history = []
        for t in range(self.iters):
            for i in range(self.n):
                r1, r2 = np.random.rand(), np.random.rand()
                v[i] = self.w*v[i] + self.c1*r1*(pbest[i]-x[i]) + self.c2*r2*(gbest-x[i])
                x[i] = x[i] + v[i]
                # enforce bounds
                for d in range(dim):
                    x[i,d] = np.clip(x[i,d], self.bounds[d][0], self.bounds[d][1])
                val = objective(tuple(x[i]))
                if val < pbest_val[i]:
                    pbest[i] = x[i].copy()
                    pbest_val[i] = val
                    if val < objective(tuple(gbest)):
                        gbest = x[i].copy()
            history.append(float(objective(tuple(gbest))))
        end = time.time()
        return {
            'best': [float(g) for g in gbest],
            'best_val': float(objective(tuple(gbest))),
            'iters': self.iters,
            'time': end-start,
            'history': history
        }

# Simple GA for continuous variables using real-valued encoding
class GA:
    def __init__(self, pop_size=40, iters=100, bounds=((-5,5),(-5,5)), cx_prob=0.8, mut_prob=0.2, mut_scale=0.5):
        self.pop_size = pop_size
        self.iters = iters
        self.bounds = bounds
        self.cx_prob = cx_prob
        self.mut_prob = mut_prob
        self.mut_scale = mut_scale

    def run(self):
        dim = 2
        pop = np.array([np.array([np.random.uniform(self.bounds[d][0], self.bounds[d][1]) for d in range(dim)]) for _ in range(self.pop_size)])
        start = time.time()
        history = []
        for t in range(self.iters):
            vals = np.array([objective(tuple(ind)) for ind in pop])
            # selection: tournament
            new_pop = []
            while len(new_pop) < self.pop_size:
                i1, i2 = np.random.randint(0, self.pop_size, 2)
                parent1 = pop[i1] if vals[i1] < vals[i2] else pop[i2]
                i3, i4 = np.random.randint(0, self.pop_size, 2)
                parent2 = pop[i3] if vals[i3] < vals[i4] else pop[i4]
                # crossover
                if random.random() < self.cx_prob:
                    alpha = random.random()
                    child = alpha*parent1 + (1-alpha)*parent2
                else:
                    child = parent1.copy()
                # mutation
                if random.random() < self.mut_prob:
                    child = child + np.random.normal(scale=self.mut_scale, size=dim)
                # clip
                for d in range(dim):
                    child[d] = np.clip(child[d], self.bounds[d][0], self.bounds[d][1])
                new_pop.append(child)
            pop = np.array(new_pop)
            best_idx = np.argmin([objective(tuple(ind)) for ind in pop])
            history.append(float(objective(tuple(pop[best_idx]))))
        end = time.time()
        best_idx = int(np.argmin([objective(tuple(ind)) for ind in pop]))
        best = pop[best_idx]
        return {
            'best': [float(b) for b in best],
            'best_val': float(objective(tuple(best))),
            'iters': self.iters,
            'time': end-start,
            'history': history
        }

# Ant Colony Optimization for TSP-like small discrete problem
class ACO:
    def __init__(self, n_ants=20, iters=100, pheromone_evap=0.5, alpha=1.0, beta=2.0):
        self.n_ants = n_ants
        self.iters = iters
        self.evap = pheromone_evap
        self.alpha = alpha
        self.beta = beta

    # We'll solve a 5-city TSP with distances provided
    def run_tsp(self, dist_matrix):
        n = len(dist_matrix)
        pher = np.ones((n,n))
        best_route = None
        best_len = float('inf')
        start = time.time()
        history = []
        for it in range(self.iters):
            routes = []
            lengths = []
            for a in range(self.n_ants):
                route = [np.random.randint(0,n)]
                while len(route) < n:
                    i = route[-1]
                    probs = []
                    for j in range(n):
                        if j in route:
                            probs.append(0.0)
                        else:
                            tau = pher[i,j]**self.alpha
                            eta = (1.0/(dist_matrix[i][j]+1e-9))**self.beta
                            probs.append(tau*eta)
                    probs = np.array(probs)
                    probs_sum = probs.sum()
                    if probs_sum==0:
                        choices = [j for j in range(n) if j not in route]
                        nxt = random.choice(choices)
                    else:
                        probs = probs / probs_sum
                        nxt = np.random.choice(range(n), p=probs)
                    route.append(int(nxt))
                # compute length
                length = sum(dist_matrix[route[i]][route[(i+1)%n]] for i in range(n))
                routes.append(route)
                lengths.append(length)
            # update pheromones
            pher = (1-self.evap)*pher
            for r,l in zip(routes,lengths):
                for i in range(n):
                    j = (i+1)%n
                    a = r[i]
                    b = r[j]
                    pher[a,b] += 1.0 / (l+1e-9)
            it_best_idx = int(np.argmin(lengths))
            if lengths[it_best_idx] < best_len:
                best_len = lengths[it_best_idx]
                best_route = routes[it_best_idx]
            history.append(float(best_len))
        end = time.time()
        return {
            'best_route': [int(r) for r in best_route],
            'best_len': float(best_len),
            'iters': self.iters,
            'time': end-start,
            'history': history
        }

# Helper to run experiments and save

def run_experiments():
    results = {}
    # PSO
    pso = PSO(n_particles=40, iters=200)
    print('Running PSO...')
    res_pso = pso.run()
    results['PSO'] = res_pso

    # GA
    ga = GA(pop_size=60, iters=200)
    print('Running GA...')
    res_ga = ga.run()
    results['GA'] = res_ga

    # ACO on TSP 5 cities
    coords = np.array([[0,0],[1,0],[1,1],[0,1],[0.5,0.5]])
    n = len(coords)
    dist = [[math.dist(coords[i],coords[j]) for j in range(n)] for i in range(n)]
    aco = ACO(n_ants=30, iters=200)
    print('Running ACO (TSP 5 cities)...')
    res_aco = aco.run_tsp(dist)
    results['ACO'] = res_aco

    with open('solutions_results.json','w',encoding='utf-8') as f:
        json.dump(results,f,indent=2,ensure_ascii=False)
    print('Saved solutions_results.json')
    print_summary(results)


def print_summary(results):
    print('\nComparison summary:')
    print('Algorithm | Best Value / Route | Iterations | Time (s)')
    print('----------------------------------------------------------')
    print(f"PSO       | {results['PSO']['best_val']:.6f}        | {results['PSO']['iters']}       | {results['PSO']['time']:.4f}")
    print(f"GA        | {results['GA']['best_val']:.6f}        | {results['GA']['iters']}       | {results['GA']['time']:.4f}")
    print(f"ACO       | {results['ACO']['best_len']:.6f}        | {results['ACO']['iters']}       | {results['ACO']['time']:.4f}")

if __name__ == '__main__':
    run_experiments()
