import random

from Locations.location import Location

random.seed(1) # Фіксуємо випадковість конкретним сідом

location = Location("Дивна печера", 2, 3)
location.onEnter()

print("Кількість зон:", len(location.instances))
location.instances[0]["enemies"][0].spawn()
location.instances[0]["NPCs"][0].talk()