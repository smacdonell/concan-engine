"""
A player in the game.  Each player has a hand and score.
"""
from game.gameplay.hand import Hand

import uuid

class Player(object):
    def __init__(self, name, turn):
        self.name = name
        self.id = uuid.uuid4()
        self.hand = Hand(True)
        self.score = 0
        self.turn = turn

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getId(self):
        return self.id

    def getHand(self):
        return self.hand

    def setHand(self, hand):
        self.hand = hand

    def addCardToHand(self, card):
        self.hand.addCardToHand(card)

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def addToScore(self, scoreToAdd):
        self.score += scoreToAdd
