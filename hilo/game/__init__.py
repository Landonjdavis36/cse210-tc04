"""
The game package contains the classes for playing Hilo.
"""
import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        print ("{} of {}".format(self.value, self.suit))

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for value in ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]:
                self.cards.append(Card(suit, value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for n in range(len(self.cards)-1,0,-1):
            r = random.randint(0, n)
            self.cards[n], self.cards[r] = self.cards[r], self.cards[n]

    def drawCard(self):
        return self.cards.pop()

class Person(object):
    def __init__(self):
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def show(self):
        for card in self.hand:
            card.show()

class NextCard(object):
    def __init__(self):
        self.nextcard = []

    def draw(self, deck):
        self.nextcard.append(deck.drawCard())
        return self

    def show(self):
        for card1 in self.nextcard:
            card1.show()
