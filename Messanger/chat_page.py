from __future__ import annotations

import sys

from PyQt6.QtWidgets import(
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget)

class ChatPage(QWidget):  
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Messanger - чат")
        
        info_lable = QLabel("Скоро тут буде чат")

        layout = QVBoxLayout()
        layout.addWidget(info_lable)
        layout.addStretch(1)
        self.setLayout(layout)

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

