from Entities.entity import Entity

class Goblin(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

    def spawn(self):
        print(f"Мерзенний гоблін {self.name} з'явився у світі.")