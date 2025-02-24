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
    print (payoffs)
    # check that app payoffs are equal for played strat
    for i in range(len(payoffs)):
        p1_strat, p1_payoff = payoffs[i]
        for j in range(len(payoffs)):
            p2_strat, p2_payoff = payoffs[j]
            if i != j:
                if abs(p1_payoff - p2_payoff) > tolerance:
                    return False

    return True


if __name__ == "__main__":
    values = [2, 4, 5]  
    mixed1 = [
        ([0, 0, 5], 0.14045462101642173),
        ([0, 1, 4], 0.15496211495866577),
        ([0, 2, 3], 0.04541673569373383),
        ([0, 3, 2], 0.05992422986845587),
        ([1, 0, 4], 0.08473480443797905),
        ([1, 1, 3], 0.09503788495378677),
        ([1, 2, 2], 0.17977268944230548),
        ([1, 3, 1], 0.1404546206153363),
        ([1, 4, 0], 0.04962114905424416),
        ([2, 3, 0], 0.04962114943279007)
    ]
    print("Nash Equilibrium" if check_NE(mixed1, values, 1e-5) else "Not a Nash Equilibrium")
