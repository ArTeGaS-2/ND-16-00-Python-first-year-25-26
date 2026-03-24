from __future__ import annotations

import sys

from PyQt6.QtWidgets import(
    QApplication,
    QHBoxLayout,
    QLineEdit,
    QPlainTextEdit,
    QPushButton,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget)

class ChatPage(QWidget):  
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Messanger - чат")
        self.reply_index = 0
        self.replies = [
            "Бубузян: Ми захопимо всесвіт!",
            "Ізюбрь: Дєд, пий таблетки.",
            "Кукуха: Бліцкріг!!!"
        ]
        
        title_lable = QLabel("Вікно чату")
        info_lable = QLabel("Перша версія: один чат без БД")

        self.history_box = QPlainTextEdit()
        self.history_box.setReadOnly(True)
        self.history_box.setPlainText(
            "Бубузян: Привіт! Це перша версія чату. \n"
            "Ти: Тут уже можна писати повідомлення.")
        
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Напиши повідомлення...")
        self.message_input.returnPressed.connect(self.send_message)

        send_button = QPushButton("Надіслати")
        send_button.clicked.connect(self.send_message)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.message_input, 1)
        bottom_layout.addWidget(send_button)

        layout = QVBoxLayout()
        layout.addWidget(title_lable)
        layout.addWidget(info_lable)
        layout.addWidget(self.history_box, 1)
        layout.addLayout(bottom_layout)
        self.setLayout(layout)

    def send_message(self) -> None:
        text = self.message_input.text().strip()
        if not text: 
            return
        
        self.history_box.appendPlainText(f"Ти: {text}")
        self.history_box.appendPlainText(self.get_reply())
        self.message_input.clear()
    
    def get_reply(self) -> str:
        reply = self.replies[self.reply_index]
        self.reply_index += 1

        if self.reply_index >= len(self.replies):
            self.reply_index = 0

        return reply

def create_chat_window() -> QMainWindow:
    window = QMainWindow()
    window.setWindowTitle("Messanger - головне вікно")

    page = ChatPage()
    window.setCentralWidget(page)
    window.resize(640, 420)
    return window

def main() -> int:
    app = QApplication(sys.argv)
    window = create_chat_window()
    window.show()
    return app.exec()

if __name__ == "__main__":
    raise SystemExit(main())

