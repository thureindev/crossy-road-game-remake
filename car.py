"""
Car Class to control each car instance. speed, appearance, etc.
Level obj instance will contain CarSpawnBase obj
"""
import game_settings as gs


class Car:
    def __init__(self, speed=gs.get_random_car_speed(), color=gs.get_random_car_color()
                 , pos_x=0, pos_y=0, direction=gs.get_random_car_direction()):
        self.speed = speed
        self.color = color

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction

        self.width = 50
        self.height = 20

        self.draw_x0 = self.pos_x - (self.width / 2)
        self.draw_x1 = self.pos_x + (self.width / 2)
        self.draw_y0 = self.pos_y - (self.height / 2)
        self.draw_y1 = self.pos_y + (self.height / 2)

    def move(self):
        if self.direction == "left":
            self.pos_x -= self.speed
        elif self.direction == "right":
            self.pos_x += self.speed
        else:
            print("Error car direction")

        self.draw_x0 = self.pos_x - (self.width / 2)
        self.draw_x1 = self.pos_x + (self.width / 2)
        self.draw_y0 = self.pos_y - (self.height / 2)
        self.draw_y1 = self.pos_y + (self.height / 2)

