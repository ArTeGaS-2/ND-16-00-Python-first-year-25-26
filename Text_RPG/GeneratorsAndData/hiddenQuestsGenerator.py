import random

from Quests.hiddenQuest import HiddenQuest

quests = [
    {"title": "Приховане світло",
     "description": "Ви бачите щілину з якої ллє м'яке світло. З'ясуйте що це",
     "reward": "Камінь світла",
     "discovery_difficulty": 6},

    {"title": "Прихована темрява",
     "description": "Ви бачите щілину з якої ллє м'яка темрява. З'ясуйте що це",
     "reward": "Камінь темряви",
     "discovery_difficulty": 6}
]

def generate_hidden_quest():
    quest_data = random.choice(quests) # Обираємо випадковий квест

    return HiddenQuest( # повертаємо його екземпляр
        quest_data["title"], # назва
        quest_data["description"], # опис
        quest_data["reward"], # нагорода
        quest_data["discovery_difficulty"] # складність виявлення
    )

def generate_hidden_quests(count):
    hidden_quests = []

    for _ in range(count):
        hidden_quests.append(generate_hidden_quest())

    return hidden_quests