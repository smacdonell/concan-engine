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
from game.util.score_calculator import ScoreCalculator
from game.gameplay.player import Player
from game.gameplay.game_manager import GameManager
from game.gameplay.game import Game

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

    for player in manager.getGame().getPlayers():
        print(player.getName())
        print('   ---   ')
        for card in player.getHand().getCardsInHand():
            print(card)

        print('-----')
        print('-----')


if __name__=='__main__':
    main()
