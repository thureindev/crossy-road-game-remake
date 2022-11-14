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
        a_base = CarSpawnBase(pos_x=0, pos_y=50, direction='right')
        self.spawn_bases.append(a_base)
        a_base.start_produce_random_car()

    def visual_update(self):
        self.canvas.delete("all")

        for base in self.spawn_bases:
            for car in base.cars:
                car.move()
                self.canvas.create_rectangle(car.draw_x0, car.draw_y0, car.draw_x1, car.draw_y1, fill=car.color)

                # self.canvas.create_rectangle(50, 50, 50 + 50, 50 + 20, fill='blue')
        self.canvas.create_rectangle(self.player.draw_x0, self.player.draw_y0, self.player.draw_x1,
                                     self.player.draw_y1, fill=car.color)

        self.after(ms=gs.CLOCK_TICK, func=self.visual_update)
