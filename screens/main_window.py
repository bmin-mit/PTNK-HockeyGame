import pygame
from pygame import Color

from screens.instruction import Instruction
from utils import fonts
from sprites.button import Button

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MainWindow:
    __screen: pygame.Surface
    __is_running: bool

    def __init__(self):
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.__button1 = Button(self.__screen, SCREEN_WIDTH // 2, 275, "Start")
        self.__button2 = Button(self.__screen, SCREEN_WIDTH // 2, 350, "Instruction")
        self.__button3 = Button(self.__screen, SCREEN_WIDTH // 2, 425, "Recent Score")

        self.__main_loop()

    def __draw(self):
        self.__screen.fill(Color('antiquewhite'))

        title_text = fonts.TITLE_TEXT_STYLE.render("Hockeyyy!!!!!",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 150))

        self.__button1.draw()
        self.__button2.draw()
        self.__button3.draw()

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__button1.collidepoint(pygame.mouse.get_pos()):
                from screens.ingame import InGame
                InGame(self.__screen)
            elif self.__button2.collidepoint(pygame.mouse.get_pos()):
                Instruction(self.__screen)
            elif self.__button3.collidepoint(pygame.mouse.get_pos()):
                from screens.recent_score import RecentScore
                RecentScore(self.__screen)
