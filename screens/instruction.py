import pygame
from pygame import Color
from utils import fonts


class Instruction:
    __is_running: bool

    def __init__(self, screen):
        from screens.main_window import SCREEN_WIDTH, SCREEN_HEIGHT
        self.__screen = screen

        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.count = 1
        self.max_count = 3

        self.__main_loop()

    def draw1(self):
        self.__screen.fill(Color('antiquewhite'))
        title_text = fonts.INSTRUCTION_TEXT_STYLE.render("Point your index finger UP, DOWN",
                                                         True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 100))
        title_text = fonts.INSTRUCTION_TEXT_STYLE.render("to move the left paddle inside the left frame",
                                                         True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 50))

        continue_text = fonts.BODY_TEXT_STYLE.render("Click mouse to continue",
                                                     True, Color('antiquewhite3'))
        self.__screen.blit(continue_text,
                           (self.SCREEN_WIDTH // 2 - continue_text.get_width() // 2, self.SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

    def draw2(self):
        self.__screen.fill(Color('antiquewhite'))
        title_text = fonts.INSTRUCTION_TEXT_STYLE.render("Point your index finger UP, DOWN",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 100))
        
        title_text = fonts.INSTRUCTION_TEXT_STYLE.render("to move the right paddle inside the right frame",
                                                         True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 50))

        continue_text = fonts.BODY_TEXT_STYLE.render("Click mouse to continue",
                                                     True, Color('antiquewhite3'))
        self.__screen.blit(continue_text,
                           (self.SCREEN_WIDTH // 2 - continue_text.get_width() // 2, self.SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

    def draw3(self):
        self.__screen.fill(Color('antiquewhite'))
        title_text = fonts.INSTRUCTION_TEXT_STYLE.render("First one score\n5pts will win.",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(title_text,
                           (self.SCREEN_WIDTH // 2 - title_text.get_width() // 2, self.SCREEN_HEIGHT // 2 - 100))

        continue_text = fonts.BODY_TEXT_STYLE.render("Click mouse to back to main menu",
                                                     True, Color('antiquewhite3'))
        self.__screen.blit(continue_text,
                           (self.SCREEN_WIDTH // 2 - continue_text.get_width() // 2, self.SCREEN_HEIGHT // 2))

        pygame.display.flip()

    def __main_loop(self):
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                if self.__handle_event(event):
                    self.count += 1

            if self.count > self.max_count:
                self.__is_running = False
                break

            getattr(self, f"draw{self.count}")()

            pygame.display.flip()

    def __handle_event(self, event):
        keys = pygame.key.get_pressed()

        if event.type == pygame.QUIT:
            self.__is_running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            return True
        return False
