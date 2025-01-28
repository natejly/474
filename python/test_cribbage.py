import sys
import time
import math
import itertools as it

from policy import CompositePolicy, RandomThrower, RandomPegger, GreedyThrower, GreedyPegger
from cribbage import Game, evaluate_policies
from my_policy import MyPolicy

if __name__ == "__main__":
    start_time = time.time()

    games = 100000
    run_time = 0
    if len(sys.argv) > 1:
        if sys.argv[1] == "--time":
            run_time = int(sys.argv[2]);
            games = 1000
        else:
            games = int(sys.argv[1])
    
    game = Game()
    benchmark = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
    submission = MyPolicy(game)
    total_games = 0

    match_values = list(it.chain(range(1, 4), range(-3, 0)))
    results = {value: 0 for value in match_values}
    start_time = time.time()
    while total_games == 0 or time.time() - start_time < run_time:
        batch_results = evaluate_policies(game, submission, benchmark, games)
        total_games += games
        for v in batch_results[3]:
            results[v] += batch_results[3][v]

    sum_squares = sum(results[v] * v * v for v in match_values)
    sum_values = sum(results[v] * v for v in match_values)
    mean = sum_values / total_games
    variance = sum_squares / total_games - math.pow(sum_values / total_games, 2)
    stddev = math.sqrt(variance)
    
    end_time = time.time() 
    print(f"TIME TAKEN: {end_time - start_time:.2f} seconds")

    print("NET:", mean)
    print("CONF:", mean - 2 * (stddev / math.sqrt(total_games)))
    print(results)

# CODE USED TO GENERATE TABLE
# import csv
# from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
# from itertools import combinations
# from scoring import score
# from deck import Card
# import random
# from cribbage import Game, evaluate_policies
# import time

# itters = 10000000
# start_time = time.time()

# full_deck = [Card(rank, suit) for rank in range(1, 14) for suit in ['S', 'H', 'D', 'C']]

# my_crib = [[0.0 for _ in range(14)] for _ in range(14)]

# game = Game()

# def number_to_card(num):
#     return Card(num, 'S')

# def get_ev(i, j):
#     crib = [number_to_card(i), number_to_card(j)]
#     possible_turn_cards = list(set(full_deck) - set(crib))  

#     my_score = 0
    
#     for turn_card in possible_turn_cards:
#         remaining_cards = list(set(full_deck) - {crib[0], crib[1], turn_card})
#         all_combos = list(combinations(remaining_cards, 2))
#         random.shuffle(all_combos)
#         test_combos = all_combos[:itters]

#         for card1, card2 in test_combos:
#             temp_crib = crib + [card1, card2]
#             my_score += score(game, temp_crib, turn_card, True)[0]

#     total_count = len(possible_turn_cards) * len(test_combos)
#     return (my_score / total_count) if total_count else 0.0

# for i in range(1, 14):
#     for j in range(1, 14):
#         my_crib[i][j] = get_ev(i, j)

# end_time = time.time()
# print(f"TIME TAKEN: {end_time - start_time:.2f} seconds")
# print(f'NUM ITTERS: {itters}')

# print("CRIB TABLE:")
# for row in my_crib:
#     print(row)

# with open("crib.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(my_crib)
