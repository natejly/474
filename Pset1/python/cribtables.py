import csv
from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
from itertools import combinations
from scoring import score
from deck import Card
import random
from cribbage import Game, evaluate_policies
import time

itters = 10000000
start_time = time.time()

full_deck = [Card(rank, suit) for rank in range(1, 14) for suit in ['S', 'H', 'D', 'C']]

my_crib = [[0.0 for _ in range(14)] for _ in range(14)]

game = Game()

def number_to_card(num):
    return Card(num, 'S')

def get_ev(i, j):
    crib = [number_to_card(i), number_to_card(j)]
    possible_turn_cards = list(set(full_deck) - set(crib))  

    my_score = 0
    
    for turn_card in possible_turn_cards:
        remaining_cards = list(set(full_deck) - {crib[0], crib[1], turn_card})
        all_combos = list(combinations(remaining_cards, 2))
        random.shuffle(all_combos)
        test_combos = all_combos[:itters]

        for card1, card2 in test_combos:
            temp_crib = crib + [card1, card2]
            my_score += score(game, temp_crib, turn_card, True)[0]

    total_count = len(possible_turn_cards) * len(test_combos)
    return (my_score / total_count) if total_count else 0.0

for i in range(1, 14):
    for j in range(1, 14):
        my_crib[i][j] = get_ev(i, j)

end_time = time.time()
print(f"TIME TAKEN: {end_time - start_time:.2f} seconds")
print(f'NUM ITTERS: {itters}')

print("CRIB TABLE:")
for row in my_crib:
    print(row)

with open("crib.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(my_crib)
