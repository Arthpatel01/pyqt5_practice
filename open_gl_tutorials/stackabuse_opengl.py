import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class DrawCube:
    def __init__(self):
        self.vertices = (
            (-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1))
        self.edges = (
            (0, 1), (1, 2), (2, 3), (0, 3), (4, 5), (5, 6), (6, 7), (4, 7), (0, 4), (1, 5), (2, 6), (3, 7)
        )

    def init_window(self):
        pg.init()
        windowSize = (1080, 540)
        pg.display.set_mode(size=windowSize, flags=DOUBLEBUF | OPENGL)

        gluPerspective(45, (windowSize[0]/windowSize[1]), 0.1, 50.0)
        glTranslatef(0.0, 0.0, -5)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            self.wire_cube()
            pg.display.flip()
            pg.time.wait(10)

    def wire_cube(self):
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()


if __name__ == "__main__":
    draw_cube = DrawCube()
    draw_cube.init_window()
