import pygame
from pygame.color import Color
from sprites.paddle import Paddle
from sprites.ball import Ball


FPS = 60


class Ingame:
    __paddle_left: Paddle
    __paddle_right: Paddle
    __ball: Ball
    __screen: pygame.Surface
    __is_running: bool

    def __init__(self, screen):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH

        self.__screen = screen

        self.__paddle_left = Paddle(
            screen, 50, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__paddle_right = Paddle(
            screen, SCREEN_WIDTH - 50 - Paddle.width, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__ball = Ball(self.__screen,
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        self.__main_loop()

    def __main_loop(self):
        clock = pygame.time.Clock()
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                self.__handle_event(event)

            self.__handle_key()
            self.__draw()
            clock.tick(FPS)

    def __draw(self):
        self.__screen.fill(Color('antiquewhite'))

        self.__paddle_left.draw()
        self.__paddle_right.draw()
        self.__ball.draw()

        pygame.display.flip()

    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.__is_running = False
            pygame.quit()

    def __handle_key(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and not keys[pygame.K_s]:
            self.__paddle_left.move_up()
        elif keys[pygame.K_s] and not keys[pygame.K_w]:
            self.__paddle_left.move_down()

        if keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
            self.__paddle_right.move_up()
        elif keys[pygame.K_DOWN] and not keys[pygame.K_UP]:
            self.__paddle_right.move_down()
