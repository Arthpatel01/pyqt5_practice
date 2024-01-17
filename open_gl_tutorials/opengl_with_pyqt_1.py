import sys

from OpenGL.raw.GLU import gluPerspective
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QOpenGLWidget
from PyQt5.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLUT import *


class OpenGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.rotation_angle = 0

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glutInit(sys.argv)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0, 0, -6)
        glRotatef(self.rotation_angle, 1, 1, 0)

        glutWireCube(2)

        self.rotation_angle += 1
        self.rotation_angle %= 360


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.opengl_widget = OpenGLWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        layout.addWidget(self.opengl_widget)

        timer = QTimer(self)
        timer.timeout.connect(self.opengl_widget.update)
        timer.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
