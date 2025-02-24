import sys
import math
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

    if f_v == "v":
        std_in = sys.stdin.read()
        for line in std_in:
            terms = line.split(",")
            strat = [int(x) for x in terms[:-1]]
            prob = float(terms[-1])
            mixed.append((strat, prob))
            
            

            
    return f_v, tolerance, w_s_l, units, values, mixed

