"""
Any move in Concan is associated to one Player.  Every move must start with the
player picking up a card.  Once picked up, a player can optionally add cards
from their hand to the board.  To finish their turn, the player must place
a card in the discard pile.
"""

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
