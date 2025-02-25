import sys
import math
from verify import get_payoffs, check_NE
from find import find_mixed_strategy
def read_input():
    f_v = None
    tolerance = float(1e-6)
    w_s_l = None
    units = None
    values = None
    args = sys.argv
    mixed = []

    if args[1] == "--find":
        f_v = "f"
    elif args[1] == "--verify":
        f_v = "v"

    if args[2] == "--tolerance":
        tolerance = float(args[3])
        w_s_l = args[4]
        if f_v == "f":
            if args[5] == "--units":
                units = int(args[6])
                values = [int(i) for i in args[7:]]
            else:
                values = [int(i) for i in args[5:]]
        else:
            values = [int(i) for i in args[5:]]
    else:
        w_s_l = args[2]
        if f_v == "f":
            if args[3] == "--units":
                units = int(args[4])
                values = [int(i) for i in args[5:]]
            else:
                values = [int(i) for i in args[3:]]
        else:
            values = [int(i) for i in args[3:]]
    # had GPT help with reading and added the .strip and .splitlines()
    if f_v == "v":
        std_in = sys.stdin.read().strip() 
        for line in std_in.splitlines():  
            terms = line.strip().split(",") 
            strat = [float(x) for x in terms[:-1]]  
            prob = float(terms[-1])  
            mixed.append((strat, prob))
            

    return f_v, tolerance, w_s_l, units, values, mixed

def main():
    f_v, tolerance, w_s_l, units, values, mixed = read_input()
    determ = True
    if f_v == "v":
        if check_NE(mixed, values, tolerance, w_s_l):
            print("PASSED")
        else:
            print("Nope")
    elif f_v == "f":
        prob, strategies = find_mixed_strategy(units, values, tolerance, w_s_l)
        for s, p in zip(strategies, prob):
            if p > tolerance:
                print(f"{','.join(map(str, s))},{p}")
        
        
    
if __name__ == "__main__":
    main()

