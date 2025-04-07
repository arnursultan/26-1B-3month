from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHBoxLayout
)
from PyQt6.QtCore import Qt

class ContactApp(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.setWindowTitle("Контакты (PyQt6)")
        self.setGeometry(100, 100, 600, 400)
        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Телефон")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.add_btn = QPushButton("Добавить контакт")
        self.add_btn.clicked.connect(self.add_contact)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Поиск по имени")
        self.search_btn = QPushButton("Найти")
        self.search_btn.clicked.connect(self.search_contacts)

        self.refresh_btn = QPushButton("Показать все")
        self.refresh_btn.clicked.connect(self.load_contacts)

        self.contacts_table = QTableWidget()
        self.contacts_table.setColumnCount(4)
        self.contacts_table.setHorizontalHeaderLabels(["ID", "Имя", "Телефон", "Email"])
        self.contacts_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        self.delete_input = QLineEdit()
        self.delete_input.setPlaceholderText("ID для удаления")
        self.delete_btn = QPushButton("Удалить")
        self.delete_btn.clicked.connect(self.delete_contact)

        self.layout.addWidget(QLabel("Добавить контакт:"))
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.phone_input)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.add_btn)

        self.layout.addWidget(QLabel("Поиск контакта:"))
        search_layout = QHBoxLayout()
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)
        search_layout.addWidget(self.refresh_btn)
        self.layout.addLayout(search_layout)

        self.layout.addWidget(self.contacts_table)

        self.layout.addWidget(QLabel("Удалить контакт по ID:"))
        delete_layout = QHBoxLayout()
        delete_layout.addWidget(self.delete_input)
        delete_layout.addWidget(self.delete_btn)
        self.layout.addLayout(delete_layout)

        self.setLayout(self.layout)
        self.load_contacts()

    def add_contact(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        email = self.email_input.text()
        if name:
            self.db.add_contact(name, phone, email)
            self.load_contacts()
            self.name_input.clear()
            self.phone_input.clear()
            self.email_input.clear()

    def load_contacts(self):
        self.contacts_table.setRowCount(0)
        for row_data in self.db.get_all_contacts():
            row_number = self.contacts_table.rowCount()
            self.contacts_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.contacts_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def search_contacts(self):
        name = self.search_input.text()
        results = self.db.search_contacts(name)
        self.contacts_table.setRowCount(0)
        for row_data in results:
            row_number = self.contacts_table.rowCount()
            self.contacts_table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.contacts_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def delete_contact(self):
        try:
            contact_id = int(self.delete_input.text())
            self.db.delete_contact(contact_id)
            self.load_contacts()
            self.delete_input.clear()
        except ValueError:
            pass
