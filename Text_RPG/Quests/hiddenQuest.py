class HiddenQuest:
    def __init__(self, title, description, reward, discovery_difficulty):

        # Назва квесту
        self.title = title
        # Опис квесту
        self.description = description
        # Нагорода за квест
        self.reward = reward
        # Складність виявлення
        self.discovery_difficulty = discovery_difficulty

        # Чи знайдено квест
        self.is_discovered = False
        # Чи завершено квест
        self.is_complited = False

    def try_dsicover(self, perception):
        # Якщо увага більша або дорівнює рівню виявлення
        if perception >= self.discovery_difficulty:
            # Квест стає виявленим
            self.is_discovered = True
            # Друкується заголовок/назва
            print(f"Знайдено прихований квест: {self.title}")
            # Пустий рядок
            print()
            # Друкується опис
            print(self.description)
            # Повертається значення - правда
            return True
        
        return False

    def show_info(self):
        if self.is_discovered:
            print(self.title)
            print()
            print(self.description)

    def complete(self):
        if not self.is_discovered or self.is_complited:
            return False

        self.is_complited = True
        print(f"Квест виконано. Нагорода: {self.reward}")
        return True
    