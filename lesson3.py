# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QPushButton")
#         self.resize(300, 200)
#
#         button = QPushButton("Нажми меня", self)
#         button.move(100, 80)
#
#         button.clicked.connect(self.button_clicked)
#
#     def button_clicked(self):
#         print("Кнопка нажата!")
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QLineEdit")
#         self.resize(300, 150)
#
#         self.text_input = QLineEdit(self)
#         self.text_input.move(50, 50)
#
#         button = QPushButton("Показать текст", self)
#         button.move(50, 90)
#         button.clicked.connect(self.show_text)
#
#     def show_text(self):
#         text = self.text_input.text()
#         print(f"Ввёденный текст: {text}")
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QTextEdit")
#         self.resize(300, 200)
#
#         self.text_edit = QTextEdit(self)
#         self.text_edit.setGeometry(50, 30, 200, 100)
#
#         button = QPushButton("Показать текст", self)
#         button.move(100, 140)
#         button.clicked.connect(self.show_text)
#
#     def show_text(self):
#         text = self.text_edit.toPlainText()
#         print(f"Ввёденный текст:\n{text}")
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QComboBox, QLabel
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QComboBox")
#         self.resize(300, 150)
#
#         self.combo = QComboBox(self)
#         self.combo.addItems(["Python", "Java", "C++", "JavaScript"])
#         self.combo.move(50, 50)
#
#         self.label = QLabel("Выберите язык", self)
#         self.label.move(50, 90)
#
#         self.combo.currentIndexChanged.connect(self.update_label)
#
#     def update_label(self):
#         self.label.setText(f"Вы выбрали: {self.combo.currentText()}")
#         self.label.adjustSize()
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLabel
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QCheckBox")
#         self.resize(300, 150)
#
#         self.checkbox = QCheckBox("Согласен с условиями", self)
#         self.checkbox.move(50, 50)
#
#         self.label = QLabel("",self)
#         self.label.move(50, 90)
#
#         self.checkbox.stateChanged.connect(self.update_label)
#
#     def update_label(self, state):
#         if state == 2:
#             self.label.setText("Вы согласились!")
#         else:
#             self.label.setText("")
#
#         self.label.adjustSize()
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

# from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel
# import sys
#
# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.setWindowTitle("Пример QRadioButton")
#         self.resize(300, 150)
#
#         self.radio1 = QRadioButton("Вариант 1", self)
#         self.radio1.move(50, 50)
#
#         self.radio2 = QRadioButton("Вариант 2", self)
#         self.radio2.move(50, 80)
#
#         self.label = QLabel("Выберите вариант", self)
#         self.label.move(50, 120)
#
#         self.radio1.toggled.connect(self.update_label)
#         self.radio2.toggled.connect(self.update_label)
#
#     def update_label(self):
#         if self.radio1.isChecked():
#             self.label.setText("Вы выбрали вариант 1")
#         elif self.radio2.isChecked():
#             self.label.setText("Вы выбрали вариант 2")
#
#         self.label.adjustSize()
#
# app = QApplication(sys.argv)
# window = MyWindow()
# window.show()
# sys.exit(app.exec())

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