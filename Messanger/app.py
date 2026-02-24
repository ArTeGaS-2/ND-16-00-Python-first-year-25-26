from __future__ import annotations
import sys
from PyQt6.QtWidgets import QApplication

from main_window import MainWindow

# Функція запуску застосунку
def main() -> int:
    # Створюємо QApplication
    app = QApplication(sys.argv)
    # Створюємо головне вікно
    window = MainWindow()
    # Задаємо розмір
    window.resize(420, 220)
    # Робимо вікно видимим
    window.setVisible(True)
    # Запускаємо цикл подій
    return app.exec()

# Якщо файл запускається напряму — стартуємо main()
if __name__ == "__main__":
    # Завершуємо програму з кодом, який повернула main()
    raise SystemExit(main())