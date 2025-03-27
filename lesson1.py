# Код #1
# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel
#
# app = QApplication(sys.argv)
#
# window = QWidget()
# window.setWindowTitle("Пример, PyQt6!")
# window.resize(300, 200)
#
# label = QLabel("Привет, мир!", parent=window)
# label.move(100, 60)
#
# window.show()
# sys.exit(app.exec())

# Код #2

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Окно через класс")
        self.resize(300, 150)

        label = QLabel("Это окно создано через класс", self)
        label.move(40, 60)

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()