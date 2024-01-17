import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *

# Global variables to store the arm positions
arm_positions = [2.0, 0.0, 7.0]


def draw_axes():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)  # Red x-axis
    glVertex3f(0, 0, 0)
    glVertex3f(1, 0, 0)

    glColor3f(0, 1, 0)  # Green y-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 1, 0)

    glColor3f(0, 0, 1)  # Blue z-axis
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, 1)
    glEnd()


def draw_live_graph():
    glBegin(GL_LINE_STRIP)
    glColor3f(1, 1, 1)  # White line
    for i, pos in enumerate(arm_positions):
        glVertex3f(i, pos, 0)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_axes()
    draw_live_graph()

    glutSwapBuffers()


def key_callback(key, x, y):
    global arm_positions
    if key == b'1':
        arm_positions[0] += 0.1
    elif key == b'2':
        arm_positions[1] += 0.1
    elif key == b'3':
        arm_positions[2] += 0.1


def main():
    glutInit(sys.argv)
    display_size = (800, 600)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutCreateWindow(b"Live Stream")

    gluPerspective(45, (display_size[0] / display_size[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    glutKeyboardFunc(key_callback)
    glutDisplayFunc(display)

    glEnable(GL_DEPTH_TEST)

    while True:
        glutMainLoopEvent()

        display()
        glutSwapBuffers()
        pygame.time.wait(10)


if __name__ == "__main__":
    main()
