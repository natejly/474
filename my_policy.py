from policy import CribbagePolicy, CompositePolicy, GreedyThrower, GreedyPegger
from itertools import combinations
from scoring import score
from deck import Card
class MyPolicy(CribbagePolicy):
    def __init__(self, game):
        self._policy = CompositePolicy(game, GreedyThrower(game), GreedyPegger(game))
        self._game = game
        self._full_deck = [Card(rank, suit) for rank in self._game.all_ranks() for suit in self._game.all_suits()]


    def get_hand_ev(self, hand, discarded):
        
        other_cards = [card for card in self._full_deck if card not in hand and card not in discarded]
        total = 0
        for card in other_cards:
            #all combos of hand and community card
            score_list = score(self._game, hand, card, False)
            total += score_list[1] + score_list[2] + score_list[3] + score_list[4]
        EV = total / len(other_cards)
        return EV
    def get_crib_ev(self, hand, discarded):
        # get 46 other cards that are not in the hand 
        other_cards = [card for card in self._full_deck if card not in hand and card not in discarded]
        total = 0
        for card in other_cards:
            score_list = score(self._game, discarded, card, True)
            total += score_list[1] + score_list[2] + score_list[3] + score_list[4]
        EV = total / len(other_cards)
        # print(EV)
        return EV


    def keep(self, hand, scores, am_dealer):
        # hand is a list of card scores 
        # maximize scoring for show, play, and crib(if dealer) else minimize opponent's scoring
        # keep in mind community card for potential crib
        # keep in mind community card for hand scoring 
        # synergy of 4 cards kept for scoring potential
        
        #eventually add in ability to know what cards have been played
    
        # get every possible combination of 4 cards from the 6 cards in hand
        #scores is a tuple of the form (player_score, opponent_score)
        EV = 0
        keep = None
        throw = None
        hands = combinations(hand, 4)
        # print(hand)
        for combo in hands:
            discarded = set(hand) - set(combo)
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

    def peg(self, cards, history, turn, scores, am_dealer):
                #greedy agent plays card that maximizes its score 

        return self._policy.peg(cards, history, turn, scores, am_dealer)



    

                                    
