import time
import csv
from pathlib import Path
from sa_ts import SAOptimizer, TabuSearchOptimizer
from problems import SphereProblem, TSPProblem


def run_on_problem(name, problem, sa_params=None, ts_params=None, runs=10):
    sa_params = sa_params or {}
    ts_params = ts_params or {}
    results = []
    for r in range(runs):
        # SA
        sa = SAOptimizer(evaluate=problem.evaluate, neighbor=problem.neighbor, initial_solution=problem.initial_solution, **sa_params)
        t0 = time.time()
        res_sa = sa.solve()
        t_sa = time.time() - t0
        # TS
        ts = TabuSearchOptimizer(evaluate=problem.evaluate, neighbor_generator=problem.neighbor, initial_solution=problem.initial_solution, **ts_params)
        t0 = time.time()
        res_ts = ts.solve()
        t_ts = time.time() - t0
        results.append({
            'problem': name,
            'run': r + 1,
            'sa_value': res_sa['value'],
            'sa_iterations': res_sa['iterations'],
            'sa_time': t_sa,
            'ts_value': res_ts['value'],
            'ts_iterations': res_ts['iterations'],
            'ts_time': t_ts,
        })
    return results


def main():
    all_results = []
    # Sphere
    sphere = SphereProblem(dim=10)
    all_results += run_on_problem('Sphere5', sphere, sa_params={'max_iter': 1500, 'T0': 10.0, 'alpha': 0.995}, ts_params={'max_iter': 2000, 'tabu_tenure': 30, 'neighborhood_size': 200}, runs=5)
    # TSP
    tsp = TSPProblem()
    all_results += run_on_problem('TSP5', tsp, sa_params={'max_iter': 1500, 'T0': 10.0, 'alpha': 0.995}, ts_params={'max_iter': 2000, 'tabu_tenure': 50, 'neighborhood_size': 300}, runs=5)

    # save csv
    keys = ['problem', 'run', 'sa_value', 'sa_iterations', 'sa_time', 'ts_value', 'ts_iterations', 'ts_time']
    output_path = Path(__file__).with_name('results_autonomo3.csv')
    with output_path.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        for row in all_results:
            writer.writerow(row)

    print(f'Experimentos completados. Resultados guardados en {output_path.name}')


if __name__ == '__main__':
    main()
