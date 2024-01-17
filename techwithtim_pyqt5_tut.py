from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QVBoxLayout, QLabel
import sys
from PyQt5.QtGui import QColor, QPalette


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Title 123")
        self.setGeometry(200, 200, 300, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        label = QLabel("This is my label")

        label_palette = label.palette()
        label_palette.setColor(QPalette.Window, QColor("green"))
        label.setPalette(label_palette)

        # label.move(50, 50)
        layout.addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
