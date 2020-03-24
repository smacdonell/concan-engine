"""
Utility class to get image filenames for different objects.
"""

from game.cards.card import Card
from game.cards.card_name import CardName
from game.cards.deck_color import DeckColor

class ImageFilenameGetter(object):
    imageExtension = '.png'
    deckEnd = "_deck"
    backEnd = "_back"

    @classmethod
    def getCardImageFilename(clazz, card):
        if card.getCardName() == CardName.JOKER:
            return card.getCardName() + clazz.imageExtension
        else:
            return card.getCardName().name[0] + clazz.imageExtension

    @classmethod
    def getCardBackImageFilename(clazz, color):
        return color.name.lower() + clazz.backEnd + clazz.imageExtension

    @classmethod
    def getCardDeckImageFilename(clazz, color):
        return color.name.lower() + clazz.deckEnd + clazz.imageExtension
