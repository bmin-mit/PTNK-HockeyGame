import pygame
from pygame import Color
from utils import fonts
from utils.score import read_data
import json


class RecentScore:
    __is_running: bool

    def __init__(self, screen):
        from screens.main_window import SCREEN_WIDTH, SCREEN_HEIGHT
        self.__screen = screen

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.__main_loop()

    def draw(self):
        self.__screen.fill(Color('antiquewhite'))
        title_text = fonts.TITLE_TEXT_STYLE.render("Recent Score",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        score_data = read_data()
        for idx, line in enumerate(score_data):
            score_text = fonts.BODY_TEXT_STYLE.render(" - ".join(line), True, Color('antiquewhite4'))
            self.__screen.blit(score_text, (self.SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200 + idx * 40))

        continue_text = fonts.BODY_TEXT_STYLE.render("Click mouse to continue",
                                                     True, Color('antiquewhite3'))
        self.__screen.blit(continue_text,
                           (self.SCREEN_WIDTH // 2 - continue_text.get_width() // 2, self.SCREEN_HEIGHT - 150))

        pygame.display.flip()

    def __main_loop(self):
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                if self.__handle_event(event):
                    self.__is_running = False
            self.draw()

            pygame.display.flip()

    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.__is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False
