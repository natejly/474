from scoring import score_determ, score_prob
# GPT helped with obj --win logic becsause I didn't realize it was a different scoring logic
# refactored from OG code at 11:40 2/23
def scoring(p1_strat, p2_strat, values, p1_prob, p2_prob, obj):
    if obj == '--win':
        p1_score, p2_score = score_determ(p1_strat, p2_strat, values)
        if p1_score > p2_score:
            outcome = 1.0
        elif p1_score == p2_score:
            outcome = 0.5
        else:
            outcome = 0.0
        payoff = outcome * p2_prob
    elif obj == '--score':
        p1_score, _ = score_determ(p1_strat, p2_strat, values)
        payoff = p1_score * p2_prob
    elif obj == '--lottery':
        p1_score, _, _, _ = score_prob(p1_strat, p2_strat, values)
        payoff = p1_score * p2_prob
    
    return payoff

def get_payoffs(mixed, values, obj):
    payoffs = []
    for p1_strat, p1_prob in mixed:
        payoff = 0.0
        for p2_strat, p2_prob in mixed:
            payoff += scoring(p1_strat, p2_strat, values, p1_prob, p2_prob, obj)
        payoffs.append((p1_strat, payoff))
    return payoffs

def check_NE(mixed, values, tolerance, obj):
    # Check that every strategy in the support has (approximately) the same expected payoff.
    payoffs = get_payoffs(mixed, values, obj)
    mixed_payoffs = [p for _, p in payoffs]
    # check that all payoffs are the same
    # not technically needed but faster if we have non eq in straetgies
    for p in mixed_payoffs:
        if abs(p - mixed_payoffs[0]) > tolerance:
            return False
    # check that no deviant strategy can do better than the equilibrium
    eq = mixed_payoffs[0]
    for dev in find_permutations(len(mixed[0][0]), int(sum(mixed[0][0]))):
        dev_payoff = 0.0
        for opp_strat, opp_prob in mixed:
            dev_payoff += scoring(dev, opp_strat, values, 1.0, opp_prob, obj)
        if dev_payoff - tolerance > eq:
            return False
    return True

#GPT4 give python code for all permutations of a list length n that add up to m
def find_permutations(n, m):
    def backtrack(remaining, path):
        if len(path) == n:
            if sum(path) == m:
                results.add(tuple(path))  # Store unique permutations
            return
        for i in range(remaining + 1):  # Generate candidates
            backtrack(remaining - i, path + [i])
    results = set()
    backtrack(m, [])
    return list(results)

if __name__ == "__main__":
    values = [2, 4, 5]  
    mixed1 = [
    ([0, 0, 5], 0.07428558119961398),
    ([0, 1, 4], 0.0628572491429189),
    ([0, 2, 3], 0.0514285583023659),
    ([0, 3, 2], 0.10857121203986661),
    ([1, 0, 4], 0.13142860782053217),
    ([1, 1, 3], 0.01714278781855886),
    ([1, 2, 2], 0.017143017862373943),
    ([1, 3, 1], 0.13142851264458152),
    ([2, 0, 3], 0.10857157877490509),
    ([2, 1, 2], 0.05142853222724512),
    ([2, 2, 1], 0.06285716721342921),
    ([2, 3, 0], 0.074285740412162),
    ([3, 2, 0], 0.10857132632298054),
]

    print("Nash Equilibrium" if check_NE(mixed1, values, 1e-5) else "Not a Nash Equilibrium")
