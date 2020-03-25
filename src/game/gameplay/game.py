"""
The game itself.  Each game has N number of players.  The game goes until
one player reaches the maxScore, at which point the player with the lowest score
wins.
"""

class Game(object):
    def __init__(self, name, maxScore):
        self.name = name
        self.maxScore = maxScore
        self.players = []

    
