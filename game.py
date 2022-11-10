"""
Game Class to control the entire game-play
"""
import random
from level import Level
from player import Player


class Game:
    def __init__(self):
        self.levels = []
        a_level = Level()
        self.levels.append(a_level)
        self.player = Player()
        self.is_gameover = False

    def start_game(self):
        pass
