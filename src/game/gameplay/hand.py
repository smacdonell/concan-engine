"""
Representation of a Player's hand.
"""

class Hand(object):
    def __init__(self, leftToRightSort):
        self.hand = []
        self.leftToRightSort = leftToRightSort

    def getLeftToRightSort(self):
        return self.leftToRightSort

    def setLeftToRightSort(self, leftToRightSort):
        self.leftToRightSort = leftToRightSort

    def addCardToHand(self, card):
        self.hand.append(card)

    def removeCardFromHand(self, card):
        if card in self.hand:
            self.hand.remove(card)

    def sortHand(self):
        self.cardDeck.sort(key=lambda x: (x.getCardName().value, x.getSuit().name if x.getSuit() else 0), reverse=not self.leftToRightSort)
