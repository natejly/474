import sys
import itertools
from itertools import combinations
from tree import Node, Tree, tree_gen, leaf_gen

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
    player, e_m, p1_score, roll_sum, positions = read_input()
    print("player: ", player)
    print("e_m: ", e_m)
    print("p1_score: ", p1_score)
    print("roll_sum: ", roll_sum)
    print("positions: ", positions)
    # print("rolls: ", rolls)
    tree = tree_gen(positions)
    leaf_gen(tree.root)
    
    



    
if __name__ == "__main__":
    main()

