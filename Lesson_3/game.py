from player import Player
from enemy import Enemy

def main():
    p = Player("Mage", 20, 4)
    e = Enemy("Goblin", 20, 3)

    while p.is_alive() and e.is_alive():
        if p.turn(e):
            break
        if e.turn(p):
            break
    print("Кінець бою.")

if __name__ == "__main__":
    main()