from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QCheckBox, QComboBox, \
    QListWidget, QLineEdit, QSpinBox
from PyQt5.QtCore import QSize, Qt
import sys
from random import choice

window_titles = [
    'My App',
    'My App',
    'Still My App',
    'Still My App',
    'What on earth',
    'What on earth',
    'This is surprising',
    'This is surprising',
    'Something went wrong'
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App 3")
        self.setMinimumSize(QSize(400, 300))
        self.setMaximumSize(QSize(600, 500))

        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.button_clicked)

        self.windowTitleChanged.connect(self.window_title_changed)

        self.setCentralWidget(self.button)

    def button_clicked(self):
        print("Clicked")
        new_title_window = choice(window_titles)
        print("Setting new window title:", new_title_window)
        self.setWindowTitle(new_title_window)

    def window_title_changed(self, title):
        print("Window title is changed: ", title)

        if title == "Something went wrong":
            print("Disabling the button!!")
            self.button.setEnabled(False)


class WidgetMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QWidget Window")
        self.setFixedSize(QSize(300, 200))

        self.button = QPushButton("QWidget Button")
        self.button.clicked.connect(self.btn1_action)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        self.setLayout(layout)

    def btn1_action(self):
        print("=======>> Widget button is clicked!!")


class LabelTutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel Example")
        # self.setMinimumSize(QSize(600, 300))

        self.label = QLabel()

        self.simple_label()
        self.image_label()

        # font = self.label1.font()
        # font.setPointSize(30)
        # self.label1.setFont(font)
        # self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(self.label)

    def simple_label(self):
        self.label.setText("Hello, How are you?")
        font = self.label.font()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

    def image_label(self):
        self.label.setPixmap(QPixmap("test_img.png"))
        self.label.setScaledContents(True)


class CheckBoxTutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkbox Tutorial")
        self.setMinimumSize(QSize(300, 200))
        self.check_box = QCheckBox("This is checkbox")
        self.check_box.clicked.connect(self.check_full_state)
        # self.check_box.setChecked(True)
        self.check_box.setCheckState(1)
        # self.check_box.setCheckable(False)
        self.setCentralWidget(self.check_box)

    def show_state(self, state):
        print('State: ', state)

    def check_full_state(self):
        check_state = self.check_box.checkState()
        if check_state == 0:
            print('====> Not Checked')
        elif check_state == 1:
            print("====> Partially Checked")
        elif check_state == 2:
            print("====> Checked")
        else:
            print("Check State is out of range:", check_state)


class ComboTutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Combo Box(Select) Example")

        self.select_input = QComboBox()
        self.select_input.setInsertPolicy(QComboBox.InsertAlphabetically)
        self.select_input.addItems(["Vadodara", "Surat", "Lunawada", "Gandhinagar", "Abu"])
        self.select_input.addItem("Junagadh")

        self.select_input.currentIndexChanged.connect(self.index_changed)
        self.select_input.currentTextChanged.connect(self.text_changed)

        # self.select_input.setMaxCount(2)
        self.select_input.setEditable(True)

        self.multiple_select = QListWidget()
        self.multiple_select.addItems(["Iron Man", "Thor", "Super Man", "Bat Man", "Spider Man"])
        self.multiple_select.MultiSelection


        self.setCentralWidget(self.select_input)

    def index_changed(self, i):
        print("Index Changed:", i)

    def text_changed(self, t):
        print("Text(value) is changed:", t)
        # print('-=-==-=-==->>', self.select_input.currentText())
        # print('-=-==-=-==->>', self.select_input.currentIndex())

class LineEditTutorial(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Line Edit (One Line Input)")

        self.line_input = QLineEdit("test text 123")
        self.line_input.setMaxLength(10)
        self.line_input.setPlaceholderText("Please enter text here")
        # self.line_input.setReadOnly(True)

        self.line_input.returnPressed.connect(self.return_pressed)
        self.line_input.selectionChanged.connect(self.selection_changed)

        self.line_input.textChanged.connect(self.text_changed)
        self.line_input.textEdited.connect(self.text_edited)

        #setInputMask for pre defined structure
        # self.line_input.setInputMask("+00 00000 00000")

        # print("Changing text...")
        # self.line_input.setText("Yooo")

        self.setCentralWidget(self.line_input)

    def return_pressed(self):
        print("Enter Key Pressed!!")

    def selection_changed(self):
        print("Selection Changed!!")

    def text_changed(self, s):
        print("Text Changed: ", s)

    def text_edited(self, s):
        print("Text Edited: ", s)

class SpinBoxTutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spin Box Example")

        self.spin_box = QSpinBox()
        self.spin_box.setMinimum(-10)
        self.spin_box.setMaximum(125)

        self.spin_box.setPrefix("INR")
        # self.spin_box.setSuffix("KM")
        self.spin_box.setSingleStep(3)
        self.setCentralWidget(self.spin_box)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SpinBoxTutorial()
    window.show()

    sys.exit(app.exec_())
