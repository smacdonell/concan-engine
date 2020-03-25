import json
from copy import copy

from game.cards.suit import Suit
from game.cards.card_name import *
from game.cards.card import *
from game.cards.deck import Deck
from game.util.image_getter import ImageFilenameGetter
from game.cards.deck_color import DeckColor
from game.gameplay.set import Set

def main():
    deck = Deck(2, { WildCardName.JOKER: 1 }, True)
    wild = WildCard(WildCardName.JOKER)
    wild.setStandardCardNameOverride(StandardCardName.ACE)
    wild.setSuitOverride(Suit.SPADES)
    set = Set([StandardCard(StandardCardName.QUEEN, Suit.SPADES), wild,
    StandardCard(StandardCardName.TWO, Suit.SPADES)])

    for c in set.getCardsInSet():
        print(c)

    a = [StandardCard(StandardCardName.TWO, Suit.SPADES), StandardCard(StandardCardName.ACE, Suit.SPADES),
    StandardCard(StandardCardName.THREE, Suit.SPADES)]
    b = [StandardCard(StandardCardName.KING, Suit.DIAMONDS)] + a



if __name__=='__main__':
    main()
