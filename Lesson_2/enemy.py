import random

enemy_name = "Goblin"
enemy_health_global = 20
enemy_level = 3

def DoDamage(hero_name, enemy_name,
        enemy_health,
        hero_level):
    damage = random.randint(1,3) * hero_level
    
    if enemy_health > damage:
        enemy_health_global = enemy_health - damage
        print(f"{enemy_name} наніс {hero_name}: {damage} шкоди."
              f"Лишилось {enemy_health} хп.")
    else:
        enemy_health_global = enemy_health - damage
        print(f"{enemy_name} помер.")