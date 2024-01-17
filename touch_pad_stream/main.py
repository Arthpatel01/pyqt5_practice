import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
import pyqtgraph as pg
from pynput import mouse

class MouseGraph(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.data_buffer = {'x': [], 'y': []}

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(100)

        self.mouse_listener = mouse.Listener(on_move=self.on_mouse_move)
        self.mouse_listener.start()

    def init_ui(self):
        self.setWindowTitle("Live Mouse Graph")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.plot_widget = pg.PlotWidget()
        self.plot = self.plot_widget.plot(pen="b")
        layout.addWidget(self.plot_widget)

    def on_mouse_move(self, x, y):
        self.data_buffer['x'].append(x)
        self.data_buffer['y'].append(y)

    def update_graph(self):
        # Update the graph with the last 100 data points
        self.plot.setData(self.data_buffer['x'][-100:], self.data_buffer['y'][-100:])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MouseGraph()
    main_window.show()

    sys.exit(app.exec_())