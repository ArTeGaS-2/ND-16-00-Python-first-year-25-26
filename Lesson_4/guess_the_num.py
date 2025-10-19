import random

num = random.randint(1, 100)

counter = 0

while True:
    guess = input("Вгадайте число, від 1 до 100:")
    counter += 1
    if num == int(guess):
        print(f"Вірно. Кількість спроб: {counter}")
    elif num > int(guess):
        print("Більше")
    elif num < int(guess):
        print("Менше")