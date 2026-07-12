from Entities.entity import Entity

class Player(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)
        
    def spawn(self):
        print(f"Герой {self.name} з'явився у світі.")

    def talk_to(self, npc):
        print(f"{self.name} Починає розмову з {npc.introduce()}")
        npc.talk()
