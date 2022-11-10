"""
Player Class to control all player inputs and behaviours
"""
import game_settings as gs


class Player():
    def __init__(self, speed=gs.CAR_SPEED_MIN, color=gs.get_random_car_color()
                 , direction=gs.get_random_car_direction()):
        self.speed = speed
        self.color = color
        self.direction = direction

    def move(self):
        pass
