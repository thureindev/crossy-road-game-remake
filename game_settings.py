"""Setting variables tweaked here"""
import random
CLOCK_TICK = 50  # in milliseconds

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Car settings
CAR_SPEED_MIN = 10
CAR_SPEED_MAX = 45


def get_random_car_color():
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'black']
    return random.choice(colors)


def get_random_car_speed():
    return random.randint(CAR_SPEED_MIN, CAR_SPEED_MAX)


def get_random_car_direction():
    direction = ['left', 'right']
    return random.choice(direction)

