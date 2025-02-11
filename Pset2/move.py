from ev import valid_moves, remove, p1_ev, p2_ev

p1_memo = {}
p2_memo = {}    

def get_p1_move(positions, roll):
    moves = valid_moves(positions, roll)
    best = None
    best_move = None
    for move in moves:
        # recursivley find the best move
        new_pos = remove(positions, move)
        temp = p1_ev(new_pos)
        if best is None or temp > best:
            best = temp
            best_move = move
    return best_move

def get_p2_move(positions, p1score, roll):
    moves = valid_moves(positions, roll)
    best = None
    best_move = None
    for move in moves:
        # recursiveley find the worst move
        new_pos = remove(positions, move)
        temp = p2_ev(new_pos, p1score)
        if best is None or temp < best:
            best = temp
            best_move = move
    return best_move
if __name__ == "__main__":
    positions = [1,4,6,7,8,9]
    roll = 9
    print(list(get_p1_move(positions, roll)))
    
    pos2 = [1,3,4,5,6,7,8,9]
    p1score = 17
    roll = 12
    
    print(list(get_p2_move(pos2, p1score, roll)))
    