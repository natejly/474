import sys
import itertools

def main():
    #arg one 
    player = None
    e_m = None
    p1_score = None
    roll_sum = None
    arguments = sys.argv[1:]
    if arguments[1] == "--one":
        player = 1
    elif arguments[1] == "--two":
        player = 2
    else:
        raise Exception("Invalid player argument")
    
    if arguments[2] == "--expect":
        e_m = "e"
    elif arguments[2] == "--move":
        e_m = "m"
    else:
        raise Exception("Invalid expect/move argument")
    
    #this is a string
    positions = arguments[3]
    
    if player == 2 and e_m == "m":
        p1_score = int(arguments[4])
        roll_sum = int(arguments[5])
    elif e_m == "m":
        roll_sum = int(arguments[4])
    elif player == 2:
        p1_score = int(arguments[4])

    
    

        





if __name__ == "__main__":
    main()
    