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
        create_btn.clicked.connect(self.check_registration)
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

    def check_registration(self) -> None:
        login = self.login_input.text()
        password = self.password_input.text()
        
        if len(login) > 1 and len(password) > 8:
            QMessageBox.information(self, "Успіх", "Реєстрація пройшла успішно!")
        else:
            QMessageBox.warning(self, "Помилка", "Логін має бути більше 1 символу, а пароль більше 8 символів.")
