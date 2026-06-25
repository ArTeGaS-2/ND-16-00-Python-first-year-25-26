from player import Player
from goblin import Goblin

class Game():
    def __init__(self):
        self.hero = Player("Artas", 20, 4)
        self.enemy = Goblin("Spoon", 7, 1.3)
    
    def next_turn(self):
        self.hero.do_damage(self.enemy)
        self.enemy.do_damage(self.hero)

    def event_handler(self):

        print("Бій!")
        self.hero.spawn()
        self.enemy.spawn()

        while self.hero.hp > 0 or self.enemy.hp > 0:
            self.next_turn()

        print("Бій завершено.")

    def run(self):
        self.event_handler()