import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton, QCheckBox, QComboBox, QLabel, QLineEdit,
                             QPlainTextEdit, QSpinBox, QVBoxLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QT Style Sheet Tutorial")

        self.container = QWidget()
        self.setCentralWidget(self.container)

        self.page_layout = QVBoxLayout()
        self.container.setLayout(self.page_layout)

        self.editor = QPlainTextEdit()
        # self.editor.textChanged.connect(self.update_styles)
        self.page_layout.addWidget(self.editor)

        apply_btn = QPushButton("Apply Style")
        apply_btn.clicked.connect(self.update_styles)
        self.page_layout.addWidget(apply_btn)

        cb = QCheckBox("Checkbox")
        self.page_layout.addWidget(cb)

        combo = QComboBox()
        combo.setObjectName("thecombo")
        combo.addItems(["First", "Second", "Third", "Fourth"])
        self.page_layout.addWidget(combo)

        sb = QSpinBox()
        sb.setRange(0, 99999)
        self.page_layout.addWidget(sb)

        l = QLabel("This is a label")
        self.page_layout.addWidget(l)

        le = QLineEdit()
        le.setObjectName("myLineEdit")
        self.page_layout.addWidget(le)

        pb = QPushButton("Push Me!")
        self.page_layout.addWidget(pb)

    def update_styles(self):
        style_sheet = self.editor.toPlainText()
        self.setStyleSheet(style_sheet)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
