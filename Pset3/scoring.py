
def score_determ(p1, p2, values):
    "Function for derterministic scoring"
    p1_score = 0
    p2_score = 0
    for i in range(len(p1)):
        if p1[i] > p2[i]:
            p1_score += values[i]
        elif p1[i] == p2[i]:
            p1_score += values[i]/2
            p2_score += values[i]/2
        else:
            p2_score += values[i]
    return p1_score,p2_score

def score_prob(p1, p2, values):
    p1_probs = [0] * len(p1)
    p2_probs = [0] * len(p1)
    p1_score = 0
    p2_score = 0
    for i in range(len(p1)):
        p1v = p1[i]
        p2v = p2[i]
        if p1v == p2v == 0:
            p1_probs[i] = 0.5
            p2_probs[i] = 0.5
        elif p1v == 0:
            p1_probs[i] = 0.0
            p2_probs[i] = 1.0
        elif p2v == 0:
            p1_probs[i] = 1.0
            p2_probs[i] = 0.0
        else:
            p1_probs[i] = (p1v**2) / ((p1v**2) + (p2v**2))
            p2_probs[i] = 1 - p1_probs[i]
        p1_score += p1_probs[i] * values[i]
        p2_score += p2_probs[i] * values[i]
    return p1_score, p2_score, p1_probs, p2_probs


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    p1 = [1, 0, 4, 5]
    p2 = [1, 1, 3, 5]
    
    print("Deterministic scoring:")
    p1_score, p2_score = score_determ(p1, p2, values)
    print(f"Player 1 score: {p1_score}")
    print(f"Player 2 score: {p2_score}")
    print("Probabilistic scoring:")
    p1_score, p2_score, p1_probs, p2_probs = score_prob(p1, p2, values)
    print(f"Player 1 score: {p1_score}")
    print(f"Player 2 score: {p2_score}")
    