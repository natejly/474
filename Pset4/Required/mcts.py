import math
import random
import time

#https://www.youtube.com/watch?v=UXW2yZndl7U

#wrapper class
class Node:
    def __init__(self, position, parent = None, action = None):
        self.pos = position
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0
        self.actions = position.get_actions().copy()
    def is_fully_expanded(self):
        return len(self.actions) == 0 and len(self.children) > 0

def mcts_policy(limit):
    def policy_wrapper(position):
        return policy(position, limit=limit)
    return policy_wrapper

def ucb(node, c):
    if node.visits == 0:
        return float('inf')
    v = node.value / node.visits
    e = math.sqrt(math.log(node.parent.visits)/node.visits)
    ucb = v + c*e
    if node.parent.pos.actor() == 0:
        return ucb
    return -ucb

def add_children(node):
    action = node.actions.pop()
    state = node.pos.successor(action)
    child = Node(state, parent=node, action=action)
    node.children.append(child)
    return child
    
def best_child(node, c):
    return max(node.children, key=lambda child: ucb(child, c))

def traverse(node, c):
    current = node
    while not current.pos.is_terminal():
        if not current.is_fully_expanded():
            return add_children(current) 
        else:
            current = best_child(current, c)
    return current

def rollout(node):
    current = node
    while not current.is_terminal():
        actions = current.get_actions()
        action = random.choice(actions)
        current = current.successor(action)
    return current.payoff()  
    
def bp(node, val):
    current = node
    while current is not None:
        current.visits += 1
        if current.pos.actor() == 1:
            current.value += val  
        else:
            current.value -= val  
        current = current.parent
            
def policy(position, limit):
    root = Node(position)
    c = math.sqrt(2)
    start = time.time()
    while time.time() - start < limit:
        node = traverse(root, c)
        val = rollout(node.pos)
        bp(node,val)
        
    return max(root.children, key=lambda child: child.visits).action
    
        