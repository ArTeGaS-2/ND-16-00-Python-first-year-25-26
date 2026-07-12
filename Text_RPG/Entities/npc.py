# Text_RPG/Entities/npc.py
class NPC:
    def __init__(self, name, role, phrase):
        self.name = name
        self.role = role
        self.phrase = phrase

    def introduce(self):
        # Представляємо персонажа на сцені
        print(f"{self.name} - {self.role}")

    def talk(self):
        # Фраза, яку каже персонаж в діалозі
        print(f"{self.name}: {self.phrase}")