import random

from WorldObjects.trap import Trap

trap_names = [
    "Яма з кілками",
    "Отруйна голка зі стіни",
    "Камінь з люка над персонажем",
    "Кислотний туман",
    "Бананова шкірка",
    "Чари переляку"
]

def generate_trap(level):
    damage = random.randint(1, 4) + level
    difficulty = random.randint(1, 3) + level

    # Повертаємо об'єкт/екземпляр класу Trap(Пастка)
    return Trap(random.choice(trap_names), damage, difficulty)

def generate_traps(level, count):
    traps = []

    for _ in range(count):
        traps.append(generate_trap(level))

    return traps