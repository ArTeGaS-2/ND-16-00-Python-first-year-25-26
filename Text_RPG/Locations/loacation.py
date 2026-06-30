class Location:
    def __init__(self, name, difficult_level, number_of_instances):
        self.name = name
        self.difficult_level = difficult_level
        self.number_of_instances = number_of_instances
        self.instances = []

    def onEnter(self):
        for _ in range(self.number_of_instances):
            inst = {"enemies": [],
                    "NPCs": [],
                    "hidden_things": [],
                    "traps": [],
                    "hidden_quests":[],
                    "caches": []}

        print(f"Ви увійши до {self.name}.")

    def inside(self):
        pass

    def onExit(self):
        pass