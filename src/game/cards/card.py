"""
Representation of a single playing card in a deck.  A StandardCard is made up of a
combination of a StandardCardName and Suit.
Ex: StandardCardName.ACE x Suit.SPADES

A WildCard only has a CardName:
Ex: WildCardName.JOKER

"""
from game.cards.card_name import CardName
from game.cards.suit import Suit

class Card(object):
    def __init__(self, cardName):
        self.cardName = cardName

    def getCardName(self):
        return self.cardName

    def __str__(self):
        return self.cardName.getPrettyName()

    def __eq__(self, obj):
        return self.cardName == obj.cardName

class WildCard(Card):
    def __init__(self, wildCardName):
        super().__init__(wildCardName)

class StandardCard(Card):
    def __init__(self, standardCardName, suit):
        super().__init__(standardCardName)
        self.suit = suit

    def getSuit(self):
        return self.suit

    def __str__(self):
        return self.cardName.getPrettyName() + ' of ' + self.suit.getPrettyName()

    def __eq__(self, obj):
        return self.cardName == obj.cardName and self.suit == obj.suit
