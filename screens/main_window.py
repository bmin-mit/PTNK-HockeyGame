import pygame
from pygame import Color

from screens.instruction import Instruction
from utils import fonts

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MainWindow:
    __screen: pygame.Surface
    __is_running: bool

    def __init__(self):
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__draw()

        self.__main_loop()

    def __draw(self):
        self.__screen.fill(Color('antiquewhite'))

        title_text = fonts.TITLE_TEXT_STYLE.render("Hockeyyy!!!!!",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

        continue_text = fonts.BODY_TEXT_STYLE.render("Press SPACE to continue",
                                                     True, Color('antiquewhite3'))
        self.__screen.blit(continue_text,
                           (SCREEN_WIDTH // 2 - continue_text.get_width() // 2, SCREEN_HEIGHT // 2))

        pygame.display.flip()

    def __main_loop(self):
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                self.__handle_event(event)
            
            self.__draw()
            pygame.display.flip()

    def __handle_event(self, event):
        keys = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT:
            self.__is_running = False

        if event.type == pygame.KEYDOWN:
            if keys[pygame.K_SPACE]:
                Instruction(self.__screen)
                from screens.ingame import InGame
                InGame(self.__screen)
