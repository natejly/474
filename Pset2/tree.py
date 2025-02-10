from itertools import combinations
import time

class Node:
    def __init__(self, positions=[], parent=None):
        self.positions = positions
        self.terminal = False
        self.parent = parent
        self.children = []
        self.root = False
        self.win = False
        self.p = 0

root = Node()
root.root = True
memo = {}
def valid_moves(positions, roll):
    "Returns list of items that can possibly be shut"
    "if nothign is shut, return None"
    #check total positions

    moves = []
    for i in range(1, len(positions)+1):
        for combo in combinations(positions, i):
            if sum(combo) == roll:
                moves.append(combo)
    if moves == []:
        return None
    return moves
    
def remove(positions, move):
    "Removes all elements in move from positions"
    new_pos = positions.copy()
    for i in move:
        new_pos.remove(i)
    return new_pos
        
def evolutions(node):
    positions = node.positions
    
    if positions == []:
        node.terminal = True
        node.win = True
        return node.children
    
    key = tuple(positions)
    if key in memo:
        return memo[key]

    two_dice = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    one_dice = [1,2, 3, 4, 5, 6]
    if sum(positions) > 6:
        rolls = two_dice
    else:
        rolls = one_dice
    for roll in rolls:
        moves = valid_moves(positions, roll)
        if moves is None:
            child = Node(positions, node)
            child.terminal = True
            child.win = False
            node.children.append(child)
    
            continue
        for move in moves:
            new_pos = remove(positions, move)
            child = Node(new_pos, node)
            node.children.append(child)
            evolutions(child)
    
    memo[key] = node.children
    return node.children  

def print_tree(node, depth=0):
    indent = "    " * depth
    # Print current node positions.
    print(f"{indent}Node positions: {node.positions}", end="")
    if node.terminal:
        if node.win:
            print(" [Win]")
        else:
            print(" [Loss]")
    else:
        print("")
    # Recursively print children.
    for child in node.children:
        print_tree(child, depth + 1)
        
if __name__ == "__main__":
    start_time = time.time()
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    root = Node(positions)
    root.root = True
    evolutions(root)
    
    print("Time taken: ", time.time() - start_time)
    # print_tree(root)