import math
import random
import time

C = math.sqrt(2)
total_iterations = 0
# https://www.youtube.com/watch?v=UXW2yZndl7U
class Node():
    def __init__(self, position, parent=None, move=None):
        self.pos = position
        self.parent = parent
        self.children = []
        self.visits = 0
        self.value = 0
        self.move = move
        if position.is_terminal():
            self.possible_moves = []
        else:
            self.possible_moves = position.get_actions()

def is_min(node):
    return node.pos.actor() == 0

def is_leaf(node):
    return node.pos.is_terminal()

def ucb(node):
    ave_val = node.value / node.visits
    explore = C * math.sqrt(math.log(node.parent.visits) / node.visits)
    if is_min(node.parent):
        return ave_val + explore
    else:
        return explore - ave_val

# def uct(node):
#     ave_val = node.value / node.visits
#     explore = C * math.sqrt(math.log(total_iterations) / node.visits)
#     if is_min(node.parent):
#         return ave_val + explore
#     else:
#         return explore - ave_val
def traverse(node, end):
    current = node
    while True:
        # terminal
        if is_leaf(current):
            return current
        # if we have unused moves 
        if current.possible_moves:
            move = current.possible_moves.pop()
            child_pos = current.pos.successor(move)
            child = Node(child_pos, current, move)
            child.visits = 1
            current.children.append(child)
            return child
        # not terminal all moves used recurse on max ucb
        current = max(current.children, key=lambda x: ucb(x))
        # if time.time() >= end:
        #     return None
    
def rollout(node, end):
    current = node.pos
    while True:
        # if time.time() >= end:
        #     return None
        if current.is_terminal():
            return current.payoff()
        actions = current.get_actions()
        if not actions:  
            return current.payoff()
        action = random.choice(actions)
        current = current.successor(action)
    
def bp(node, payoff):
    current = node
    while current:
        current.value += payoff
        current.visits += 1
        current = current.parent
    
def policy(position, limit):
    # global total_iterations
    root = Node(position)
    root.visits = 1  
    start = time.time()
    end = start + limit
    while True:
        if time.time() >= end:
            break
        node = traverse(root, end)
        # if node is None:
        #     break
        payoff = rollout(node, end)
        # if payoff is None:
        #     break
        bp(node, payoff)
    # total_iterations += 1  
    # print("taken : " + str(time.time() - start))
    if root.children == []:
        return random.choice(root.possible_moves) 
    best_child = max(root.children, key=lambda x: x.visits)
    return best_child.move
    # for move in position.get_actions():
    #     child_pos = position.successor(move)
    #     if child_pos == best_child.pos:
    #         return move

def mcts_policy(limit):
    def policy_wrapper(position):
        return policy(position, limit=limit)
    return policy_wrapper