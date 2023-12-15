import sys
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class MainWindow(QMainWindow):
    message = pyqtSignal(str)
    multi_things = pyqtSignal(int, str, int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Signals")

        self.message.connect(self.custom_slot)
        self.multi_things.connect(self.custom_slot)

        self.message.emit("Test Message")
        self.multi_things.emit(2023, "<----Year ==== Month---->", 12)

    def custom_slot(self, *a):
        a = [1, 2, 3]
        print('-------Slot Called:')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
