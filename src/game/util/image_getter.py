"""
Utility class to get image filenames for different objects.
"""

from game.cards.card_name import StandardCardName
from game.cards.card_name import WildCardName
from game.cards.card import StandardCard
from game.cards.card import WildCard
from game.cards.deck_color import DeckColor

class ImageFilenameGetter(object):
    imageExtension = '.png'
    deckEnd = "_deck"
    backEnd = "_back"

    @classmethod
    def getCardImageFilename(clazz, card):
        if isinstance(card, WildCard):
            return card.getCardName().name + clazz.imageExtension
        else:
            return card.getCardName().name[0] + clazz.imageExtension

    @classmethod
    def getCardBackImageFilename(clazz, color):
        return color.name.lower() + clazz.backEnd + clazz.imageExtension

    @classmethod
    def getCardDeckImageFilename(clazz, color):
        return color.name.lower() + clazz.deckEnd + clazz.imageExtension
