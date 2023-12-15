from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import sys


def btn_action1(x, y):
    print(x, "==============", y)


app = QApplication(sys.argv)

window = QWidget()
button = QPushButton(window)
button.setText("Press Me!!")
button.clicked.connect(lambda: btn_action1(2, 3))
window.show()

sys.exit(app.exec_())
