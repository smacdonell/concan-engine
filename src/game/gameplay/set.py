"""
Cards must be arranged into a valid set before being placed on the board.
A set is valid if:
-It has a minimum of 3 cards
AND
-The cards are all the same StandardCardName but all have a different Suit.
Ex: StandardCardName.ACE (Suit.SPADES, Suit.HEARTS, Suit.DIAMONDS, Suit.CLUBS)
-If the cards all have a different StandardCardName, but same Suit, and are in
consecutive order.  An ACE can be high or low, but not both.
Ex Valid:
Suit.SPADES (StandardCardName.ACE, StandardCardName.TWO, StandardCardName.THREE)
Suit.DIAMONDS (StandardCardName.QUEEN, StandardCardName.KING, StandardCardName.ACE)
Ex Not Valid:
Suit.SPADES (StandardCardName.KING, StandardCardName.ACE, StandardCardName.TWO)
Suit.CLUBS (StandardCardName.FIVE, StandardCardName.SIX, StandardCardName.EIGHT)
"""

from game.cards.card import *
from game.cards.card_name import *
from game.util.card_utils import CardUtils

class Set(object):
    def __init__(self, cards):
        self.cards = cards
        self.sortCardsByCardName()

    def sortCardsByCardName(self):
        self.cards.sort(key=lambda x: (x.getStandardCardNameOverride().value if isinstance(x, WildCard) and x.getStandardCardNameOverride() else x.getCardName().value,
        x.getSuitOverride().name if isinstance(x, WildCard) else x.getSuit().value))

        lowCardsFound = 0
        highCardsFound = 0
        ace = None
        for card in self.cards:
            if CardUtils.isLowCard(card):
                lowCardsFound += 1
            if CardUtils.isHighCardExcludingAce(card):
                highCardsFound += 1
            if (CardUtils.getStandardCardName(card) == StandardCardName.ACE):
                ace = card

        if ace is not None:
            if lowCardsFound > highCardsFound:
                self.cards.remove(ace)
                self.cards = [ace] + self.cards

    def sortCardsBySuit(self):
        self.cards.sort(key=lambda x: (x.getSuitOverride().value if isinstance(x, WildCard) and x.getSuitOverride() else x.getSuit().value,
        x.getStandardCardNameOverride().value if isinstance(x, WildCard) and x.getStandardCardNameOverride() else x.getCardName().value))

    def setCardsInSet(self, cards):
        self.cards = cards
        self.sortCardsByCardName()

    def getCardsInSet(self):
        return self.cards

    def printSet(self):
        for c in self.cards:
            print(c)
