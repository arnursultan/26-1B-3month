import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from ui import TaskManagerUI
import database as db

class TaskApp(TaskManagerUI):
    def __init__(self):
        super().__init__()
        db.init_db()
        self.load_tasks()

        self.current_task_id = None

        self.add_button.clicked.connect(self.save_task)
        self.search_button.clicked.connect(self.search_task)
        self.delete_button.clicked.connect(self.delete_selected)
        self.task_list.itemDoubleClicked.connect(self.load_selected_for_edit)
        self.filter_status_combo.currentTextChanged.connect(self.load_tasks)

    def load_tasks(self):
        self.task_list.clear()
        tasks = db.get_tasks(self.filter_status_combo.currentText())
        for task in tasks:
            item = f"{task[0]}: {task[1]} [{task[3]}] | {task[4]}"
            self.task_list.addItem(item)

    def save_task(self):
        title = self.title_input.text()
        description = self.desc_input.toPlainText()
        status = self.status_combo.currentText()

        if not title:
            QMessageBox.warning(self, "Ошибка", "Название задачи не может быть пустым.")
            return

        if self.current_task_id:
            db.update_task(self.current_task_id, title, description, status)
            QMessageBox.information(self, "Успех", "Задача обновлена.")
            self.current_task_id = None
        else:
            db.add_task(title, description, status)

        self.clear_fields()
        self.load_tasks()

    def search_task(self):
        query = self.search_input.text()
        results = db.search_tasks(query)
        self.task_list.clear()
        for task in results:
            item = f"{task[0]}: {task[1]} [{task[3]}] | {task[4]}"
            self.task_list.addItem(item)

    def delete_selected(self):
        selected = self.task_list.currentItem()
        if selected:
            task_id = int(selected.text().split(":")[0])
            db.delete_task(task_id)
            self.load_tasks()

    def load_selected_for_edit(self):
        selected = self.task_list.currentItem()
        if selected:
            task_id = int(selected.text().split(":")[0])
            task = db.get_task_by_id(task_id)
            if task:
                self.current_task_id = task[0]
                self.title_input.setText(task[1])
                self.desc_input.setText(task[2])
                self.status_combo.setCurrentText(task[3])
                self.add_button.setText("Сохранить изменения")

    def clear_fields(self):
        self.title_input.clear()
        self.desc_input.clear()
        self.status_combo.setCurrentIndex(0)
        self.add_button.setText("Сохранить / Добавить")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaskApp()
    window.show()
    sys.exit(app.exec())
