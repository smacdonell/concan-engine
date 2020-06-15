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
from game.request.move_request import MoveRequest
from game.util.score_calculator import ScoreCalculator
from game.gameplay.player import Player
from game.gameplay.game_manager import GameManager
from game.gameplay.game import Game
from game.util.request_validator import RequestValidator
from collections import Counter

import json


def main():
    manager = GameManager()

    p1 = Player('Scott', 0)
    p2 = Player('Cathay', 1)
    p3 = Player('Raha', 2)

    g = Game('The Best Game', 300)

    manager.setGame(g)
    manager.addPlayerToGame(p1)
    manager.addPlayerToGame(p2)
    manager.addPlayerToGame(p3)
    manager.startNewGame()

    j = '''{"playerId":"12345","discardedCard":{"cardName":"ACE","suit":"SPADES"},"newSets":[[{"cardName":"ACE","suit":"SPADES","wild":"JOKER"}
    ,{"cardName":"ACE","suit":"DIAMONDS"},{"cardName":"ACE","suit":"HEARTS"}]],"board":[[{"cardName":"KING","suit":"SPADES"},
    {"cardName":"KING","suit":"DIAMONDS"},{"cardName":"KING","suit":"HEARTS"}],[{"cardName":"TWO","suit":"DIAMONDS"},
    {"cardName":"THREE","suit":"DIAMONDS"},{"cardName":"FOUR","suit":"DIAMONDS"}],[{"cardName":"NINE","suit":"CLUBS"},
    {"cardName":"NINE","suit":"DIAMONDS"},{"cardName":"NINE","suit":"HEARTS"}]]}'''

    #RequestValidator.validateMoveRequest(j)

    js = {
      "playerId": "12345",
      "discardedCard": {
        "cardName": "ACE",
        "suit": "SPADES"
      },
      "newSets": [
        [
          {
            "cardName": "ACE",
            "suit": "SPADES",
            "wild": "JOKER"
          },
          {
            "cardName": "ACE",
            "suit": "DIAMONDS"
          },
          {
            "cardName": "ACE",
            "suit": "HEARTS"
          }
        ]
      ],
      "board": [
        [
          {
            "cardName": "KING",
            "suit": "SPADES"
          },
          {
            "cardName": "KING",
            "suit": "DIAMONDS"
          },
          {
            "cardName": "KING",
            "suit": "HEARTS"
          }
        ],
        [
          {
            "cardName": "TWO",
            "suit": "DIAMONDS"
          },
          {
            "cardName": "THREE",
            "suit": "DIAMONDS"
          },
          {
            "cardName": "FOUR",
            "suit": "DIAMONDS"
          }
        ],
        [
          {
            "cardName": "NINE",
            "suit": "CLUBS"
          },
          {
            "cardName": "NINE",
            "suit": "DIAMONDS"
          },
          {
            "cardName": "NINE",
            "suit": "HEARTS",
          }
        ]
      ]
    }

    a = [
        StandardCard(StandardCardName.KING, Suit.SPADES), StandardCard(StandardCardName.KING, Suit.SPADES), StandardCard(StandardCardName.KING, Suit.DIAMONDS),
        StandardCard(StandardCardName.KING, Suit.DIAMONDS), StandardCard(StandardCardName.KING, Suit.HEARTS), StandardCard(StandardCardName.KING, Suit.CLUBS)
    ]
    b = [
        StandardCard(StandardCardName.KING, Suit.SPADES), StandardCard(StandardCardName.KING, Suit.SPADES),
        StandardCard(StandardCardName.KING, Suit.DIAMONDS), StandardCard(StandardCardName.KING, Suit.HEARTS), StandardCard(StandardCardName.KING, Suit.CLUBS)
    ]

    res = list((Counter(a) & Counter(b)).elements())
    for c in res:
        print(c)


if __name__=='__main__':
    main()
