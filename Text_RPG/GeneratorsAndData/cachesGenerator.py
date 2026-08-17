import random

from WorldObjects.cache import Cache

cache_names = [
    "Стара скринька",
    "Мішечок під камінням",
    "Непримітний сховок у куті кімнати"
]

loot_names = [
    "Лікувальна настоянка",
    "Старий ключ",
    "Карта місцевості",
    "Амулет від проклять",
    "Дворянські чоботи"
]

def generate_cache(peception_lvl):
    loot_count = random.randint(1,2)
    loot = []

    for _ in range(loot_count):
        loot.append(random.choice(loot_names))

    return Cache(
        random.choice(cache_names),
        loot,
        random.randint(2,8) * peception_lvl,
        random.randint(1,3) + peception_lvl
    )

