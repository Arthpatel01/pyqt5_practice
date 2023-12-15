import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, \
    QLabel, QToolBar, QAction, QStatusBar, QRadioButton, QButtonGroup, QCheckBox, QDialog, QDialogButtonBox, \
    QMessageBox, QGridLayout
from PyQt5.QtGui import QColor, QPalette, QIcon, QKeySequence
from PyQt5.QtCore import QSize


class Toolbar_Tutorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Toolbar Tutorial")

        page_layout = QVBoxLayout()
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()

        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        row1_layout.addWidget(name_label)
        row1_layout.addWidget(self.name_input)

        page_layout.addLayout(row1_layout)

        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter your email address")
        row2_layout.addWidget(email_label)
        row2_layout.addWidget(self.email_input)

        page_layout.addLayout(row2_layout)

        button = QPushButton("Submit")
        button.clicked.connect(self.submit_action)
        page_layout.addWidget(button)

        self.output_label = QLabel()
        page_layout.addWidget(self.output_label)

        widget = QWidget()
        widget.setLayout(page_layout)

        # ---------------------------Toolbar Section--------------------------->>

        tool_bar = QToolBar("My Toolbar")
        # tool_bar.setIconSize(QSize(16, 16))
        self.addToolBar(tool_bar)

        # button_action = QAction("Your Button", self)
        button_action = QAction(QIcon("static/images/icons/home-color.png"), "Home", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolbarButtonClick)
        button_action.setCheckable(True)
        tool_bar.addAction(button_action)

        about_btn = QAction(QIcon("static/images/icons/about-color.png"), "About", self)
        about_btn.setStatusTip("This is about app")
        # about_btn.triggred.connect()
        tool_bar.addAction(about_btn)

        # ---------------------------Toolbar Section End ---------------------->>

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("skyblue"))
        self.setPalette(palette)

        status_bar = QStatusBar(self)
        self.setStatusBar(status_bar)

        self.setMaximumSize(300, 400)
        self.setCentralWidget(widget)

    def submit_action(self):
        name = self.name_input.text()
        email = self.email_input.text()

        output = f"Name: {name} \nEmail: {email}"
        self.output_label.setText(output)

        self.name_input.setText("")
        self.email_input.setText("")

    def onMyToolbarButtonClick(self, s):
        print("====>", s)


