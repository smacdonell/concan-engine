"""
Representation of a Player's hand.
"""

class Hand(object):
    def __init__(self, leftToRightSort):
        self.cardsInHand = []
        self.leftToRightSort = leftToRightSort

    def getLeftToRightSort(self):
        return self.leftToRightSort

    def setLeftToRightSort(self, leftToRightSort):
        self.leftToRightSort = leftToRightSort

    def getCardsInHand(self):
        return self.cardsInHand

    def setCardsInHand(self, cardsInHand):
        self.cardsInHand = cardsInHand

    def addCardToHand(self, card):
        self.cardsInHand.append(card)

    def removeCardFromHand(self, card):
        if card in self.cardsInHand:
            self.cardsInHand.remove(card)

    def sortHand(self):
        self.cardDeck.sort(key=lambda x: (x.getCardName().value, x.getSuit().name if x.getSuit() else 0), reverse=not self.leftToRightSort)

    def getNumCardsInHand(self):
        return len(self.cardsInHand)
