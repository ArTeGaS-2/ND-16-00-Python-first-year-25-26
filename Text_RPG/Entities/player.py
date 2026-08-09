from Entities.entity import Entity

class Player(Entity):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp, damage)

        self.strenght = 10
        self.perception = 10
        self.endurance = 10
        self.charisma = 10
        self.intelligence = 10
        self.agility = 10
        self.luck = 10
        
    def spawn(self):
        print(f"Герой {self.name} з'явився у світі.")

    def talk_to(self, npc):
        print(f"{self.name} Починає розмову з {npc.introduce()}")
        npc.talk()

    def handle_trap(self, trap):
        print(f"{self.name} перевіряє шлях поперду...")

        if trap.try_discover(self.perception):
            answer = input("Знешкодити пастку? (так/ні): \n")

            if answer.lower() == "так":
                trap.disarm()
                return
            
        trap.activate(self)