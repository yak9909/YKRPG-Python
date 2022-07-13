import random


class Entity:
    def __init__(self, health=0, attack=0, defence=0, speed=0):
        self.health = health
        self.attack = attack
        self.defence = defence
        self.speed = speed
        
        self.alive = True
    
    def take_damage(self, damage):
        damage_adjust = round(max(1, damage - self.defence))
        self.health -= damage_adjust
        
        if self.health <= 0:
            self.alive = False
        
        return self.alive
    
    def attack_to(self, obj):
        damage = self.damage_calc()
        obj.take_damage(damage)
        return damage
    
    def damage_calc(self):
        damage_min = max(1, round(self.attack/1.2))
        damage_max = self.attack
        damage = random.randint(damage_min, damage_max)

        return damage
