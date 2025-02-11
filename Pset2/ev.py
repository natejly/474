from itertools import combinations
import time

memo = {}    

def two_dice():
    return [
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 4),
        (6, 5),
        (7, 6),
        (8, 5),
        (9, 4),
        (10, 3),
        (11, 2),
        (12, 1)
    ]
    
def one_dice():
    return [(1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6)]

def valid_moves(positions, roll):
    "Returns list of items that can possibly be shut"
    "if nothign is shut, return None"
    moves = []
    #this part was GPT "give me function that takes in list and gives all subsets that equal to an int argument"
    for i in range(1, len(positions)+1):
        for combo in combinations(positions, i):
            if sum(combo) == roll:
                moves.append(combo)
    if moves == []:
        return None
    return moves
    #origionally was having trouble because wasn't copying the list but GPT fixed for me
def remove(positions, move):
    "Removes all elements in move from positions"
    new_pos = positions.copy()
    for i in move:
        new_pos.remove(i)
    return new_pos

def p2_ev(positions, p1score):
    "want to play the lowest score and retuns expected outcome"
    "returns expected outcome for player 1"
    if positions == []:
        return 0
    # check if memoized
    key = (tuple(positions), p1score)
    if key in memo:
        return memo[key]
    value = 0 
    # two dice if sum of pos > 6
    if sum(positions) > 6:
        possible_rolls = two_dice()
    else:
        possible_rolls = one_dice()
    # itter through rolls and probs to get EV 
    # EV is sum of probability of getting to each node * reward
    for pair in possible_rolls:
        roll = float(pair[0])
        prob = float(pair[1])/36
        moves = valid_moves(positions, roll)
        best = None
        # terminal
        if moves == None:
            # game scoring logic
            score = sum(positions)
            if score > p1score:
                value += prob * 1
            if score == p1score:
                value += prob * 0.5
            if score < p1score:
                value += prob * 0
        else:
            # not terminal
            for move in moves:
                # recursiveley find the worst move
                new_pos = remove(positions, move)
                temp = p2_ev(new_pos, p1score)
                # less than here because our optimal move is to minimize our score in golf terms
                if best is None or temp < best:
                    best = temp
            value += prob * best
    memo[key] = value
    return value

def p1_ev(positions):
    "gets player 1's expected value given positions"
    "recursive function that gets EV of node"
    # terminal condition if pos is empty box is shut
    if positions == []:
        return 1
    # check if memoized
    key = tuple(positions)
    value = 0 
    if key in memo:
        return memo[key]
    
    if sum(positions) > 6:
        possible_rolls = two_dice()
    else:
        possible_rolls = one_dice()
    for pair in possible_rolls:
        # itter through rolls and probs to get EV 
        roll = float(pair[0])
        prob = float(pair[1])/36
        moves = valid_moves(positions, roll)
        best = None
        if moves is None:
            score = sum(positions)
            value += prob * p2_ev([1,2,3,4,5,6,7,8,9], score)
        else:
            for move in moves:
                # recursivley find the best move
                new_pos = remove(positions, move)
                temp = p1_ev(new_pos)
                if best is None or temp > best:
                    best = temp
            value += prob * best
    memo[key] = value
    return value

    

if __name__ == "__main__":
    start_time = time.time()
    positions = [1,2, 3, 4, 5, 6, 7, 8, 9]
    pos2 = [1,4,6,7,8,9]
    ev = p1_ev(positions)
    print(ev)

    print("Time taken: ", time.time() - start_time)
