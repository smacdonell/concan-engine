"""
TODO:
This should take in certain objects like card, hand, player, etc, and then
calculate the score of a card, hand, player, etc.

When calculating set scores, it is assumed that sets have already been
validated by the MoveValidator.

Aces are the only card that can have a different score depending on the set
context.  Since we know sets should be validated before being scored, and that
all Aces have a value of 10 except when they are the first card in a small
straight (Ace, Two, Three, Etc), then we can safely assume every Ace has a
value of 10, unless we also find a Two in the set, in which case it has a
value of 1.
"""

from game.gameplay.set import Set
from game.gameplay.player import Player
from game.gameplay.hand import Hand
from game.util.card_utils import CardUtils
from game.cards.card_name import StandardCardName
from game.cards.card import WildCard

class ScoreCalculator(object):
    scoreMap = {
        StandardCardName.JACK: 10,
        StandardCardName.QUEEN: 10,
        StandardCardName.KING: 10,
        StandardCardName.ACE: 10
    }

    @classmethod
    def calculateSetScore(clazz, set):
        totalScore = 0
        foundAce = False
        foundTwo = False
        for card in set.getCardsInSet():
            cardName = CardUtils.getCardName(card)
            if cardName == StandardCardName.ACE:
                foundAce = True
            elif cardName in clazz.scoreMap.keys():
                totalScore += clazz.scoreMap[cardName]
            else:
                if cardName == StandardCardName.TWO:
                    foundTwo = True
                totalScore += cardName.value

        if foundAce:
            if foundTwo:
                totalScore += 1
            else:
                totalScore += 10

        return totalScore

    @classmethod
    def calculateLoserScore(clazz, player, round):
        # eventually use round to see if player opened
        opened = False

        totalScore = 0
        jokerScore = 0
        cardsInHand = player.getHand().getCardsInHand()
        for card in cardsInHand:
            if isinstance(card, WildCard):
                jokerScore += 50
            elif opened:
                cardName = CardUtils.getCardName(card)
                if cardName in clazz.scoreMap.keys():
                    totalScore += clazz.scoreMap[cardName]
                else:
                    totalScore += cardName.value

        if not opened or totalScore > 100:
            totalScore = 100

        totalScore += jokerScore

        return totalScore
