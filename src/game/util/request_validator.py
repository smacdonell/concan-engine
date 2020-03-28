"""
Validates requests from the front end of the app.
"""

from game.util.move_validator import MoveValidator

class requestValidator(class):

    """
    A valid move must:
    -Discard a card
    -Optionally play new sets
    -Optionally rearrange existing sets on board

    The board at the end of a move must contain all valid sets
    """
    @classmethod
    def validateMoveRequest(clazz, moveRequest):
        print('TODO - validateMoveRequest')
        # for set in sets on board of move
        # iterate through each set and call MoveValidator.validateSet(set)
        # on each set
