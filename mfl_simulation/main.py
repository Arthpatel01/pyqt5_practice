import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QMenuBar, QAction
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon
import pyqtgraph as pg
import os
from style import MFLapp_Style, MenuBar_Style, StartSim_Btn_Style

current_dir = os.getcwd()


class MFLapp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        self.plot_widget = pg.PlotWidget()
        self.start_button = QPushButton("Start Simulation")
        self.timer = QTimer()

        self.position_start = 0
        self.position_end = 10

        self.data = {
            "position": np.linspace(self.position_start, self.position_end, 100),
            "sensor_data": np.zeros(100)
        }

        # initializing ui part
        self.init_ui()

        self.start_button.clicked.connect(self.start_simulation)

        self.timer.timeout.connect(self.update_plot)

        self.menu_bar = MenuBarApp(parent_window=self)
        self.setMenuBar(self.menu_bar)

    def init_ui(self):
        self.setStyleSheet(MFLapp_Style)

        self.start_button.setStyleSheet(StartSim_Btn_Style)

        self.setWindowTitle("MFL Data Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(self.layout)
        self.layout.addWidget(self.plot_widget)

        self.layout.addWidget(self.start_button)

    def start_simulation(self):
        self.timer.start(100)

    def update_plot(self):
        new_data = np.random.uniform(low=-0.5, high=0.5, size=len(self.data["sensor_data"]))
        self.data["sensor_data"] += new_data
        self.position_start, self.position_end = self.position_start + 10, self.position_end + 10
        self.data['position'] += np.linspace(self.position_start, self.position_end, 100)

        self.plot_widget.clear()
        self.plot_widget.plot(self.data["position"], self.data["sensor_data"], pen="g")


class MenuBarApp(QMenuBar):
    """
    This class is responsible for initializing Menus and it's actions and also slots.
    """
    def __init__(self, parent_window):
        super().__init__()
        # Parent window (MFLapp) instance, so we can do changes in that instance from here
        self.parent_window = parent_window

        # Set Style from style.py
        self.setStyleSheet(MenuBar_Style)

        # File Menu section
        home_icon_path = os.path.join(current_dir, 'icons\\home-color.png')
        self.file_menu = self.addMenu(QIcon(home_icon_path), "&Home")

        # New menu button section
        new_file_action = QAction("New File", self)
        self.file_menu.addAction(new_file_action)

        # Reset menu button section
        reset_action = QAction("&Reset", self)
        reset_action.triggered.connect(self.reset_action_slot)
        self.file_menu.addAction(reset_action)

        # Exit menu button section
        exit_action = QAction("&Exit", self)
        exit_action.triggered.connect(QApplication.instance().quit)
        self.file_menu.addAction(exit_action)

    def reset_action_slot(self):
        """
        -This function will trigger when someone click reset button form home menu.
        -This function firstly clear plot widget, then stop timer so no action occur,
         then reset data dictionary as it is in starting of program
        :return: None
        """
        self.parent_window.plot_widget.clear()
        self.parent_window.timer.stop()
        self.parent_window.position_start = 0
        self.parent_window.position_end = 10

        self.parent_window.data = {
            "position": np.linspace(self.parent_window.position_start, self.parent_window.position_end, 100),
            "sensor_data": np.zeros(100)
        }




def run_application():
    app = QApplication(sys.argv)

    window = MFLapp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    run_application()
