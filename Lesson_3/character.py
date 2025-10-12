import random

class Character:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def is_alive(self):
        return self.health > 0
    
    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)

    def attack(self, target):
        dmg = random.randint(1,3) * self.level
        target.take_damage(dmg)
        return dmg
    
    def turn(self, defender):
        dmg = self.attack(defender)
        print(f"{self.name} вдарив {defender.name} на {dmg}. У "
              f"{defender.name}: {defender.health} хп.")
        if not defender.is_alive():
            print(f"{defender.name} помер.")
            return True
        return False