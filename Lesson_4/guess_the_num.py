import random

random_num = random.randint(1, 100)

while True:
    guess = int(input("Вгадайте число від 1 до 100: "))
    if random_num == guess:
        print("Ви вгадали!")
    elif random_num > guess:
        print("Загадане число більше.")
    elif random_num < guess:
        print("Загадане число менше.")
    
