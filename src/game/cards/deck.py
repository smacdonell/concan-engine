from game.cards.card_name import StandardCardName
from game.cards.card_name import WildCardName
from game.cards.suit import Suit
from game.cards.card import StandardCard
from game.cards.card import WildCard

import random

class Deck(object):
    def __init__(self, numDecks, numWildMap, shuffleOnInit):
        self.numDecks = numDecks
        self.numWildMap = numWildMap

        self.__initDeck(shuffleOnInit)

    def __initDeck(self, shuffleOnInit):
        self.cardDeck = []

        for i in range(0, self.numDecks):
            self.__populateStandardDeck()
            self.__populateWildDeck()

        if shuffleOnInit:
            self.shuffleDeck()

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

    def shuffleDeck(self):
        for i in range(0, len(self.cardDeck)):
            rand = random.randrange(0, len(self.cardDeck))
            temp = self.cardDeck[i]
            self.cardDeck[i] = self.cardDeck[rand]
            self.cardDeck[rand] = temp

    def resetDeck(self):
        self.__initDeck(False)

    def printDeck(self):
        for card in self.cardDeck:
            print(card)