class Temp_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.prev_data = {
            "name": "",
            "phone": "",
            "gender": ""
        }

        self.setWindowTitle("Temporary Window")

        page_layout = QVBoxLayout()
        row1_layout = QHBoxLayout()
        row2_layout = QHBoxLayout()
        row3_layout = QHBoxLayout()

        page_layout.addLayout(row1_layout)
        page_layout.addLayout(row2_layout)
        page_layout.addLayout(row3_layout)

        name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter your name")
        row1_layout.addWidget(name_label)
        row1_layout.addWidget(self.name_input)

        phone_label = QLabel("Phone:")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter your phone number")
        row2_layout.addWidget(phone_label)
        row2_layout.addWidget(self.phone_input)

        gender_label = QLabel("Gender:")

        self.gender_input = QRadioButton("male")
        self.gender_input2 = QRadioButton("female")
        self.gender_btn_group = QButtonGroup()
        self.gender_btn_group.addButton(self.gender_input)
        self.gender_btn_group.addButton(self.gender_input2)
        row3_layout.addWidget(gender_label)
        row3_layout.addWidget(self.gender_input)
        row3_layout.addWidget(self.gender_input2)
        # self.gender_btn_group.buttonClicked.connect(self.get_output)

        submit_btn = QPushButton("Submit")
        submit_btn.setStatusTip("Submit your data")
        page_layout.addWidget(submit_btn)
        submit_btn.clicked.connect(self.get_output)

        clear_btn = QPushButton("Clear")
        clear_btn.setStatusTip("Clear the form")
        clear_btn.clicked.connect(self.clear_form_action)
        page_layout.addWidget(clear_btn)

        self.output_label = QLabel()
        page_layout.addWidget(self.output_label)

        widget = QWidget()
        widget.setLayout(page_layout)

        self.initialize_tool_bar()
        self.initialize_menu()

        self.setStatusBar(QStatusBar(self))

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("yellow"))
        self.setPalette(palette)


        self.setCentralWidget(widget)

    def initialize_tool_bar(self):
        toolbar = QToolBar("My Tool Bar")
        self.addToolBar(toolbar)

        home_btn = QAction(QIcon("static/images/icons/home-color.png"), "Home", self)
        home_btn.setStatusTip("This is your home button")
        home_btn.triggered.connect(self.home_button_click)
        home_btn.setCheckable(True)
        toolbar.addAction(home_btn)

        about_btn = QAction(QIcon("static/images/icons/about-color.png"), "About", self)
        about_btn.setStatusTip("Get information about us")
        about_btn.triggered.connect(self.about_us_event)
        toolbar.addAction(about_btn)

        call_book = QAction(QIcon("static/images/icons/address-book.png"), "Contacts", self)
        call_book.setStatusTip("Contact list to contact with our experts")
        call_book.triggered.connect(self.address_book_event)
        toolbar.addAction(call_book)

        save_cbk = QCheckBox("Save")
        save_cbk.setChecked(True)
        toolbar.addWidget(save_cbk)

    def initialize_menu(self):
        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        fileNew_btn = QAction(QIcon("static/images/icons/file-new.png"), "New...", self)
        file_menu.addAction(fileNew_btn)

        fileSave_btn = QAction(QIcon("static/images/icons/file-save.png"), "Save", self)
        fileSave_btn.triggered.connect(self.file_menu_save_action)
        fileSave_btn.setShortcut(QKeySequence("Ctrl+s"))
        file_menu.addAction(fileSave_btn)

        fileSaveAs_btn = QAction(QIcon("static/images/icons/file-save-as.png"), "Save As...", self)
        file_menu.addAction(fileSaveAs_btn)

        sub_file_menu = file_menu.addMenu("Sub Menu")
        option1 = QAction("Option1..", self)
        option2 = QAction("Option2..", self)
        sub_file_menu.addActions([option1, option2])

        data_menu = menu_bar.addMenu("Data")

        previous_data_btn = QAction("My Previous Data", self)
        previous_data_btn.triggered.connect(self.get_previous_data)
        data_menu.addAction(previous_data_btn)

    def home_button_click(self, s):
        print("Home Button is clicked:", s)

    def get_output(self):
        name = self.name_input.text()
        phone = self.phone_input.text()
        gender = self.gender_btn_group.checkedButton().text()

        output = f"Name: {name}\nPhone: {phone}\nGender: {gender}"
        self.output_label.setText(output)

        self.prev_data['name'] = name
        self.prev_data['phone'] = phone
        self.prev_data['gender'] = gender

    def file_menu_save_action(self):
        print("File Saved Successfully!!")

    def get_previous_data(self):
        # prev_data_dialog = QDialog()
        # dialog_layout = QVBoxLayout(prev_data_dialog)
        # output_label = QLabel()
        # output = f"Name: {self.prev_data['name']}\nPhone: {self.prev_data['phone']}\nGender: {self.prev_data['gender']}"
        # output_label.setText(output)
        #
        # dialog_box_btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        # dialog_box_btns.accepted.connect(prev_data_dialog.accept)
        # dialog_box_btns.rejected.connect(prev_data_dialog.reject)
        #
        # dialog_layout.addWidget(output_label)
        # dialog_layout.addWidget(dialog_box_btns)
        # prev_data_dialog.exec_()

        output = f"Name: {self.prev_data['name']}\nPhone: {self.prev_data['phone']}\nGender: {self.prev_data['gender']}"
        prev_data_dialog = CustomDialog(output=output)
        # prev_data_dialog.exec_()
        if prev_data_dialog.exec_():
            print("Success!")
        else:
            print("Cancel!")

    def clear_form_action(self):
        self.name_input.setText("")
        self.phone_input.setText("")
        self.gender_input.setChecked(False)
        self.gender_input2.setChecked(False)

    def about_us_event(self):
        msg = "Hello, My name is Arth Patel. I have developed this application with PyQt5 package in python."
        message_box = CustomMessageBox(msg=msg, title="About Us")
        message_box.exec_()

    def something_went_wrong_box(self):
        buttons = QMessageBox.Discard | QMessageBox.Ignore | QMessageBox.NoToAll
        box = QMessageBox.critical(self, "Opps!", "Something went wrong!!", buttons=buttons)
        if box == QMessageBox.Ignore:
            print("Ignore!")
        else:
            print("No!")

    def address_book_event(self):
        self.address_book_win = QWidget()
        dict = {
            "Rahul Sing (Support)": 9685475896,
            "Vijay Malya (Owner)": 6985008023,
            "Rajesh Agrawal (Manager)": 9958742093,
            "Chandravir Solanki (Assistant)": 7855480985,
        }
        layout = QGridLayout()
        layout.addWidget(QLabel("Name"), 0, 0)
        layout.addWidget(QLabel("Contact No"), 0, 1)
        for i, key in enumerate(dict):
            layout.addWidget(QLabel(str(key)), i + 1, 0)

            number_label = QLabel(str(dict[key]))
            palette = self.palette()
            palette.setColor(QPalette.WindowText, QColor("blue"))
            number_label.setPalette(palette)
            layout.addWidget(number_label, i + 1, 1)

        self.address_book_win.setLayout(layout)
        self.address_book_win.show()


class CustomDialog(QDialog):
    def __init__(self, output="", title=""):
        super().__init__()
        self.setWindowTitle("Pop Up Box")
        layout = QVBoxLayout(self)
        output_label = QLabel()
        output_label.setText(output)
        layout.addWidget(output_label)

        btns = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        layout.addWidget(btns)


class CustomMessageBox(QMessageBox):
    def __init__(self, msg="", title=""):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(msg)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("skyblue"))
        self.setPalette(palette)

        self.setIcon(QMessageBox.Information)

class CustomMouseEvent(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Examples")
        label = QLabel("Mouse Events")
        self.setCentralWidget(label)

    def mouseDoubleClickEvent(self, e):
        print("======Mouse Clicked:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = CustomMouseEvent()
    window.show()

    sys.exit(app.exec())
