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

from game.util.card_utils import CardUtils
from game.cards.card_name import StandardCardName

import copy

class MoveValidator(object):

    @classmethod
    def validateSet(clazz, set):
        if len(set.getCardsInSet()) < 3 or len(set.getCardsInSet()) > 13:
            return False

        #check for same name different suit
        if clazz.__checkForSameCardNameDifferentSuit(set):
            return True

        # check for cards of same suit in a row
        return clazz.__checkForStraight(set)

    @classmethod
    def __checkForSameCardNameDifferentSuit(clazz, set):
        set.sortCardsByCardName()
        cards = copy.deepcopy(set.getCardsInSet())
        if (not CardUtils.equalCardName(cards[0], cards[len(cards) - 1]) or
        len(cards) > 4):
            return False

        suitsFound = {}
        for card in cards:
            cardData = CardUtils.getCardNameAndSuit(card)
            suit = cardData['suit']
            if suit in suitsFound.keys():
                return False

            suitsFound[suit] = True
        return True

    @classmethod
    def __checkForStraight(clazz, set):
        valid = False

        set.sortCardsBySuit()
        cards = copy.deepcopy(set.getCardsInSet())
        if not CardUtils.equalSuit(cards[0], cards[len(cards) - 1]):
            return False

        if len(cards) < 13:
            ace = None
            two = None
            for card in cards:
                cardName = CardUtils.getCardName(card)
                if cardName == StandardCardName.ACE:
                    ace = card
                if cardName == StandardCardName.TWO:
                    two = card

            if ace is not None and two is not None:
                cards.remove(ace)

            valid = clazz.__validateStraight(cards)
        else:
            valid = clazz.__validateStraight(cards)

        return valid

    @classmethod
    def __validateStraight(clazz, cards):
        namesFound = {}
        for i in range(0, len(cards) - 1):
            thisCardValue = CardUtils.getCardName(cards[i])
            nextCardValue = CardUtils.getCardName(cards[i + 1])
            if (thisCardValue.value + 1) != nextCardValue.value:
                return False

        return True
