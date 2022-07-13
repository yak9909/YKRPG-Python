import random
from .entity import *


class Enemy(Entity):
    def __init__(self):
        super().__init__()
        
        self.health = 50
        self.attack = 30
        self.defence = 0
        self.speed = 0

