from __future__ import annotations
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import (
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget)

# Оголошуємо клас сторінки входу (окремий віджет)
class LoginPage(QWidget):
    # Оголошуємо власний сигнал: "хочу перейти до реєстрації"
    go_to_register = pyqtSignal()

    def __init__(self) -> None:
        super().__init__()
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
        login_btn.clicked.connect(self.check_login)
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

    def check_login(self) -> None:
        login = self.login_input.text()
        password = self.password_input.text()
        
        if len(login) > 1 and len(password) > 8:
            QMessageBox.information(self, "Успіх", "Вхід виконано успішно!")
        else:
            QMessageBox.warning(self, "Помилка", "Логін має бути більше 1 символу, а пароль більше 8 символів.")
