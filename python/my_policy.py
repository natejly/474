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
        data = []
        with open("crib.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                # Convert each value from string to float
                data.append([float(value) for value in row])
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
        if i == 0 or j == 0:
            print("ERROR")
        number = self.data[i][j]
        return number


    def keep(self, hand, scores, am_dealer):
        # hand is a list of card scores 
        # maximize scoring for show, play, and crib(if dealer) else minimize opponent's scoring
        # keep in mind community card for potential crib
        # keep in mind community card for hand scoring 
        # synergy of 4 cards kept for scoring potential
        
        #eventually add in ability to know what cards have been played
    
        # get every possible combination of 4 cards from the 6 cards in hand
        #scores is a tuple of the form (player_score, opponent_score)
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
            total_ev = hand_ev + (crib_ev if am_dealer else -crib_ev) + peg_ev
            if total_ev > EV:
                EV = total_ev
                keep = list(combo)
                throw = list(discarded)
        # calculate the score of each combination and subtract EV of discarded if not dealer
        # create EV table for each possible combination of cards 
        # return the combination with the highest score
        # print(hand)
        return keep, throw
    
    def card_min(self, cards):
        min_card = cards[0]
        for card in cards:
            if card.rank() < min_card.rank():
                min_card = card
        return min_card
            
    def peg(self, cards, history, turn, scores, am_dealer):
        # return self._policy.peg(cards, history, turn, scores, am_dealer)
        # TODO: ask about this in OH
        sorted_cards = sorted(cards, key=lambda card: card.rank())
        # if we are leading 
        if history.is_start_round():
            # play card under 4
            for card in sorted_cards:
                if card.rank() <= 4:
                    return card
            # lead with one of two cards in hand that add to 15 that isn't a 5
            # classic twosum
            seen = set()
            # go through all cards and play highes???
            for card in sorted_cards: # TODO: ask if giving higher pair is better
                complement = 15 - card.rank()
                if complement in seen and card.rank() != 5:
                    return card
                seen.add(card.rank())

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
        




    

                                    
