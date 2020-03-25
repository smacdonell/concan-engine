import json
from copy import copy

from game.cards.suit import Suit
from game.cards.card_name import *
from game.cards.card import *
from game.cards.deck import Deck
from game.util.image_getter import ImageFilenameGetter
from game.cards.deck_color import DeckColor
from game.gameplay.set import Set
from game.util.card_utils import CardUtils
from game.util.move_validator import MoveValidator

def main():
    deck = Deck(2, { }, True)
    wild = WildCard(WildCardName.JOKER)
    wild.setStandardCardNameOverride(StandardCardName.JACK)
    wild.setSuitOverride(Suit.HEARTS)

    set = Set([StandardCard(StandardCardName.SIX, Suit.SPADES),
    StandardCard(StandardCardName.FOUR, Suit.SPADES),
    StandardCard(StandardCardName.FIVE, Suit.SPADES),
    StandardCard(StandardCardName.THREE, Suit.SPADES),
    StandardCard(StandardCardName.TWO, Suit.SPADES),
    StandardCard(StandardCardName.SEVEN, Suit.SPADES),
    StandardCard(StandardCardName.ACE, Suit.SPADES),
    StandardCard(StandardCardName.EIGHT, Suit.SPADES),
    StandardCard(StandardCardName.QUEEN, Suit.SPADES),
    StandardCard(StandardCardName.KING, Suit.SPADES),
    wild,
    StandardCard(StandardCardName.TEN, Suit.SPADES),
    StandardCard(StandardCardName.NINE, Suit.SPADES)])

    print(MoveValidator.validateSet(set))

if __name__=='__main__':
    main()
