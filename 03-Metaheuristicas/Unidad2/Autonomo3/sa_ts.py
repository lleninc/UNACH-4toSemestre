import math
import random
import time


class SAOptimizer:
    def __init__(self, evaluate, neighbor, initial_solution, max_iter=1000, T0=1.0, alpha=0.995):
        self.evaluate = evaluate
        self.neighbor = neighbor
        self.initial_solution = initial_solution
        self.max_iter = max_iter
        self.T0 = T0
        self.alpha = alpha

    def solve(self):
        s = self.initial_solution()
        best = s
        best_val = self.evaluate(best)
        curr = s
        curr_val = best_val
        T = self.T0
        iter_no_improve = 0
        for it in range(1, self.max_iter + 1):
            nxt = self.neighbor(curr)
            nxt_val = self.evaluate(nxt)
            delta = nxt_val - curr_val
            if delta < 0 or random.random() < math.exp(-delta / max(T, 1e-12)):
                curr, curr_val = nxt, nxt_val
            if curr_val < best_val:
                best, best_val = curr, curr_val
                iter_no_improve = 0
            else:
                iter_no_improve += 1
            T *= self.alpha
            if iter_no_improve > 200:
                break
        return {"solution": best, "value": best_val, "iterations": it}


class TabuSearchOptimizer:
    def __init__(self, evaluate, neighbor_generator, initial_solution, max_iter=1000, tabu_tenure=20, neighborhood_size=100):
        self.evaluate = evaluate
        self.neighbor_generator = neighbor_generator
        self.initial_solution = initial_solution
        self.max_iter = max_iter
        self.tabu_tenure = tabu_tenure
        self.neighborhood_size = neighborhood_size

    def _hash_solution(self, s):
        try:
            return tuple(round(float(x), 6) for x in s)
        except Exception:
            return tuple(s)

    def solve(self):
        s = self.initial_solution()
        best = s
        best_val = self.evaluate(best)
        curr = s
        curr_val = best_val
        tabu = {}
        iter_no_improve = 0
        for it in range(1, self.max_iter + 1):
            # generate neighborhood
            candidates = [self.neighbor_generator(curr) for _ in range(self.neighborhood_size)]
            candidates = list({self._hash_solution(c): c for c in candidates}.values())
            candidates_eval = [(c, self.evaluate(c)) for c in candidates]
            candidates_eval.sort(key=lambda x: x[1])
            chosen = None
            chosen_val = None
            for c, val in candidates_eval:
                h = self._hash_solution(c)
                if h not in tabu or val < best_val:  # aspiration
                    chosen, chosen_val = c, val
                    break
            if chosen is None:
                break
            # update
            curr, curr_val = chosen, chosen_val
            h_curr = self._hash_solution(curr)
            tabu[h_curr] = self.tabu_tenure
            # decay tabu
            for k in list(tabu.keys()):
                tabu[k] -= 1
                if tabu[k] <= 0:
                    del tabu[k]
            if curr_val < best_val:
                best, best_val = curr, curr_val
                iter_no_improve = 0
            else:
                iter_no_improve += 1
            if iter_no_improve > 200:
                break
        return {"solution": best, "value": best_val, "iterations": it}
