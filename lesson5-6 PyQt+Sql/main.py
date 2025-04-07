import sys
from PyQt6.QtWidgets import QApplication
import database
from ui import ContactApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContactApp(database)
    window.show()
    sys.exit(app.exec())