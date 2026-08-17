import random

from Locations.location import Location
from Entities.player import Player

random.seed(1) # Фіксуємо випадковість конкретним сідом

player = Player("Artas", 10, 3)

location = Location("Дивна печера", 2, 3)
location.onEnter()

#print("Кількість зон:", len(location.instances))
#location.instances[0]["enemies"][0].spawn()
#location.instances[0]["NPCs"][0].talk() 

#trap = location.instances[0]["traps"][0]
#player.handle_trap(trap)

#location.instances[0]["hidden_quests"][0].try_discover(20)
location.show_hidden_quest(0)
