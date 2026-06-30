class Entity():
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def spawn(self):
        print(f"{self.name} з'явився у світі.")

    def take_damage(self, damage):
        print(f"{self.name} отримує {damage} шкоди. Залишилось {self.hp}")
        self.hp -= damage

    def do_damage(self, target):
        print(f"{self.name} наносить {target.name} {self.damage} шкоди")
        target.take_damage(self.damage)

 