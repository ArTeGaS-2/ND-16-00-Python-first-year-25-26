from Entities.player import Player
from Entities.goblin import Goblin

class Game():
    def __init__(self):
        self.hero = Player("Artas", 20, 4)
        self.enemy = Goblin("Spoon", 7, 1.3)
        self.is_all_alive = True
    
    def next_turn(self):
        self.hero.do_damage(self.enemy)
        self.enemy.do_damage(self.hero)

    def event_handler(self):
        self.duel(self.hero, self.enemy)

    def duel(self, first_opponent, second_opponent):
        print("Бій!")
        first_opponent.spawn()
        second_opponent.spawn()

        while self.is_all_alive:
            if first_opponent.hp > 0 and second_opponent.hp > 0:
                self.next_turn()
            else:
                self.is_all_alive = False

        print("Бій завершено.")

    def run(self):
        self.event_handler()