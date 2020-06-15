"""
Validates requests from the front end of the app.
"""

from game.util.card_utils import CardUtils
from game.util.move_validator import MoveValidator
from game.request.move_request import MoveRequest

import jsonschema
import json
import os
import collections

class RequestValidator(object):

    """
    A valid move must:
    -Discard a card
    -Optionally play new sets
    -Optionally rearrange existing sets on board

    The board at the end of a move must contain all valid sets
    """
    @classmethod
    def validateMoveRequest(clazz, moveRequestJson):
        dirname = os.path.dirname(__file__)
        with open(os.path.join(dirname, '../schema/move_request_schema.json')) as schemaFile:
            schema = json.load(schemaFile)

        try:
            jsonschema.validate(instance=moveRequestJson, schema=schema)
        except Exception as e:
            print(e)
            return False


    @classmethod
    def validateMoveStructure(clazz, player, board, moveRequest):
        #moveRequest = MoveRequest(moveRequestJson)

        discardedCard = CardUtils.getCardFromJson(moveRequest.getDiscardedCard())
        newSets = CardUtils.getSetsFromJson(moveRequest.getNewSets())
        setsOnBoard = CardUtils.getSetsFromJson(moveRequest.getBoard())

        oldBoardState = []
        newBoardState = []

        for set in newSets:
            newBoardState += set.getCardsInSet()

        for set in setsOnBoard:
            newBoardState += set.getCardsInSet()

        for set in board.getSetsOnBoard():
            oldBoardState += set.getCardsInSet()

        boardDiff = list((collections.Counter(newBoardState) - collections.Counter(oldBoardState)).elements())
