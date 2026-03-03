from __future__ import annotations

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QHBoxLayout,
    QPushButton,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class ProfileSidebar(QWidget):
    """Бічна панель профілю, що «підсвічується» зліва."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFixedWidth(0)
        self.setVisible(False)
        self.setStyleSheet(
            "background-color: #1f1f3d; color: #f8f8f8; border-left: 1px solid #3b3f56;"
        )
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        title = QLabel("Профіль користувача")
        title_font = QFont()
        title_font.setWeight(QFont.Weight.DemiBold)
        title_font.setPointSize(12)
        title.setFont(title_font)
        layout.addWidget(title)
        desc = QLabel("Тут буде базова інформація про аккаунт, статус або ключі.")
        desc.setWordWrap(True)
        desc.setStyleSheet(
            "background-color: #cfd8ff; color: #1b1b32; border-radius: 6px; padding: 6px;"
        )
        layout.addWidget(desc)
        layout.addStretch(1)

    def toggle(self, target_width: int) -> None:
        if self.isVisible():
            self.setFixedWidth(0)
            self.setVisible(False)
        else:
            self.setFixedWidth(target_width)
            self.setVisible(True)


class ChatPage(QWidget):
    """Заглушка головного чату; використовуватиметься як сторінка або окремий віконний модуль."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Messanger — чат")

        self.sidebar = ProfileSidebar(self)
        self.profile_btn = QPushButton("Профіль")
        btn_font = self.profile_btn.font()
        btn_font.setWeight(QFont.Weight.DemiBold)
        self.profile_btn.setFont(btn_font)
        hint = self.profile_btn.sizeHint()
        self.profile_btn.setFixedSize(hint.width() * 3, hint.height() * 3)
        self.profile_btn.clicked.connect(self.open_profile_panel)

        top_bar = QHBoxLayout()
        top_bar.setContentsMargins(0, 0, 0, 0)
        top_bar.addWidget(self.profile_btn)
        top_bar.addStretch(1)

        main_content = QWidget()
        main_layout = QVBoxLayout(main_content)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(top_bar)
        info_label = QLabel("Скоро тут буде чати з учнями й колегами. Чекати лишилось трохи.")
        info_font = QFont()
        info_font.setWeight(QFont.Weight.Bold)
        info_label.setFont(info_font)
        info_label.setStyleSheet(
            "background-color: #eef2ff; color: #111; border-radius: 6px; padding: 10px;"
        )
        main_layout.addWidget(info_label)
        main_layout.addStretch(1)

        body_layout = QHBoxLayout(self)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.addWidget(self.sidebar)
        body_layout.addWidget(main_content, 1)

    def open_profile_panel(self) -> None:
        target_width = max(int(self.width() * 0.25), 220)
        current_visible = self.sidebar.isVisible()
        self.sidebar.toggle(target_width if not current_visible else 0)


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
