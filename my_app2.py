from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import QSize
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.is_button_checked = True
        self.setWindowTitle("My Main Window")

        self.button = QPushButton("Push Me")
        # button.setFixedSize(QSize(100, 40))

        # self.button.setCheckable(True)
        self.button.clicked.connect(self.button_clicked)
        # self.button.setChecked(self.is_button_checked)

        self.setCentralWidget(self.button)

        # self.setFixedSize(QSize(400, 300))
        self.setMinimumSize(QSize(200, 100))
        self.setMaximumSize(QSize(500, 400))

    def button_clicked(self):
        print('===========>>Clicked')
        self.button.setText("Thank You for Click!!")
        self.button.setEnabled(False)

        self.setWindowTitle("One Shot App")

        # self.is_button_checked = self.button.isChecked()
        # print(self.is_button_checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
