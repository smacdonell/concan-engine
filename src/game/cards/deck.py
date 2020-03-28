"""
Card deck and appropriate methods.  The decks of cards represented here are
stack-like.  The 'top' of the deck is the last index, and the 'bottom' is
the first index.
"""

from game.cards.card_name import StandardCardName
from game.cards.card_name import WildCardName
from game.cards.suit import Suit
from game.cards.card import StandardCard
from game.cards.card import WildCard

import random
import copy

class Deck(object):
    def __init__(self, numDecks, numWildMap, shuffleOnInit):
        self.numDecks = numDecks
        self.numWildMap = numWildMap

        self.__initDeck(shuffleOnInit)

    def __initDeck(self, shuffleOnInit):
        self.cardDeck = []
        self.discardDeck = []

        for i in range(0, self.numDecks):
            self.__populateStandardDeck()

        self.__populateWildDeck()

        if shuffleOnInit:
            self.shuffleCardDeck()

    def __populateStandardDeck(self):
        for cardName in StandardCardName:
            for suit in Suit:
                card = StandardCard(cardName, suit)
                self.cardDeck.append(card)

    def __populateWildDeck(self):
        for wildType in self.numWildMap:
            for i in range(0, self.numWildMap[wildType]):
                wildCard = WildCard(wildType)
                self.cardDeck.append(wildCard)

    def shuffleCardDeck(self):
        for i in range(0, len(self.cardDeck)):
            rand = random.randrange(0, len(self.cardDeck))
            temp = self.cardDeck[i]
            self.cardDeck[i] = self.cardDeck[rand]
            self.cardDeck[rand] = temp

    def getCardDeck(self):
        return self.cardDeck

    def setCardDeck(self, cardDeck):
        self.cardDeck = cardDeck

    def addCardToDeck(self, card):
        count = {}
        for card in self.cardDeck:
            count[card] = count.get(card, 0) + 1

        if count[card] < self.numDecks:
            self.cardDeck.append(card);

    def removeCardFromDeck(self, card):
        if card in self.cardDeck:
            self.cardDeck.remove(card)

    def getNextCardFromDeck(self):
        nextCard = self.cardDeck.pop()

        if len(self.cardDeck) <= 0:
            self.cardDeck = copy.deepcopy(self.discardDeck)
            self.discardDeck = []
            self.shuffleCardDeck()

        return nextCard

    def resetDeck(self):
        self.__initDeck(False)

    def printDeck(self):
        for card in self.cardDeck:
            print(card)

    def getDiscardDeck(self):
        return self.discardDeck

    def addCardToDiscardDeck(self, card):
        self.discardDeck.append(card)

    def removeTopCardFromDiscardDeck(self):
        return self.discardDeck.pop()

    def printDiscardDeck(self):
        for card in self.discardDeck:
            print(card)
