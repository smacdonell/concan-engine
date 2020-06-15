"""
A model of the data in a request for a move from a player.
"""
import json

class MoveRequest(object):
    def __init__(self, jsonData):
        self.__dict__ = json.loads(jsonData)

    def getPlayerId(self):
        return self.playerId

    def getDiscardedCard(self):
        return self.discardedCard

    def getNewSets(self):
        return self.newSets

    def getBoard(self):
        return self.board
