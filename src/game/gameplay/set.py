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

class Set(object):
    def __init__(self, cards):
        self.cards = cards
        self.__sortCards()

    def __sortCards(self):
        self.cards.sort(key=lambda x: (x.getStandardCardNameOverride().value if isinstance(x, WildCard) else x.getCardName().value,
        x.getSuitOverride().name if isinstance(x, WildCard) else x.getSuit()))

        # this attemps to figure out if the ace should be sorted as high or low
        sum = 0
        ace = None
        for card in self.cards:
            if (isinstance(card, StandardCard) and card.getCardName() != StandardCardName.ACE):
                sum += card.getCardName().value
            if ((isinstance(card, StandardCard) and card.getCardName() == StandardCardName.ACE)
            or (isinstance(card, WildCard) and card.getStandardCardNameOverride() == StandardCardName.ACE)):
                ace = card

        if ace is not None:
            if (len(self.cards) - 1 > 5 and sum < 30) or (len(self.cards) - 1 > 3 and sum < 20) or (sum < 15):
                self.cards.remove(ace)
                self.cards = [ace] + self.cards

    def setCardsInSet(self, cards):
        self.cards = cards
        self.__sortCards()

    def getCardsInSet(self):
        return self.cards
