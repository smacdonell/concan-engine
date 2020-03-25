from game.cards.card_name import *
from game.cards.card import *

class CardUtils(object):
    __lowCards = [StandardCardName.TWO, StandardCardName.THREE,
    StandardCardName.FOUR, StandardCardName.FIVE, StandardCardName.SIX]

    __highCards = [StandardCardName.ACE, StandardCardName.KING,
    StandardCardName.QUEEN, StandardCardName.JACK, StandardCardName.TEN]

    __highCardsExcludingAce = [StandardCardName.KING, StandardCardName.QUEEN,
    StandardCardName.JACK, StandardCardName.TEN]

    @classmethod
    def getStandardCardName(clazz, card):
        if isinstance(card, StandardCard):
            return card.getCardName()
        else:
            return card.getStandardCardNameOverride()

    @classmethod
    def isLowCard(clazz, card):
        return clazz.getStandardCardName(card) in clazz.__lowCards

    @classmethod
    def isHighCard(clazz, card):
        return clazz.getStandardCardName(card) in clazz.__highCards

    @classmethod
    def isHighCardExcludingAce(clazz, card):
        return clazz.getStandardCardName(card) in clazz.__highCardsExcludingAce

    @classmethod
    def getCardName(clazz, card):
        if isinstance(card, WildCard):
            return card.getStandardCardNameOverride()
        else:
            return card.getCardName()

    @classmethod
    def getCardSuit(clazz, card):
        if isinstance(card, WildCard):
            return card.getSuitOverride()
        else:
            return card.getSuit()

    @classmethod
    def getCardNameAndSuit(clazz, card):
        dict = {}
        if isinstance(card, WildCard):
            dict['cardName'] = card.getStandardCardNameOverride()
            dict['suit'] = card.getSuitOverride()
        else:
            dict['cardName'] = card.getCardName()
            dict['suit'] = card.getSuit()

        return dict

    @classmethod
    def equalIgnoreCardType(clazz, x, y):
        xData = clazz.getCardNameAndSuit(x)
        yData = clazz.getCardNameAndSuit(y)

        if (xData['cardName'] == yData['cardName']
            and xData['suit'] == yData['suit']):
            return True

        return False

    @classmethod
    def equalCardNameDifferentSuit(clazz, x, y):
        xData = clazz.getCardNameAndSuit(x)
        yData = clazz.getCardNameAndSuit(y)

        if (xData['cardName'] == yData['cardName']
            and xData['suit'] != yData['suit']):
            return True

        return False

    @classmethod
    def equalSuitDifferentCardName(clazz, x, y):
        xData = clazz.getCardNameAndSuit(x)
        yData = clazz.getCardNameAndSuit(y)

        if (xData['cardName'] != yData['cardName']
            and xData['suit'] == yData['suit']):
            return True

        return False

    @classmethod
    def equalCardName(clazz, x, y):
        xData = clazz.getCardNameAndSuit(x)
        yData = clazz.getCardNameAndSuit(y)

        if xData['cardName'] == yData['cardName']:
            return True

        return False

    @classmethod
    def equalSuit(clazz, x, y):
        xData = clazz.getCardNameAndSuit(x)
        yData = clazz.getCardNameAndSuit(y)

        if xData['suit'] == yData['suit']:
            return True

        return False
