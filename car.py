"""
Car Class to control each car instance. speed, appearance, etc.
Level obj instance will contain CarSpawnBase obj
"""
import game_settings as gs


class Car:
    def __init__(self, speed=gs.CAR_SPEED_MIN, color=gs.get_random_car_color()
                 , pos_x=0, pos_y=0, direction=gs.get_random_car_direction()):
        self.speed = speed
        self.color = color

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        print(f"car pos_x = {type(self.pos_x)}")
        print(f"car pos_y = {type(self.pos_y)}")

        self.width = 50
        self.height = 20

    def move(self):
        if self.direction == "left":
            self.pos_x -= 10
        elif self.direction == "right":
            self.pos_x += 10
        else:
            print("Error car direction")

