"""
Any move in Concan is associated to one Player.  Every move must start with the
player picking up a card.  Once picked up, a player can optionally add cards
from their hand to the board.  A player can also rearrange cards on the board.
To finish their turn, the player must place a card in the discard pile.
"""

from game.gameplay.board import Board

class Move(object):
    def __init__(self, player):
        self.player = player

    def __init__(self, player, cardPickedUp, cardDiscarded):
        self.player = player
        self.cardPickedUp = cardPickedUp
        self.cardDiscarded = cardDiscarded

    def __init__(self, player, cardPickedUp, cardDiscarded, cardsAddedToBoard, board):
        self.player = player
        self.cardPickedUp = cardPickedUp
        self.cardDiscarded = cardDiscarded
        self.cardsAddedToBoard = cardsAddedToBoard
        self.board = board

    def setPlayer(self, player):
        self.player = player

    def getPlayer(self):
        return self.player

    def setCardPickedUp(self, cardPickedUp):
        self.cardPickedUp = cardPickedUp

    def getCardPickedUp(self):
        return self.cardPickedUp

    def setCardDiscarded(self, cardDiscarded):
        self.cardDiscarded = cardDiscarded

    def getCardDiscarded(self):
        return self.cardDiscarded

    def setCardsAddedToBoard(self, cardsAddedToBoard):
        self.cardsAddedToBoard = setCardsAddedToBoard

    def getCardsAddedToBoard(self):
        return self.getCardsAddedToBoard

    def setBoard(self, board):
        self.board = board

    def getBoard(self):
        return self.board
