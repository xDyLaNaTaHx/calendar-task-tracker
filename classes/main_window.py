from PyQt6.QtWidgets import (
    QWidget, 
    QVBoxLayout, 
    QLabel, 
    QLineEdit, 
    QPushButton, 
    QComboBox,
)

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calendar app")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        # Box to enter goals
        self.enter_goal_label = QLabel("Enter a goal:")
        self.input_box = QLineEdit()
        self.enter_goal_button = QPushButton("Enter")

        # Goal entry callback
        self.current_goals = list() #(eventually read from file)
        self.enter_goal_button.clicked.connect(self.enter_goal_callback)

        # Goal dropdown
        self.goal_dropdown = QComboBox()

        # Remove goal button
        self.remove_goal_button = QPushButton("Remove button")
        self.remove_goal_button.clicked.connect(self.remover_goal_callback)


        # Habit entry

        # Add widgets
        layout.addWidget(self.enter_goal_label)
        layout.addWidget(self.input_box)
        layout.addWidget(self.enter_goal_button)
        layout.addWidget(self.goal_dropdown)
        layout.addWidget(self.remove_goal_button)

        self.setLayout(layout)

    def enter_goal_callback(self):
        goal = self.input_box.text().strip()

        if goal:
            self.current_goals.append(goal)
            self.goal_dropdown.addItem(goal)   # add to combo box
            self.input_box.clear()             # optional: clear input after adding
            self.enter_goal_label.setText("Enter a goal:")
        else:
            self.enter_goal_label.setText("Please enter your goal.")

    def remover_goal_callback(self):
        current_index = self.goal_dropdown.currentIndex()
        if current_index != -1:  # Ensure the combobox isn't empty
            self.goal_dropdown.removeItem(current_index)
            self.current_goals.pop(current_index)