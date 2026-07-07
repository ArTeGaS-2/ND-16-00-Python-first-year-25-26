import random

from Entities.goblin import Goblin

names = [
    "Нечепура",
    "Страшко",
    "Кривий",
    "Пуганий",
    "Закреп",
    "Свисток",
    "Шмигач",
    "Роззява",
    "Пук",
    "Сивий",
    "Ерудит",
    "Кволий",
    "Гикач",
    "Пляма"]

def generate_enemy(level):
    name = random.choice(names) # Вобір випадкового імені зі списку
    hp = random.randint(6, 10) + level * 2 # Задаємо кількість ХП випадково але 
                                           # з модифікатором рівня складності
    damage = random.randint(1, 3) + level / 2 # Демедж задаємо як ХП
    # Повертаємо екземпляр ворога як об'єкт класу гоблін з визначеними статами
    return Goblin(name, hp, damage)

def generate_enemies(level, count):
    enemies = [] # створюємо пустий список

    for _ in range(count): 
        enemy = generate_enemy(level) # Зберегли ворога у змінну
        enemies.append(enemy) # Додали ворога до списку
    
    return enemies # Повернули список
