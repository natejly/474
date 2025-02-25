from verify import find_permutations, scoring
import sys
import numpy as np
from scipy.optimize import linprog
from scoring import score_determ, score_prob

def get_matrix(units, values, tolerance, obj):
    strategies = sorted(find_permutations(len(values), units))
    matrix = np.zeros((len(strategies), len(strategies)))
    for i, p1_strat in enumerate(strategies):
        for j, p2_strat in enumerate(strategies):
            payoff = scoring(p1_strat, p2_strat, values, 1.0, 1.0, obj)
            matrix[i][j] = payoff
    return matrix, strategies

def find_mixed_strategy(units, values, tolerance, obj):
    payoff_matrix, strategies = get_matrix(units, values, tolerance, obj)
    n = len(strategies)
    # (v, strats ...)
    c = np.zeros(n + 1)
    c[-1] = -1 
    A_ub = -payoff_matrix.T
    A_ub = np.hstack((A_ub, (np.ones((n, 1)))))
    b_ub = np.zeros(n)
    # constrain probs to adding to 1
    A_eq = [[1]*n + [0]] 
    b_eq = [1] 
    res = linprog(c, A_ub, b_ub, A_eq, b_eq, method="highs")
    prob = res.x[:-1]
    return prob, strategies

if __name__ == "__main__":
    units = 5
    values = [2, 4, 5]
    obj = "--win"

    prob, strategies = find_mixed_strategy(units, values, obj)
    print("Optimal Mixed Strategy:")
    for strat, prob in zip(strategies, prob):
        print(f"  Strategy {strat}: {prob:.4f}")
