import random

from GeneratorsAndData.enemiesGenerator import generate_enemies
from GeneratorsAndData.npcGenerator import generate_npcs
from GeneratorsAndData.trapsGenerator import generate_traps
from GeneratorsAndData.hiddenQuestsGenerator import generate_hidden_quests

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
            npcs_count = random.randint(1, 5)
            traps_count = random.randint(1, 5)
            hidden_quests_count = random.randint(1,2)

            instance = {"name": f"Зона {number + 1}",
                        "enemies": generate_enemies(self.difficult_level,
                                                    enemies_count),
                        "NPCs": generate_npcs(npcs_count),
                        "hidden_things": [],
                        "traps": generate_traps(self.difficult_level, traps_count),
                        "hidden_quests": generate_hidden_quests(hidden_quests_count),
                        "caches": []}
            self.instances.append(instance)

        print(f"Ви увійши до {self.name}.")

    def inside(self):
        pass

    def onExit(self):
        pass

    def show_hidden_quest(self ,quest_index):
        current_quest = self.instances[0]["hidden_quests"][quest_index]

        print("Назва: ", current_quest.title)
        print("Опис: ", current_quest.description)
        print("Нагорода: ", current_quest.reward)
        print()
