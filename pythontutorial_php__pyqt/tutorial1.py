from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QAction
from PyQt5.QtGui import QIcon
import sys


class MainWindow(QMainWindow):
    """
    In This example we are going to explore methods and properties
    of QMainWindow in detail
    """

    def __init__(self):
        super().__init__()

        # A QMainWindow has one and only one central widget
        self.setCentralWidget(QLineEdit())

        # To set the title for the main window
        self.setWindowTitle("This is my title")

        # To set icon for the window
        # first create a QIcon and pass in the path of image
        # then pass that QIcon object in setWindowIcon method
        self.setWindowIcon(QIcon("../test_img.png"))

        # set geometry for the window (x, y, width, height)
        self.setGeometry(200, 200, 500,
                         200)  # in this example window will appeared at (200, 200) with 500px-width and 200px-height


        # To add Menu Bar
        menu_bar = self.menuBar()

        # Add menu to menu bar
        file_menu = menu_bar.addMenu("&File")
        edit_menu = menu_bar.addMenu("&Edit")
        help_menu = menu_bar.addMenu("&Help")

        # To add menu items to a menu, you need to create Actions
        # Method 1:
        file_menu.addAction("New", self.menu_action)

        # Method 2:
        open_action_item = QAction("Open", self)
        open_action_item.triggered.connect(self.menu_action)
        file_menu.addAction(open_action_item)

        # other Actions
        file_menu.addAction("Exit", self.destroy)

        # more Actions
        copy_action = QAction("Copy", self)
        copy_action.triggered.connect(self.copy_action_trigger)
        copy_action.setShortcut("Ctrl+Z")
        file_menu.addAction(copy_action)

    def menu_action(self):
        print('=============>>Menu item clicked')

    def copy_action_trigger(self):
        print("Item Copied!!")



if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
