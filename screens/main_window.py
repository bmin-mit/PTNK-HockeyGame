import pygame
from pygame import Color

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


class MainWindow:
    __window: pygame.Surface
    __clock: pygame.time.Clock
    __is_running: bool

    def __init__(self):
        pygame.init()
        self.__window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__clock = pygame.time.Clock()
        self.__draw()

        self.__main_loop()

        pygame.quit()

    def __draw(self):
        self.__window.fill(Color('white'))

        pygame.display.flip()

    def __main_loop(self):
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__is_running = False

            self.__clock.tick(FPS)
