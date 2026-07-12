import random

from GeneratorsAndData.enemiesGenerator import generate_enemies
from GeneratorsAndData.npcGenerator import generate_npcs

class Location:
    def __init__(self, name, difficult_level, number_of_instances):
        self.name = name
        self.difficult_level = difficult_level
        self.number_of_instances = number_of_instances
        self.instances = []

    def onEnter(self):
        self.instances = [] # Очищуємо список
        for number in range(self.number_of_instances):
            enemies_count = random.randint(1, self.difficult_level + 1)
            npcs_count = random.randint(0, 2)

            instance = {"name": f"Зона {number + 1}",
                        "enemies": generate_enemies(self.difficult_level,
                                                    enemies_count),
                        "NPCs": generate_npcs(npcs_count),
                        "hidden_things": [],
                        "traps": [],
                        "hidden_quests":[],
                        "caches": []}
            self.instances.append(instance)

        print(f"Ви увійши до {self.name}.")

    def inside(self):
        pass

    def onExit(self):
        pass