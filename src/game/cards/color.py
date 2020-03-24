"""
Two colors in a deck, RED or BLACK
"""

from enum import Enum, auto

class Color(Enum):
    RED = auto()
    BLACK = auto()

    def getPrettyName(self):
        return self.name.capitalize()
