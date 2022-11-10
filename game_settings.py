"""Setting variables tweaked here"""
import random

# Car settings
CAR_SPEED_MIN = 10
CAR_SPEED_MAX = 45


def get_random_car_color():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'black']
    return random.choice(colors)


def get_random_car_direction():
    direction = ['left', 'right']
    return random.choice(direction)

