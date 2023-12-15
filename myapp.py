from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys

app = QApplication(sys.argv)

window = QMainWindow()
window.show()

sys.exit(app.exec_())