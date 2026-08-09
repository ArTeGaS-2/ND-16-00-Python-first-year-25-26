class Trap:
    def __init__(self, name, damage, discovery_difficulty):
        self.name = name # Назва пастки
        self.damage = damage # Шкода яку нанесу
        # Рівень пастки, складність виявлення
        self.discovery_difficulty = discovery_difficulty
        self.is_discovered = False # Чи була виявлена
        self.is_active = True # Чи є наразі активною

    def try_discover(self, perception):
        # Якщо сприйняття більше або дорвнює рівню пастки
        if perception >= self.discovery_difficulty:
            self.is_discovered = True # Пастка виявлена
            print(f"Виявлено пастку: {self.name}.")
            return True
        
        return False
    
    def activate(self, target):
        if not self.is_active: # Якщо пастка не активна
            return # Не виконуємо код нижче
        
        print(f"Спрацювала пастка: {self.name}.")
        target.take_damage(self.damage) # Наносимо визначену шкоду цілі
        self.is_active = False # Деактивуємо пастку

    def disarm(self): # Знешкодження пастки
        if self.is_discovered and self.is_active:
            self.is_active = False
            print(f"Пастку {self.name} знешкоджено.")
            return True
        
        return False
