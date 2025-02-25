from verify import find_permutations, scoring


def find_mixed_strategies(units, values, tolerance, obj):
    possible = find_permutations(len(values), units)
    strategy_profiles = []
    eq = 0
    for strat in possible:
        payoff = 0
        for opp_strat in possible:
            payoff += scoring(strat, opp_strat, values, 1.0, 1.0, obj)
        if payoff > eq + tolerance:
            eq = payoff
            strategy_profiles = [strat]
        elif abs(payoff - eq) < tolerance:
            strategy_profiles.append(strat)
    
    num_best = len(strategy_profiles)
    if num_best == 0:
        return []
    probability = 1.0 / num_best
    # Return a list of (pure_strategy, probability) tuples.
    return [(s, probability) for s in strategy_profiles]
    
    
    
    
    
if __name__ == "__main__":
    units = 2
    values = [1, 2]
    obj = "--win"
    print(find_mixed_strategies(units, values, 1e-5, obj))