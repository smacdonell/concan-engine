"""
Name of a playing card.  There are 14 different playing card names in any deck.
"""

from enum import Enum, auto

class CardName(Enum):
    def getPrettyName(self):
        return self.name.capitalize()

class StandardCardName(CardName):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class WildCardName(CardName):
    JOKER = auto()
