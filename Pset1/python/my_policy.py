from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
from itertools import combinations
from scoring import score
from deck import Card
import csv

class MyPolicy(CribbagePolicy):
    def __init__(self, game):
        self._policy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        self._game = game
        self._full_deck = [Card(rank, suit) for rank in self._game.all_ranks() for suit in self._game.all_suits()]
        # Method for generating the table is commented out below working code
        # I saved to csv for temporary testing and then converted to a hardcoded list
        data = [
            [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, 5.738087234893958, 4.476989795918367, 4.596989795918367, 5.505765306122449, 5.7685204081632655, 4.295051020408163, 4.116887755102041, 4.160255102040816, 4.076173469387755, 3.9941326530612247, 4.2125, 3.8920918367346937, 3.783520408163265],
            [0.0, 4.476989795918367, 6.039263705482193, 6.874744897959184, 4.883112244897959, 5.797908163265306, 4.403724489795918, 4.318724489795918, 4.270663265306123, 4.174132653061225, 4.106581632653061, 4.324948979591837, 4.00454081632653, 3.895969387755102],
            [0.0, 4.596989795918367, 6.874744897959184, 6.3975830332132855, 5.534132653061224, 6.4634183673469385, 4.31015306122449, 4.391275510204082, 4.326377551020408, 4.152193877551021, 4.181887755102041, 4.400255102040816, 4.0798469387755105, 3.9712755102040815],
            [0.0, 5.505765306122449, 4.883112244897959, 5.534132653061224, 6.370020008003201, 7.032602040816326, 5.003520408163265, 4.215255102040817, 4.339642857142858, 4.23984693877551, 4.178418367346938, 4.3967857142857145, 4.076377551020408, 3.96780612244898],
            [0.0, 5.7685204081632655, 5.797908163265306, 6.4634183673469385, 7.032602040816326, 9.33280512204882, 7.1275, 6.449948979591837, 5.792397959183673, 5.77219387755102, 7.062602040816326, 7.280969387755102, 6.960561224489796, 6.851989795918367],
            [0.0, 4.295051020408163, 4.403724489795918, 4.31015306122449, 5.003520408163265, 7.1275, 6.525602240896359, 5.574948979591837, 4.936581632653061, 5.613724489795918, 3.8759693877551022, 4.0943367346938775, 3.7739285714285713, 3.6653571428571428],
            [0.0, 4.116887755102041, 4.318724489795918, 4.391275510204082, 4.215255102040817, 6.449948979591837, 5.574948979591837, 6.3467787114845935, 6.801071428571428, 4.389642857142857, 3.762295918367347, 4.041071428571429, 3.7206632653061225, 3.612091836734694],
            [0.0, 4.160255102040816, 4.270663265306123, 4.326377551020408, 4.339642857142858, 5.792397959183673, 4.936581632653061, 6.801071428571428, 5.845266106442577, 4.967602040816327, 4.340255102040817, 3.9645408163265308, 3.7045408163265305, 3.595969387755102],
            [0.0, 4.076173469387755, 4.174132653061225, 4.152193877551021, 4.23984693877551, 5.77219387755102, 5.613724489795918, 4.389642857142857, 4.967602040816327, 5.743657462985194, 4.881887755102041, 4.506173469387755, 3.5916836734693875, 3.5435204081632654],
            [0.0, 3.9941326530612247, 4.106581632653061, 4.181887755102041, 4.178418367346938, 7.062602040816326, 3.8759693877551022, 3.762295918367347, 4.340255102040817, 4.881887755102041, 5.679311724689876, 5.066989795918367, 4.1525, 3.44984693877551],
            [0.0, 4.2125, 4.324948979591837, 4.400255102040816, 4.3967857142857145, 7.280969387755102, 4.0943367346938775, 4.041071428571429, 3.9645408163265308, 4.506173469387755, 5.066989795918367, 6.144345738295318, 5.029030612244898, 4.326377551020408],
            [0.0, 3.8920918367346937, 4.00454081632653, 4.0798469387755105, 4.076377551020408, 6.960561224489796, 3.7739285714285713, 3.7206632653061225, 3.7045408163265305, 3.5916836734693875, 4.1525, 5.029030612244898, 5.471100440176071, 4.005969387755102],
            [0.0, 3.783520408163265, 3.895969387755102, 3.9712755102040815, 3.96780612244898, 6.851989795918367, 3.6653571428571428, 3.612091836734694, 3.595969387755102, 3.5435204081632654, 3.44984693877551, 4.326377551020408, 4.005969387755102, 5.259815926370548],
        ]
        self.data = data        

    def get_hand_ev(self, hand, discarded):
        other_cards = [card for card in self._full_deck if card not in hand and card not in discarded]
        total = 0
        for card in other_cards:
            #all combos of hand and community card
            score_list = score(self._game, hand, card, False)
            total += score_list[0]  #TODO: Ask if I need to include turn card
        EV = total / len(other_cards)
        return EV
    def get_crib_ev(self, hand, discarded):
        # # get 46 other cards that are not in the hand 
        # other_cards = [card for card in self._full_deck if card not in hand and card not in discarded]
        # total = 0
        # for card in other_cards:
        #     score_list = score(self._game, discarded, card, True)
        #     total += score_list[0] #TODO: Ask if I need to include turn card
        # EV = total / len(other_cards)
        # # print(EV)
        # return EV
        i = discarded[0].rank() 
        j = discarded[1].rank()
        # if i == 0 or j == 0:
        #     print("ERROR")
        number = self.data[i][j]
        return number


    def keep(self, hand, scores, am_dealer):
        # return self._policy.keep(hand, scores, am_dealer)

        EV = -100
        keep = None
        throw = None
        hands = combinations(hand, 4)
        # print(hand)
        for combo in hands:
            discarded = list(set(hand) - set(combo))
            hand_ev = self.get_hand_ev(combo, discarded)
            crib_ev = self.get_crib_ev(combo, discarded)
            peg_ev = 0
            # next line was by GPT because I didn't like the if statment and forgot python syntax
            total_ev = hand_ev + (crib_ev if am_dealer else -crib_ev) + peg_ev
            if total_ev > EV:
                EV = total_ev
                keep = list(combo)
                throw = list(discarded)
        return keep, throw

    def peg(self, cards, history, turn, scores, am_dealer):
        # return self._policy.peg(cards, history, turn, scores, am_dealer)
        sorted_cards = sorted(cards, key=lambda card: card.rank())
        # if we are leading 
        if history.is_start_round():
            # play card under 4
            for card in sorted_cards:
                if card.rank() <= 4:
                    return card
            # I had a double for loop that checked if cards weren't a 5 and added to 15
            # but then gave my code to GPT and I told it to use a set and complements for speed
            # Like the leetcode twosum problem
            seen = set()
            for card in sorted_cards: 
                complement = 15 - card.rank()
                if complement in seen and card.rank() != 5:
                    return card
                seen.add(card.rank())
                
        # following chunk was taken from the greedy pegging policy
        best_card = None
        best_score = None
        for card in cards:
            score = history.score(self._game, card, 0 if am_dealer else 1)
            if score is not None and (best_score is None or score > best_score):
                best_score = score
                best_card = card
        if best_card is not None and best_score > 0:
            return best_card
        
        # TODO: can do this in one for loop
        reversed_cards = sorted(cards, key=lambda card: card.rank(), reverse=True)
        # play highest legal card to complete 31
        for card in reversed_cards:
            if history.score(self._game, card, 0 if am_dealer else 1) is not None:
                return card
# CSV TO LIST FUNCTION GENERATED BY CHATGPT
# def csv_to_list(input_csv, output_txt):
#     # Read CSV and convert to a list of lists
#     csv_list = []
#     with open(input_csv, 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             csv_list.append(row)
    
#     # Write the Python list to a text file
#     with open(output_txt, 'w') as file:
#         file.write("csv_list = [\n")
#         for row in csv_list:
#             file.write(f"    {row},\n")
#         file.write("]\n")

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





    

                                    
