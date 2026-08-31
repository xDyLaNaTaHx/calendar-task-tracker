import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from classes.main_window import MyWindow
from classes.calendar_event import CalendarView

app = QApplication(sys.argv)

window = MyWindow()
window.show()

# app = QApplication(sys.argv)
# view = CalendarView()
# view.show()

sys.exit(app.exec())