"""
The game itself.  Each game has N number of players.  The game goes until
one player reaches the maxScore, at which point the player with the lowest score
wins.
"""

from game.gameplay.board import Board
from game.gameplay.player import Player
from game.gameplay.round import Round
from game.cards.deck import Deck
from game.cards.card_name import WildCardName

import uuid
import math

class Game(object):
    def __init__(self, name, maxScore):
        self.gameId = uuid.uuid4()
        self.name = name
        self.maxScore = maxScore
        self.deck = None
        self.players = []
        self.roundHistory = []
        self.currentRound = None

    def getGameId(self):
        return setlf.gameId

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getMaxScore(self):
        return self.maxScore

    def getDeck(self):
        return self.deck

    def setDeck(self, deck):
        self.deck = deck

    def getPlayers(self):
        return self.players

    def setPlayers(self, players):
        self.players = players

    def addPlayer(self, player):
        self.players.append(player)

    def getRoundHistory(self):
        return self.roundHistory

    def getCurrentRound(self):
        return self.currentRound

    def startNewGame(self):
        numDecks = math.ceil((14 * len(self.players) + 30) / 52)

        self.deck = Deck(numDecks, { WildCardName.JOKER: 2 }, True)

        self.startNewRound()

    def startNewRound(self):
        lastDealer = None
        if self.currentRound is not None:
            self.roundHistory.append(self.currentRound)
            lastDealer = self.currentRound.getDealer()

        if lastDealer is None:
            currentDealer = self.players[0]
        else:
            lastDealerIndex = self.players.index(lastDealer)
            if lastDealerIndex == len(self.players) - 1:
                currentDealer = self.players[0]
            else:
                currentDealer = self.players[lastDealerIndex + 1]

        self.currentRound = Round(self.players, len(self.roundHistory), currentDealer)
        self.deck.shuffleCardDeck()

    def getPlayersByRoundTurnOrder(self):
        return self.currentRound.getPlayersInOrder()
