"""
Car Class to control each car instance. speed, appearance, etc.
Level obj instance will contain CarSpawnBase obj
"""
import game_settings as gs


class Car:
    def __init__(self, speed=gs.CAR_SPEED_MIN, color=gs.get_random_car_color()
                 , direction=gs.get_random_car_direction()):
        self.speed = speed
        self.color = color
        self.direction = direction

    def move(self):
        pass

