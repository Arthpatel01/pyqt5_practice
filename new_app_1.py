import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QWidget, QLabel, \
    QApplication, QStatusBar, QMenuBar, QAction, QFileDialog
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_template import FigureCanvas


class CustomButton(QPushButton):
    def __init__(self, btn_type="Normal", text="Button"):
        super().__init__(text=text)
        # self.setText(text)
        self.clicked.connect(self.action_1)

    def action_1(self):
        print("Custom Button Clicked!!")


class PlottedGraph(FigureCanvas):
    def __init__(self, file, header=None):
        super().__init__()
        self.file = file
        self.header = header

        self.x_data = []
        self.y_data = []

        if self.file:
            self.initDataFrame()
            self.plot_graph()
        else:
            print("No file is selected!!")

    def initDataFrame(self):
        self.df = pd.read_csv(self.file, header=self.header)
        self.x_data = self.df[0].values
        self.y_data = self.df[1].values

    def plot_graph(self):
        self.fig, self.ax = plt.subplots()
        self.ax.scatter(x=self.x_data, y=self.y_data)
        self.ax.set_xlabel("X Label")
        self.ax.set_ylabel("Y Label")
        self.ax.legend()

        self.draw()



class CustomFileDialog(QFileDialog):
    def __init__(self, page_layout):
        super().__init__()
        self.setFileMode(QFileDialog.AnyFile)

        if self.exec_():
            file = self.selectedFiles()[0]
            plot_graph = PlottedGraph(file=file)
            page_layout.addWidget(plot_graph)

            print('================>>>>>')

    def test(self):
        print("-------123")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Desktop App 1")
        self.setStatusBar(QStatusBar())

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        page_layout = QVBoxLayout()
        central_widget.setLayout(page_layout)

        row_1_layout = QHBoxLayout()
        page_layout.addLayout(row_1_layout)

        self.f_name_input = QLineEdit()
        self.f_name_input.setPlaceholderText("Enter Your First Name")
        row_1_layout.addWidget(self.f_name_input)

        self.l_name_input = QLineEdit()
        self.l_name_input.setPlaceholderText("Enter Your Last Name")
        row_1_layout.addWidget(self.l_name_input)

        button1 = QPushButton("Submit")
        button1.clicked.connect(self.submit_action)
        button1.setStatusTip("Submit button to see output of filled form.")
        row_1_layout.addWidget(button1)

        self.output_label = QLabel()
        page_layout.addWidget(self.output_label)

        clear_btn = CustomButton(text="Clear")
        page_layout.addWidget(clear_btn)

        file_input = CustomFileDialog(page_layout=page_layout)
        page_layout.addWidget(file_input)

        self.init_menu()

    def submit_action(self):
        output = f"First Name: {self.f_name_input.text()}\n\nLast Name: {self.l_name_input.text()}"
        self.output_label.setText(output)

    def init_menu(self):
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)
        menu_1 = menu_bar.addMenu("Tools")

        menu_action_1 = QAction("Clear Output", self)
        menu_action_1.triggered.connect(self.menu_action)
        menu_1.addAction(menu_action_1)

    def menu_action(self):
        self.output_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
