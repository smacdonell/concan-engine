from enum import Enum, auto

class DeckColor(Enum):
    BLUE = auto()
    GREY = auto()
    GREEN = auto()
    PURPLE = auto()
    RED = auto()
    YELLOW = auto()

    def getPrettyName(self):
        return self.name.capitalize()
