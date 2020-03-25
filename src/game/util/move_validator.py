"""
This is responsible for validating any move that a player attempts to make.
Possible move types:
-Open (first time added to board, must have 51 points)
-Put down new set
-Add to existing set
-Rearrange existing sets

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

The catch here is that WildCardName.JOKER cards are wild, and can be any card.
A player must assign the card a StandardCardName and Suit before it can be played.
"""

class MoveValidator(object):

    @classmethod
    def validateSet(clazz, set):
        cards = set.getCardsInSet()
        if len(cards) < 3:
            return False

        return True
