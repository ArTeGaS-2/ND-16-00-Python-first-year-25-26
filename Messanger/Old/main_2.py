import sys
from PyQt6.QtWidgets import (
    QApplication, # Застосунок
    QWidget,      # Базове вікно
    QLabel,       # Текст
    QPushButton,  # Кнопка
    QVBoxLayout,  # Вертикальна розкладка
    QFormLayout,
    QLineEdit,
    QMessageBox)

# Створюємо застосунок
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Вхід")

login_input = QLineEdit()
login_input.setPlaceholderText("Логін або Email")

password_input = QLineEdit()
password_input.setPlaceholderText("Пароль")
password_input.setEchoMode(QLineEdit.EchoMode.Password)

def on_login():
    login = login_input.text()
    password = password_input.text()
    QMessageBox.information(window, "Демонстрація",
         f"Логін: {login}\nПароль: {len(password)} символів")
    
form = QFormLayout()
form.addRow("Логін/E-mail:", login_input)
form.addRow("Пароль:", password_input)

btn = QPushButton("Увійти")
btn.clicked.connect(on_login)

root = QVBoxLayout()
root.addLayout(form)
root.addWidget(btn)
window.setLayout(root)

window.resize(300,100) # Ширина(X) і висота(Y)
window.setVisible(True)

sys.exit(app.exec())