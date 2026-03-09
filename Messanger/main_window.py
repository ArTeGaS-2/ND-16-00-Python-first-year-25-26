from __future__ import annotations
from PyQt6.QtWidgets import (
    QStackedWidget,
    QVBoxLayout,
    QWidget)

from login_page import LoginPage
from register_page import RegisterPage

# Головне вікно, яке перемикає сторінки
class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Auth demo (PyQt6)")
        # Стек сторінок (показує одну з багатьох)
        self.stack = QStackedWidget()
        # Створюємо сторінку входу
        self.login_page = LoginPage()
        # Створюємо сторінку реєстрації
        self.register_page = RegisterPage()
        # Додаємо сторінку входу як 0-й елемент
        self.stack.addWidget(self.login_page)
        # Додаємо сторінку реєстрації як 1-й елемент
        self.stack.addWidget(self.register_page)

        # Функція: показати вхід (індекс 0)
        def open_login() -> None:
            # Перемикаємо стек на сторінку 0
            self.stack.setCurrentIndex(0)
        # Функція: показати реєстрацію (індекс 1)
        def open_register() -> None:
            # Перемикаємо стек на сторінку 1
            self.stack.setCurrentIndex(1)

        # При сигналі зі сторінки входу — відкриваємо реєстрацію
        self.login_page.go_to_register.connect(open_register)
        # При сигналі зі сторінки реєстрації — відкриваємо вхід
        self.register_page.go_to_login.connect(open_login)

        # Коренева розкладка вікна
        root = QVBoxLayout()
        # Додаємо стек у розкладку
        root.addWidget(self.stack)
        # Встановлюємо розкладку для вікна
        self.setLayout(root)
        # Показуємо вхід за замовчуванням
        open_login()
