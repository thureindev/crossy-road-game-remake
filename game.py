"""
Game Class to control the entire game-play
"""
import tkinter as tk
import time
import game_settings as gs

import random
from level import Level
from carspawnbase import CarSpawnBase
from player import Player


class Game(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{gs.SCREEN_WIDTH}x{gs.SCREEN_HEIGHT}")

        # canvas can be game visual controller obj
        self.canvas = tk.Canvas(self, width=gs.SCREEN_WIDTH, height=gs.SCREEN_HEIGHT)
        self.canvas.pack()

        self.canvas.create_rectangle(0, 0, 50, 20, fill='red')
        self.canvas.create_rectangle(100, 100, 100 + 50, 100 + 20, fill='blue')

        self.levels = []
        a_level = Level()
        self.levels.append(a_level)

        self.player = Player()
        self.is_gameover = False

        self.spawn_bases = []
        a_base = CarSpawnBase(direction='right')
        self.spawn_bases.append(a_base)
        a_base.produce_random_car()

    def visual_update(self):
        print("I'm visual update")
        for base in self.spawn_bases:
            print(base)
            for car in base.cars:
                print(car)
                car.move()
                print(car.color)
                self.canvas.create_rectangle(car.pos_x, car.pos_y, car.width, car.height, fill=car.color)

                self.canvas.create_rectangle(50, 50, 50 + 50, 50 + 20, fill='blue')

        self.after(ms=gs.CLOCK_TICK, func=self.visual_update)
