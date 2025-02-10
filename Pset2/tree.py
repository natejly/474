from itertools import combinations
import time
class Node:
    def __init__(self, positions, turn=None, parent=None):
        self.parent = parent
        self.p1score = 0
        self.p2score = 0
        self.turn = turn
        self.children = []
        self.positions = positions

class Tree:
    def __init__(self, root):
        self.root = root
memo = {}

def tree_gen(positions):
    head = Node(positions)
    tree = Tree(head)
    return tree

# GPT return list of all numbers under x that can add up to x
def all_nums(i):
    numbers = list(range(1, i+1))
    subsets = []
    # subsets.append(i)
    for r in range(1, len(numbers) + 1):
        for subset in combinations(numbers, r):
            if sum(subset) == i:
                subsets.append(subset)
    return subsets

def leaf_gen(node):
    # If the node is terminal, return.
    if node.positions == []:
        return None

    # Use the tuple of positions as a memo key.
    key = tuple(node.positions)
    if key in memo:
        return memo[key]

    # For each dice roll from 2 to 12...
    for x in range(2, 13):
        sets = all_nums(x)
        for s in sets:
            comp = node.positions[:]  
            valid = True
            # Remove the numbers of the move from the copy if they exist.
            for num in s:
                if num in comp:
                    comp.remove(num)
                else:
                    valid = False
                    break
            if valid:
                temp = Node(comp, parent=node)
                node.children.append(temp)
                temp.p1score += sum(temp.positions)
                # Recurse on the newly created node.
                leaf_gen(temp)
    memo[key] = node
    return node

if __name__ == "__main__":
    start = time.time()
    positions = [1,2,3,4,5,6,7,8,9]
    tree = tree_gen(positions)
    leaf_gen(tree.root)
    end = time.time()
    print("Time: ", end-start)
