import json
from copy import copy

from game.cards.suit import Suit
from game.cards.card_name import *
from game.cards.card import *
from game.cards.deck import Deck
from game.util.image_getter import ImageFilenameGetter
from game.cards.deck_color import DeckColor


def main():
    deck = Deck(2, { WildCardName.JOKER: 1 }, True)
    a = [1,2,3,4,5]

    a.sort(key=lambda x: x, reverse=not False)

    print(a)

if __name__=='__main__':
    main()
