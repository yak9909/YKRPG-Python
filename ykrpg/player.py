import random
from .entity import *


class Player(Entity):
    def __init__(self):
        super().__init__()
        
        self.health = 100
        self.attack = 15
        self.defence = 0
        self.speed = 0

