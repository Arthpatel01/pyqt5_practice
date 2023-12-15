from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys
import os


class MyWebApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.web_view = QWebEngineView()

        # self.load_my_portfolio()
        self.load_local_pages()

        self.setCentralWidget(self.web_view)

        self.setWindowTitle("My Web App")
    def load_my_portfolio(self):
        self.web_view.setUrl(QUrl("https://artheverywhere.pythonanywhere.com"))

    def load_local_pages(self):
        full_path = os.path.abspath("oxer-html/index.html")
        self.web_view.setUrl(QUrl.fromLocalFile(full_path))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWebApp()
    window.show()

    sys.exit(app.exec_())
