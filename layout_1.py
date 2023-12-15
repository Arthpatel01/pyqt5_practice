import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout, QLabel, \
    QLineEdit, QGridLayout, QStackedLayout, QTabWidget
from basic_layouts.layout_colorwidget import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Layout 1")

        widget = Color("red")

        self.setCentralWidget(widget)


class QVBoxLayout_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vertical Layout")

        layout = QVBoxLayout()
        layout.addWidget(Color("red"))
        layout.addWidget(Color("Yellow"))
        layout.addWidget(Color("green"))

        button = QPushButton("Push Me!!")
        layout.addWidget(button)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)


class QHBoxLayout_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Horizontal Layout")

        layout = QHBoxLayout()
        label = QLabel("Name:")
        self.line_input = QLineEdit()
        self.line_input.setPlaceholderText("Enter Your Name")
        self.button = QPushButton("Submit")

        layout.addWidget(label)
        layout.addWidget(self.line_input)
        layout.addWidget(self.button)

        self.button.clicked.connect(self.submit_action)
        self.line_input.returnPressed.connect(self.submit_action)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    def submit_action(self):
        val = self.line_input.text()
        if val:
            print("Name:", val)
        else:
            pass


class Nesting_Layout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nested Layout Example")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(20)

        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))

        layout1.addLayout(layout2)

        layout1.addWidget(Color("green"))

        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))

        layout1.addLayout(layout3)

        widget = QWidget()
        widget.setLayout(layout1)

        self.setCentralWidget(widget)


class Grid_Layout_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layout Example")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        dummy_widget = QWidget()
        dummy_widget.setLayout(layout)

        self.setCentralWidget(dummy_widget)


class Stack_Layout_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stacked Layout Example")

        page_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stack_layout = QStackedLayout()

        page_layout.addLayout(button_layout)
        page_layout.addLayout(self.stack_layout)

        btn = QPushButton("Red")
        btn.clicked.connect(self.activate_tab1)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("red"))

        btn = QPushButton("Green")
        btn.clicked.connect(self.activate_tab2)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("green"))

        btn = QPushButton("Yellow")
        btn.clicked.connect(self.activate_tab3)
        button_layout.addWidget(btn)
        self.stack_layout.addWidget(Color("yellow"))

        widget = QWidget()
        widget.setLayout(page_layout)

        self.setCentralWidget(widget)

    def activate_tab1(self):
        self.stack_layout.setCurrentIndex(0)

    def activate_tab2(self):
        self.stack_layout.setCurrentIndex(1)

    def activate_tab3(self):
        self.stack_layout.setCurrentIndex(2)

class Tab_Widget_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tab Widget Example")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        for n, color in enumerate(["red", "green", "yellow", "blue"]):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = Tab_Widget_Tutorial()
    window.show()

    sys.exit(app.exec_())
