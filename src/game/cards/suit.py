"""
Standard suit representation for a deck of cards.  One deck has a full run of
cards (minus jokers) in each Suit.
SPADES, DIAMONDS, HEARTS, CLUBS
"""
from enum import Enum
from game.cards.color import Color

class Suit(Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    SPADES = "S"
    CLUBS = "C"

    def getPrettyName(self):
        return self.name.capitalize()

    def getColor(self):
        if self in [Suit.HEARTS, Suit.DIAMONDS]:
            return Color.RED
        else:
            return Color.BLACK
