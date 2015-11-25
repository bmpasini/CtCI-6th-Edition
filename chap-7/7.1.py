# Design the data structures for a generic deck of cards. Explain how you would
# subclass the data structures to implement blackjack.

from random import random
from math import floor

class Suit(object): pass
class Clubs(Suit): pass
class Hearts(Suit): pass
class Spades(Suit): pass
class Diamonds(Suit): pass


class Card(object):
    
    def __init__(self, face_value, suit):
        self.face_value = face_value
        self.suit = suit
        self.available = True

    def value(self):
        raise NotImplementedError("Abstract method.")

    def is_ace(self):
        return self.face_value == 1


class Deck(object):
    
    def __init__(self):
        self.reset_deck()

    def reset_deck(self):
        self.cards = [ Card(face_value, suit) for face_value in range(1, 14) for suit in (Clubs(), Hearts(), Spades(), Diamonds()) ]
        self.shuffle()

    def shuffle(self):
        for i in range(len(self.cards)):
            rand = floor((i + 1) * random())
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def deal_card(self):
        return self.cards.pop()

    def deal_hand(self, number):
        return [ self.deal_card() for _ in range(number) ]

    def size(self):
        return len(self.cards)


class Hand(object):

    def __init__(self, cards=list()):
        self.cards = cards

    def score(self):
        score = 0
        for card in self.cards:
            score += card.value()
        return score

    def add_card(self, card):
        self.cards.append(card)


class BlackJackCard(Card):

    def __init__(self, face_value, suit):
        super(BlackJackCard, self).__init__(face_value, suit)

    def value(self):
        if self.face_value <= 10:
            return self.face_value
        elif self.face_value > 10:
            return 10

    def min_value(self):
        return self.value()

    def max_value(self):
        if self.face_value == 1:
            return 11
        else:
            return self.value()


class BlackJackHand(Hand):

    def __init__(self, cards=list()):
        super(BlackJackHand, self).__init__(cards)
        
    def possible_scores(self):
        scores = [0]
        for card in self.cards:
            for i in range(len(scores)):
                scores[i] += card.value()
            if card.is_ace():
                new_scores = score.copy()
                for i in range(len(new_scores)):
                    new_scores[i] += card.max_value() - 1
                scores += new_scores
        return scores

    def score(self):
        max_under = 0
        min_over = 4 * (2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 3 * 10 + 11)
        for score in self.possible_scores():
            if score > 21 and score < min_over:
                min_over = score
            elif score > max_under:
                max_under = score
        if max_under != 0:
            return max_under
        else:
            return min_over

    def is_21(self):
        return self.score() == 21

    def busted(self):
        return self.score() > 21

    def is_black_jack(self):
        pass








