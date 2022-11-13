"""CarSpawnBase Class to control spawn positions and randomness of cars spawned"""
from car import Car
import game_settings as gs


class CarSpawnBase:
    def __init__(self, pos_x=0, pos_y=0, direction="left"):
        self.pos_x = int(pos_x)
        self.pos_y = pos_y
        self.direction = direction

        self.interval = 2
        self.cars = []

    def produce_random_car(self):
        pos_y = self.pos_y

        for _ in range(0, 5):
            direction = gs.get_random_car_direction()
            if direction == "left":
                pos_x = gs.SCREEN_WIDTH
            elif direction == "right":
                pos_x = 0
            else:
                print("Error! direction error.")

            car = Car(pos_x=pos_x, pos_y=pos_y, direction=direction, color=gs.get_random_car_color(),
                      speed=gs.get_random_car_speed())
            self.cars.append(car)

            pos_y += 50

        return car


