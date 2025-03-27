from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QIcon
import sys
import random


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.click_count = 0
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Супер Пример QVBoxLayout!")
        self.resize(350, 250)

        layout = QVBoxLayout()

        self.label = QLabel("Привет, мир!")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.button_change = QPushButton("Изменить текст")
        self.button_change.setIcon(QIcon("icons/change.png"))

        self.button_exit = QPushButton("Выйти")
        self.button_exit.setIcon(QIcon("icons/exit.jpg"))  #

        layout.addWidget(self.label)
        layout.addWidget(self.button_change)
        layout.addWidget(self.button_exit)

        self.setLayout(layout)

        self.button_change.clicked.connect(self.change_text)
        self.button_exit.clicked.connect(self.close_app)

        self.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                color: #FFFFFF;
                font-family: 'Arial';
            }
            QLabel {
                font-size: 18px;
                font-weight: bold;
                margin-top: 10px;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border-radius: 8px;
                border: 2px solid #4CAF50;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3e8e41;
            }
        """)

    def change_text(self):
        self.click_count += 1

        texts = [
            "Текст изменён!",
            "Как дела?",
            "Ты чилловый парень!",
            "PyQt6 рулит!",
            "Вперёд к успеху!",
            "Клики: {}".format(self.click_count)
        ]

        new_text = random.choice(texts)

        self.label.setText("")
        QTimer.singleShot(200, lambda: self.label.setText(new_text))

        self.label.adjustSize()

    def close_app(self):
        self.label.setText("Пока!")
        QTimer.singleShot(500, self.close)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())