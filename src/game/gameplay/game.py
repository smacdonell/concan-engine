"""
The game itself.  Each game has N number of players.  The game goes until
one player reaches the maxScore, at which point the player with the lowest score
wins.
"""

from game.gameplay.board import Board
from game.gameplay.player import Player

import uuid

class Game(object):
    def __init__(self, name, maxScore):
        self.gameId = uuid.uuid4()
        self.name = name
        self.maxScore = maxScore
        self.players = []
        self.board = Board()
        self.turn = turn
