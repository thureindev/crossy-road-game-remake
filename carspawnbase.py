"""CarSpawnBase Class to control spawn positions and randomness of cars spawned"""
from car import Car


class CarSpawnBase:
    def __init__(self, pos_x=0, pos_y=0, direction="left"):
        self.pos_x = int(pos_x)
        self.pos_y = pos_y
        self.direction = direction

        print(f"carspawnbase pos_x = {type(self.pos_x)}")
        print(f"carspawnbase pos_y = {type(self.pos_y)}")

        self.interval = 2
        self.cars = []

    def produce_random_car(self):
        car = Car(pos_x=self.pos_x, pos_y=self.pos_y, direction=self.direction)
        self.cars.append(car)

        return car


