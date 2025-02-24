from scoring import score_determ, score_prob
# check whether both players playing mixed strategy is an equilibrium
def get_payoffs(mixed, values, determ = True):
    payoffs = []
    for p1_strat, p1_prob in mixed:
        payoff = 0
        for p2_strat, p2_prob in mixed:
            if determ:
                p1_score, p2_score = score_determ(p1_strat, p2_strat, values)
            else:
                p1_score, p2_score, _, _ = score_prob(p1_strat, p2_strat, values)   
            payoff += p1_score * p2_prob
            
        payoffs.append((p1_strat, payoff))
    return payoffs

def check_NE(mixed, values, tolerance, determ = True):
    payoffs = get_payoffs(mixed, values, determ)
    # print (payoffs)
    # check that app payoffs are equal for played strat
    mixed_payoffs = [p1_payoff for _, p1_payoff in payoffs]
    max_payoff = max(mixed_payoffs)
    min_payoff = min(mixed_payoffs) 
    if max_payoff - min_payoff > tolerance:
        return False
    best_score = best_response(mixed, values, determ)
    # if best_score > max_payoff + tolerance:
    #     return False
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

def best_response(mixed, values, determ = True):
    deviant = find_permutations(len(values), int(sum(mixed[0][0])))
    # print(deviant)
    best_score = 0
    for p1_strat, p1_prob in mixed:
        for strat in deviant:
            if determ:
                p1_score, p2_score = score_determ(p1_strat, strat, values)
            else:
                p1_score, p2_score, _, _ = score_prob(p1_strat, strat, values) 
            if p2_score > best_score:
                best_score = p2_score
    return best_score
                  






if __name__ == "__main__":
    values = [1, 1]  
    mixed1 = [([1, 0], 1),]
    best_response(mixed1, values)
    print("Nash Equilibrium" if check_NE(mixed1, values, 1e-5) else "Not a Nash Equilibrium")
