import pygame
import sys


class Base(object):

    def __init__(self, screenSize=(512, 512)):
        # initialize all pygame modules
        pygame.init()

        # indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL

        # initialize buffer to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)

        # use core opengl profile for cross-platform compatibility
        pygame.display.gl_set_attribute(pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE)

        # crate and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)

        # set the text that appears in title bar of the window
        pygame.display.set_caption("Graphics Window")

        # determine if main loop is active
        self.running = True
        # manage time-related data and operations
        self.clock = pygame.time.Clock()


    # implement by extending class
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        self.initialize()

        while self.running:
            self.update()

            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()
        sys.exit()
