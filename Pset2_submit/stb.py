import sys
from ev import p1_ev, p2_ev
from move import get_p1_move, get_p2_move
import time
def read_input():
    player = None
    e_m = None
    p1_score = None
    roll_sum = None
    arguments = sys.argv
    if arguments[1] == "--one":
        player = 1
    elif arguments[1] == "--two":
        player = 2
    else:
        print(arguments[1])
        raise Exception("Invalid player argument")
    
    if arguments[2] == "--expect":
        e_m = "e"
    elif arguments[2] == "--move":
        e_m = "m"
    else:
        raise Exception("Invalid expect/move argument")
    
    #this is a string
    positions = arguments[3]
    positions = [int(i) for i in positions]

    if player == 2 and e_m == "m":
        p1_score = int(arguments[4])
        roll_sum = int(arguments[5])
    elif e_m == "m":
        roll_sum = int(arguments[4])
    elif player == 2:
        p1_score = int(arguments[4])
    return player, e_m, p1_score, roll_sum, positions
    
def main():
    start = time.time()
    player, e_m, p1_score, roll_sum, positions = read_input()
    if e_m == "e":
        if player == 1:
            print(f"{p1_ev(positions):.6f}")
        else:
            print(f"{1-p2_ev(positions, p1_score):.6f}")
    if e_m == "m":
        if player == 1:
            print(list(get_p1_move(positions, roll_sum)))
        else:
            print(list(get_p2_move(positions, p1_score, roll_sum)))

if __name__ == "__main__":
    main()

