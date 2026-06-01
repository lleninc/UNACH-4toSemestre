import csv
import statistics
from tsp import generate_points, distance_matrix
from sa import simulated_annealing
from tabu import tabu_search

NUM_NODES = 8
RUNS = 5

def run():
    points = generate_points(NUM_NODES, seed=42)
    D = distance_matrix(points)

    results = []

    # Simulated Annealing runs
    sa_costs = []
    sa_times = []
    sa_iters = []
    for r in range(RUNS):
        best, cost, iters, elapsed = simulated_annealing(D, max_iters=20000, T0=100.0, alpha=0.995)
        sa_costs.append(cost)
        sa_times.append(elapsed)
        sa_iters.append(iters)
        results.append(('SA', r+1, cost, elapsed, iters))

    # Tabu Search runs
    tabu_costs = []
    tabu_times = []
    tabu_iters = []
    for r in range(RUNS):
        best, cost, iters, elapsed = tabu_search(D, max_iters=2000, tabu_tenure=7)
        tabu_costs.append(cost)
        tabu_times.append(elapsed)
        tabu_iters.append(iters)
        results.append(('Tabu', r+1, cost, elapsed, iters))

    # Save CSV
    with open('results_experiments.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['algorithm','run','cost','time_s','iterations'])
        writer.writerows(results)

    def summarize(name, costs, times, iters):
        print(f"\n{name} summary:")
        print(f" best: {min(costs):.4f}, mean: {statistics.mean(costs):.4f}, std: {statistics.pstdev(costs):.4f}")
        print(f" time (s) mean: {statistics.mean(times):.4f}")
        print(f" iterations mean: {statistics.mean(iters):.1f}")

    summarize('Simulated Annealing', sa_costs, sa_times, sa_iters)
    summarize('Tabu Search', tabu_costs, tabu_times, tabu_iters)

if __name__ == '__main__':
    run()
