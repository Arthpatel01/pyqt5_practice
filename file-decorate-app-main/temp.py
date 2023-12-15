from PyQt5.QtWidgets import QPushButton, QApplication, QRadioButton
import sys


app = QApplication(sys.argv)
window = QRadioButton("Radio Btn")
window.show()
sys.exit(app.exec_())
