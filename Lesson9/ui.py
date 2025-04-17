from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLineEdit,
    QTextEdit, QListWidget, QListWidgetItem, QHBoxLayout,
    QLabel, QComboBox
)

class TaskManagerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task Manager")
        self.setGeometry(300, 100, 600, 600)

        self.layout = QVBoxLayout()

        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Название задачи")
        self.layout.addWidget(self.title_input)

        self.desc_input = QTextEdit()
        self.desc_input.setPlaceholderText("Описание")
        self.layout.addWidget(self.desc_input)

        self.status_combo = QComboBox()
        self.status_combo.addItems(["не выполнено", "выполнено"])
        self.layout.addWidget(self.status_combo)

        self.add_button = QPushButton("Сохранить / Добавить")
        self.layout.addWidget(self.add_button)

        filter_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по названию или статусу")
        filter_layout.addWidget(self.search_input)

        self.search_button = QPushButton("Найти")
        filter_layout.addWidget(self.search_button)

        self.filter_status_combo = QComboBox()
        self.filter_status_combo.addItems(["все", "не выполнено", "выполнено"])
        filter_layout.addWidget(self.filter_status_combo)

        self.layout.addLayout(filter_layout)

        self.task_list = QListWidget()
        self.layout.addWidget(self.task_list)

        self.delete_button = QPushButton("Удалить выбранную задачу")
        self.layout.addWidget(self.delete_button)

        self.setLayout(self.layout)
