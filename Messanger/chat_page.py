from __future__ import annotations

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QMainWindow,
    QStackedWidget,
    QWidget,
)


class ChatPage(QWidget):
    """Проста сторінка чату з лівою панеллю кнопок."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Messanger — чат")
        self.setStyleSheet("background-color: #090312; color: #f7edff;")

        sidebar = QWidget()
        sidebar.setFixedWidth(88)
        sidebar.setStyleSheet(
            "background-color: #1b1030; border-right: 1px solid #4b2c7a;"
        )

        sidebar_layout = QVBoxLayout()
        sidebar_layout.setContentsMargins(12, 12, 12, 12)
        sidebar_layout.setSpacing(10)

        self.content_stack = QStackedWidget()
        self.content_stack.addWidget(
            self.create_page("Профіль", "Тут буде інформація про користувача, аватар і короткий опис.")
        )
        self.content_stack.addWidget(
            self.create_page("Чати", "Скоро тут буде список чатів з учнями й колегами.")
        )
        self.content_stack.addWidget(
            self.create_page("Збережене", "Тут можна буде зберігати важливі повідомлення або нотатки.")
        )
        self.content_stack.addWidget(
            self.create_page("Налаштування", "Тут з'являться основні налаштування застосунку.")
        )

        buttons = (
            ("Профіль", 0),
            ("Чати", 1),
            ("Збереже\nне", 2),
            ("Налашт\nування", 3),
        )

        for text, page_index in buttons:
            button = QPushButton(text)
            button.setFixedSize(64, 64)
            button.clicked.connect(
                lambda checked=False, index=page_index: self.content_stack.setCurrentIndex(index)
            )
            button.setStyleSheet(
                "QPushButton {"
                "background-color: #271241;"
                "color: #f7edff;"
                "border: 1px solid #6d3db0;"
                "border-radius: 14px;"
                "font-size: 11px;"
                "font-weight: 600;"
                "}"
                "QPushButton:hover {"
                "background-color: #38205e;"
                "}"
            )
            sidebar_layout.addWidget(button, 0, Qt.AlignmentFlag.AlignHCenter)

        sidebar_layout.addStretch(1)
        sidebar.setLayout(sidebar_layout)

        self.content_stack.setCurrentIndex(1)

        body_layout = QHBoxLayout(self)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)
        body_layout.addWidget(sidebar)
        body_layout.addWidget(self.content_stack, 1)

    def create_page(self, title_text: str, info_text: str) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout()
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        title = QLabel(title_text)
        title_font = QFont()
        title_font.setWeight(QFont.Weight.Bold)
        title_font.setPointSize(18)
        title.setFont(title_font)

        info_label = QLabel(info_text)
        info_font = QFont()
        info_font.setWeight(QFont.Weight.Bold)
        info_font.setPointSize(12)
        info_label.setFont(info_font)
        info_label.setWordWrap(True)
        info_label.setStyleSheet(
            "background-color: #201134; color: #f7edff; border: 1px solid #58338f; border-radius: 12px; padding: 12px;"
        )

        layout.addWidget(title)
        layout.addWidget(info_label)
        layout.addStretch(1)
        page.setLayout(layout)
        return page


def create_chat_window() -> QMainWindow:
    """Повертає окремий QMainWindow, якщо потрібен окремий запуск."""
    window = QMainWindow()
    window.setWindowTitle("Messanger — головне вікно")
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
