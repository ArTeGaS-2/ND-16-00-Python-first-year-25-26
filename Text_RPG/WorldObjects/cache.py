class Cache:
    def __init__(self, name, loot, gold, discovery_difficeulty):
        self.name = name # Назва тайнику
        self.loot = loot # Що в ньому окрім золота
        self.gold = gold # Чи є золото і скільки
        # Складність виявлення
        self.discovery_difficeulty = discovery_difficeulty
        self.is_discovered = False # Чи виявлено
        self.is_opened = False # Чи було відкрито

    def try_discover(self, perception):
            # Якщо сприйняття більше або дорвнює рівню пастки
            if perception >= self.discovery_difficulty:
                self.is_discovered = True # Пастка виявлена
                print(f"Ви знайшли сховок: {self.name}.")
                return True
            
            return False

    def open(self):
        if not self.is_discovered:
            print("Здається тут є щось цінне.")
            return None

        if self.is_opened:
            print("Цей сховок вже порожній.")
            return None

        self.is_opened = True
        print(f"Знайдено: {self.loot} і {self.gold} золота.")
        return self.loot, self.gold
             