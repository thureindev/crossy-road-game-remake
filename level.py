"""
Level Class to control unique level behaviours
"""
import random
from carspawnbase import CarSpawnBase as Base


class Level:
    def __init__(self, name="another level", num=1):
        self.name = name
        self.num = num
        self.spawn_bases = []
        a_base = Base()
        self.spawn_bases.append(a_base)

