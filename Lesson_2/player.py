import random

name = "Mage"
health = 20
level = 4

def DoDamage(hero_name, enemy_name,
        enemy_health,
        hero_level):
    damage = random.randint(1,3) * hero_level
    
    if enemy_health > damage:
        health = enemy_health - damage
        print(f"{enemy_name} наніс {hero_name}: {damage} шкоди."
              f"Лишилось {health} хп.")
    else:
        health = enemy_health - damage
        print(f"{name} помер.")