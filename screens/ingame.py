import pygame
from pygame.color import Color
from sprites.paddle import Paddle
from sprites.ball import Ball
from utils import fonts

FPS = 60


class InGame:
    __paddle_left: Paddle
    __paddle_right: Paddle
    __ball: Ball
    __screen: pygame.Surface
    __is_running: bool
    __speed: float = 5
    __score_left: int = 0
    __score_right: int = 0

    def __init__(self, screen):
        from .main_window import SCREEN_HEIGHT, SCREEN_WIDTH

        self.__screen = screen

        self.__paddle_left = Paddle(
            screen, 50, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__paddle_right = Paddle(
            screen, SCREEN_WIDTH - 50 - Paddle.width, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__ball = Ball(self.__screen,
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.__speed)

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
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH
        self.__screen.fill(Color('antiquewhite'))

        score_text = fonts.TITLE_TEXT_STYLE.render(f"{self.__score_left} - {self.__score_right}",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(score_text,
                           (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 - score_text.get_height() // 2))

        up_text = fonts.BODY_TEXT_STYLE.render(
            "UP", True, Color('antiquewhite4'))
        self.__screen.blit(up_text,
                           (SCREEN_WIDTH - up_text.get_width() - 40, 40))
        down_text = fonts.BODY_TEXT_STYLE.render(
            "DOWN", True, Color('antiquewhite4'))
        self.__screen.blit(down_text,
                           (SCREEN_WIDTH - down_text.get_width() - 40, SCREEN_HEIGHT - down_text.get_height() - 40))

        w_text = fonts.BODY_TEXT_STYLE.render(
            "W", True, Color('antiquewhite4'))
        self.__screen.blit(w_text,
                           (40, 40))
        s_text = fonts.BODY_TEXT_STYLE.render(
            "S", True, Color('antiquewhite4'))
        self.__screen.blit(s_text,
                           (40, SCREEN_HEIGHT - s_text.get_height() - 40))

        self.__paddle_left.draw()
        self.__paddle_right.draw()
        self.__ball.move()

        if self.__paddle_left.collidepoint(self.__ball.x - Ball.RADIUS, self.__ball.y):
            self.__ball.bounce_left()
        if self.__paddle_right.collidepoint(self.__ball.x + Ball.RADIUS, self.__ball.y):
            self.__ball.bounce_right()
        if self.__ball.y - Ball.RADIUS < 0:
            self.__ball.bounce_top()
        if self.__ball.y + Ball.RADIUS > SCREEN_HEIGHT:
            self.__ball.bounce_bottom()

        if self.__ball.x + Ball.RADIUS < 0:
            self.__score_right += 1
            self.__increase_speed()
            self.__reset_ball()
        if self.__ball.x - Ball.RADIUS > SCREEN_WIDTH:
            self.__score_left += 1
            self.__increase_speed()
            self.__reset_ball()

        if max(self.__score_left, self.__score_right) == 5:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.__is_running = False
                            return

                self.__screen.fill(Color('antiquewhite'))

                title_text = fonts.TITLE_TEXT_STYLE.render(f"{"P1" if self.__score_left == 3 else "P2"} WIN!",
                                                           True, Color('antiquewhite4'))
                self.__screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width(
                ) // 2, SCREEN_HEIGHT // 2 - title_text.get_height() // 2))

                body_text = fonts.BODY_TEXT_STYLE.render(
                    "Press ENTER to play again!", True, Color('antiquewhite4'))
                self.__screen.blit(body_text, (SCREEN_WIDTH // 2 - body_text.get_width() // 2, SCREEN_HEIGHT //2 - body_text.get_height() // 2 + 50))

                pygame.display.flip()

        pygame.display.flip()

    def __increase_speed(self):
        self.__speed += 0.5
        self.__paddle_left.speed += 0.5
        self.__paddle_right.speed += 0.5

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

    def __reset_ball(self):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH
        self.__ball = Ball(self.__screen,
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.__speed)
