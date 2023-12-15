import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QListWidget, QCheckBox, QListWidgetItem

class ToDoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.initStyle()

    def initUI(self):
        self.setWindowTitle("My To DO App")
        self.setGeometry(100, 100, 600, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        input_layout = QHBoxLayout()
        self.task_input = QLineEdit()
        add_button = QPushButton("Add Task")
        add_button.clicked.connect(self.add_task)

        input_layout.addWidget(self.task_input)
        input_layout.addWidget(add_button)

        self.task_list = QListWidget()

        layout.addLayout(input_layout)
        layout.addWidget(self.task_list)

        central_widget.setLayout(layout)
    def initStyle(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            
            QWidget {
                background-color: #ffffff;
                border: 1px solid #d0d0d0;
            }
            
            QLineEdit {
                border: 1px solid #a0a0a0;
                padding: 5px;
                font-size: 14px;
            }
            
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 12px;
                margin-left: 5px;
                font-size: 14px;
                cursor: pointer;
            }
            
            QPushButton:hover {
                background-color: 45a049;
            }
            
            QListWidget {
                background-color: #ffffff;
                border-top: 1px solid #d0d0d0;
                border-bottom: 1px solid #d0d0d0;
            }
            
            QCheckBox {
                font-size: 14px;
            }
        """)

    def add_task(self):
        task_text = self.task_input.text()
        if task_text:
            task_item = QListWidgetItem()
            task_ckeckbox = QCheckBox(task_text)
            self.task_list.addItem(task_item)
            self.task_list.setItemWidget(task_item, task_ckeckbox)
            self.task_input.clear()

#


if __name__ == "__main__":
    app = QApplication(sys.argv)
    todo_app = ToDoApp()
    todo_app.show()
    sys.exit(app.exec_())