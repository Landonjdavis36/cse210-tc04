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






deck = Deck()
deck.shuffle()

human = Person()
playerHand = human.draw(deck)

newcard = NextCard()
nextCard = newcard.draw(deck)





play = input("Do you want to play High/Low? Y or N? ")
while play.lower()== "y":
    card = playerHand
    print("The current card is: ", str(card.show()))
    guess = input("Guess H for high or L for low." )
    if guess.lower()=="h":
        if card > nextCard:
            print("Congratulations! You guessed correctly! The next card was ", card)
            play = input("Play again? Y or N? ")

        if card < nextCard:
            print("You lost! The next card was ", nextCard)
            play = input("Play again? Y or N? ")

    if guess.lower()=="l":
        if card > nextCard:
            print("You lost! The next card was ", nextCard)
            play = input("Play again? Y or N? ")

        if card < nextCard:
            print("Congratulations! You guessed correctly! The next card was ", nextCard)
else:
    print("The game is over.")
    
