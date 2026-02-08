from __future__ import annotations
import sys
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QApplication,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget)

# Оголошуємо клас сторінки входу (окремий віджет)
class LoginPage(QWidget):
    # Оголошуємо власний сигнал: "хочу перейти до реєстрації"
    go_to_register = pyqtSignal()

    def __init__(self) -> None:
        super.__init__()
        title = QLabel("Вхід")
        # Поле логіну
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логін або E-mail")
        # Поле паролю
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        # Ховаємо символи паролю
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        form = QFormLayout()
        form.addRow("Логін/E-mail:", self.login_input)
        form.addRow("Пароль:", self.password_input)

        # Кнопка "Увійти"
        login_btn = QPushButton("Увійти")
        # Кнопка "Реєстрації"
        register_btn = QPushButton("Реєстрація")

        register_btn.clicked.connect(self.go_to_register.emit)

        # Горизонтальна розкладка для кнопок
        buttons = QHBoxLayout()
        # Додаємо кнопку входу
        buttons.addWidget(login_btn)
        # Додаємо кнопку реєстрація
        buttons.addWidget(register_btn)

        # Коренева вертикальна розкладка
        root = QVBoxLayout()
        # Заголовок
        root.addWidget(title)
        # Форма
        root.addLayout(form)
        # Кнопки
        root.addLayout(buttons)
        # Додаємо "пружину", щоб елементи були вгорі
        root.addStretch(1)
        # Прив'язуємо розкладку до сторінки
        self.setLayout(root)
# Клас сторінки реєстрації
class RegisterPage(QWidget):
    # Сигнал "хочу перейти на вхід"
    go_to_login = pyqtSignal()
    def __init__(self) -> None:
        super().__init__()
        title = QLabel("Реєстрація")
        # Поле логіну
        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логін або E-mail")
        # Поле паролю
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        # Повтор
        self.password_repeat = QLineEdit()
        self.password_repeat.setPlaceholderText("Повтор пароля")
        self.password_repeat.setEchoMode(QLineEdit.EchoMode.Password)

        form = QFormLayout()
        form.addRow("Логін/E-mail:", self.login_input)
        form.addRow("Пароль:", self.password_input)
        form.addRow("Повтор паролю:", self.password_repeat)

        create_btn = QPushButton("Зареєструватися")
        back_btn = QPushButton("Вхід")
        back_btn.clicked.connect(self.go_to_login.emit)

        buttons = QHBoxLayout()
        buttons.addWidget(create_btn)
        buttons.addWidget(back_btn)

        root = QVBoxLayout()
        root.addWidget(title)
        root.addLayout(form)
        root.addLayout(buttons)
        root.addStretch(1)
        self.setLayout(root)
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