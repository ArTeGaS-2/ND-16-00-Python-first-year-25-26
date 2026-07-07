from Entities.entity import Entity

class Player(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        
    def spawn(self):
        print(f"Герой {self.name} з'явився у світі.")
 