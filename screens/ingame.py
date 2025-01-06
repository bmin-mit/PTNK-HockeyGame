import cv2
import pygame
from pygame.color import Color
from sprites.paddle import Paddle
from sprites.ball import Ball
from utils import fonts
from utils.score import write_data
import mediapipe as mp

FPS = 60

mp_drawing = mp.solutions.drawing_utils

class InGame:
    __paddle_left: Paddle
    __paddle_right: Paddle
    __ball: Ball
    __screen: pygame.Surface
    __is_running: bool
    __speed: float = 5
    __score_left: int = 0
    __score_right: int = 0
    __hands: mp.solutions.hands.Hands

    def __init__(self, screen):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH

        self.__screen = screen

        self.__paddle_left = Paddle(
            screen, 50, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__paddle_right = Paddle(
            screen, SCREEN_WIDTH - 50 - Paddle.width, SCREEN_HEIGHT // 2 - Paddle.height // 2)
        self.__ball = Ball(self.__screen,
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.__speed)

        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.ret, self.frame = self.cap.read()
        cv2.imshow('frame', self.frame)
        cv2.moveWindow('frame', 0, 0)
        self.hands = mp.solutions.hands.Hands(static_image_mode=False,
                                              max_num_hands=2,
                                              min_detection_confidence=0.5,
                                              model_complexity=1)

        self.__main_loop()

    def __show_camera(self):
        self.ret, self.frame = self.cap.read()
        if self.ret:
            self.cv2_window_dimension = (x, y, w, h) = cv2.getWindowImageRect('frame')
            self.frame = cv2.flip(self.frame, 1)
            cv2.line(self.frame, (w // 2, 0), (w // 2, h), (0, 0, 255), 2)
            self.__draw_landmarks(self.frame)
            cv2.imshow('frame', self.frame)
            self.__hand_gestures()
    
    def __hand_gestures(self):
        multi_hand_landmarks = self.result.multi_hand_landmarks
        w, h = self.cv2_window_dimension[2:]

        if multi_hand_landmarks:
            for hand_landmarks in multi_hand_landmarks:
                index_base = hand_landmarks.landmark[5]
                index_tip = hand_landmarks.landmark[8]
                
                print(index_base, index_tip)

                x_tip, y_tip = int(index_tip.x * w), int(index_tip.y * h)
                x_base, y_base = int(index_base.x * w), int(index_base.y * h)
                
                if x_base < w // 2:
                    if y_tip < y_base:
                        self.__paddle_left.move_up()
                    else:
                        self.__paddle_left.move_down()
                else:
                    if y_tip < y_base:
                        self.__paddle_right.move_up()
                    else:
                        self.__paddle_right.move_down()

    def __main_loop(self):
        clock = pygame.time.Clock()
        self.__is_running = True

        while self.__is_running:
            for event in pygame.event.get():
                self.__handle_event(event)

            self.__show_camera()

            self.__draw()
            clock.tick(FPS)

        self.cap.release()
        cv2.destroyAllWindows()

    def __draw(self):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH
        self.__screen.fill(Color('antiquewhite'))

        score_text = fonts.TITLE_TEXT_STYLE.render(f"{self.__score_left} - {self.__score_right}",
                                                   True, Color('antiquewhite4'))
        self.__screen.blit(score_text,
                           (SCREEN_WIDTH // 2 - score_text.get_width() // 2,
                            SCREEN_HEIGHT // 2 - score_text.get_height() // 2))

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
            self.__paddle_left.play_sound()
        if self.__paddle_right.collidepoint(self.__ball.x + Ball.RADIUS, self.__ball.y):
            self.__ball.bounce_right()
            self.__paddle_right.play_sound()
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
            write_data(self.__score_left, self.__score_right)
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.__is_running = False
                        return

                self.__screen.fill(Color('antiquewhite'))

                title_text = fonts.TITLE_TEXT_STYLE.render(f"{"P1" if self.__score_left == 3 else "P2"} WIN!",
                                                           True, Color('antiquewhite4'))
                self.__screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width(
                ) // 2, SCREEN_HEIGHT // 2 - title_text.get_height() // 2))

                body_text = fonts.BODY_TEXT_STYLE.render(
                    "Click mouse to back to menu!", True, Color('antiquewhite4'))
                self.__screen.blit(body_text, (
                SCREEN_WIDTH // 2 - body_text.get_width() // 2, SCREEN_HEIGHT // 2 - body_text.get_height() // 2 + 50))

                pygame.display.flip()

        pygame.display.flip()
    
    def __draw_landmarks(self, frame):
        self.result = self.hands.process(frame)

        if self.result.multi_hand_landmarks:
            for hand_landmarks in self.result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    def __increase_speed(self):
        self.__speed += 0.5
        self.__paddle_left.speed += 0.5
        self.__paddle_right.speed += 0.5

    def __handle_event(self, event):
        if event.type == pygame.QUIT:
            self.__is_running = False
            pygame.quit()

    def __reset_ball(self):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH
        self.__ball = Ball(self.__screen,
                           SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, self.__speed)
