"""
Represents a round of the game.  Events in a round happen in this order:
-The deck is shuffled
-The player to the left of the dealer cuts the deck, if the bottom card is a
Joker, they get to keep the Joker
-14 cards are dealt to each player except the dealer, who is dealt 15
-Dealer starts the round by discarding a card into the discard pile
-Players always start their turn by picking up a card.  If the player picks
up a card from the discard pile, they must use it in their turn
-If the player has not yet opened, they can open by playing a set or sets with
a total score >= 51
-If the player has not yet opened and cannot open, their turn is over and they
must discard a card
-If a player has opened, they can rearrange any cards on the board, and play
any cards from their hand, as long as when they finish their turn, every
set on the board is still a valid set
-If there is a Joker on the board, and a player has opened and has the card which
the Joker represents, they can swap their card for the Joker and keep the Joker
-The player's turn ends when they discard a card
The round ends when a player gets rid of all of their cards
"""

import uuid

from game.gameplay.board import Board
from game.gameplay.player import Player
from game.gameplay.move import Move

class Round(object):
    def __init__(self, players, roundIndex, dealer):
        self.roundId = uuid.uuid4()
        self.roundIndex = roundIndex
        self.board = Board()
        self.dealer = dealer
        self.currentPlayer = dealer

        self.moves = []

        dealerIndex = players.index(dealer)
        self.playersInOrder = players[dealerIndex:] + players[0:dealerIndex]

        self.playerState = {}
        for player in players:
            self.playerState[player.getId()] = { 'opened': False }

    def getRoundId(self):
        return self.roundId

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def getPlayerState(self, player):
        return self.playerState[player.getId()]

    def getDealer(self):
        return self.dealer

    def setDealer(self, player):
        self.dealer = player

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getMoves(self):
        return self.moves

    def setMoves(self, moves):
        self.moves = moves

    def addMove(self, move):
        self.moves.append(move)

    def getPlayersInOrder(self):
        return self.playersInOrder

    def getNextPlayerInTurnOrder(self):
        currentPlayerIndex = self.playersInOrder.index(self.currentPlayer)
        if currentPlayerIndex == len(self.playersInOrder) - 1:
            return self.playersInOrder[0]
        else:
            return self.playersInOrder[currentPlayerIndex + 1]

    def endCurrentPlayersTurn(self):
        currentPlayer = getNextPlayerInTurnOrder()
