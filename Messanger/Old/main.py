import sys
from PyQt6.QtWidgets import (
    QApplication, # Застосунок
    QWidget,      # Базове вікно
    QLabel,       # Текст
    QPushButton,  # Кнопка
    QVBoxLayout,  # Вертикальна розкладка
    QFormLayout,
    QLineEdit)

# Створюємо застосунок
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Вхід")

label = QLabel("Натисни кнопку") 
button = QPushButton("Натисни мене")

def on_click():
    label.setText("Працює! Кнопку натиснули")
button.clicked.connect(on_click)

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(button)
window.setLayout(layout)

window.resize(300,100) # Ширина(X) і висота(Y)
window.setVisible(True)

sys.exit(app.exec())