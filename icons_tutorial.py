from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QCheckBox
from PyQt5.Qt import QStyle
from PyQt5.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Inbuilt Icon Examples")
        self.setGeometry(100, 100, 300, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.page_layout = QVBoxLayout()
        central_widget.setLayout(self.page_layout)

        self.add_icon_btn()
        self.add_icon_btn(icon_object=QStyle.SP_ArrowBack)
        self.add_icon_btn(QStyle.SP_ArrowDown)
        self.add_icon_btn(QStyle.SP_ArrowLeft)
        self.add_icon_btn(QStyle.SP_ArrowRight)
        self.add_icon_btn(QStyle.SP_ArrowForward)
        self.add_icon_btn(QStyle.SP_DirOpenIcon)
        self.add_icon_btn(QStyle.SP_MediaStop)
        self.add_icon_btn(QStyle.SP_MediaPlay)
        self.add_icon_btn(QStyle.SP_ComputerIcon)

        check_btn = QCheckBox()
        style = check_btn.style()
        icon = style.standardIcon(QStyle.SP_FileIcon)
        check_btn.setIcon(icon)
        check_btn.setText("Including File")
        self.page_layout.addWidget(check_btn)

        custom_icon = QIcon("static/images/icons/home-color.png")
        custom_icon_btn = QPushButton()
        custom_icon_btn.setIcon(custom_icon)
        self.page_layout.addWidget(custom_icon_btn)

    def add_icon_btn(self, icon_object=QStyle.SP_ArrowUp):
        button = QPushButton()
        style = button.style()
        icon = style.standardIcon(icon_object)
        button.setIcon(icon)

        self.page_layout.addWidget(button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())