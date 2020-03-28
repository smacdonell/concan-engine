"""
Manages all game functions.
"""

from game.gameplay.game import Game
from game.cards.deck import Deck
from game.cards.card import WildCard
from game.request.move_request import MoveRequest

import random

class GameManager(object):
    def __init__(self):
        self.game = None

    def getGame(self):
        return self.game

    def setGame(self, game):
        self.game = game

    # create a new game
    def createNewGame(self, name, maxScore):
        self.game = Game(name, maxScore)

    def addPlayerToGame(self, player):
        self.game.addPlayer(player)

    # start a new game
    def startNewGame(self):
        self.game.startNewGame()
        jokerFoundOnCut = self.cutDeckAndCheckForJoker()
        self.dealCardsToPlayers(jokerFoundOnCut)

    # cut the deck and see if the bottom card is a Joker
    def cutDeckAndCheckForJoker(self):
        cardDeck = self.game.getDeck().getCardDeck()
        rand = random.randrange(0, len(cardDeck))
        card = cardDeck[rand]

        if isinstance(card, WildCard) and card.getCardName() == WildCardName.JOKER:
            # give the player to the left of the dealer the joker
            playerToLeftOfDealer = self.game.getRound().getPlayersInOrder()[1]
            playerToLeftOfDealer.addCardToHand(cardDeck[rand])
            self.game.getDeck().setCardDeck(cardDeck[rand + 1:] + cardDeck[0:rand])
            return True

        self.game.getDeck().setCardDeck(cardDeck[rand:] + cardDeck[0:rand])
        return False

    # deal cards to each player
    def dealCardsToPlayers(self, jokerFoundOnCut):
        for i in range(0, 14):
            for player in self.game.getPlayersByRoundTurnOrder():
                if player.getHand().getNumCardsInHand() < 14:
                    player.addCardToHand(self.game.getDeck().getNextCardFromDeck())

        self.game.getPlayersByRoundTurnOrder()[0].addCardToHand(self.game.getDeck().getNextCardFromDeck())


    # start a new round
    def startNewRound(self):
        self.game.startNewRound()

    def shuffleCards(self):
        self.game.getDeck().shuffleCardDeck()

    def getActiveTurnPlayer(self):
        return self.game.getCurrentRound().getCurrentPlayer()

    # process a move from the current player
    # assume that proper validation has happened on the moveRequest
    def processMove(self, player, moveRequest):
        print('TODO -- processMove()')
