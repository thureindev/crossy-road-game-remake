"""CarSpawnBase Class to control spawn positions and randomness of cars spawned"""
from car import Car


class CarSpawnBase:
    def __init__(self):
        self.cars = []
        a_car = Car()
        self.cars.append(a_car)

