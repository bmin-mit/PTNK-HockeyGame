from screens.main_window import SCREEN_HEIGHT
from pygame.color import Color
from pygame import Rect
import pygame

class Paddle(Rect):
    width: int = 20
    height: int = 100
    speed: int = 5
    rect: Rect
    screen: pygame.Surface

    def __init__(self, screen, pos_x, pos_y):
        super().__init__(pos_x, pos_y, self.width, self.height)
        self.screen = screen

    def move_up(self):
        if self.y > 0:
            self.move_ip(0, -self.speed)

    def move_down(self):
        if self.y + self.height < SCREEN_HEIGHT:
            self.move_ip(0, self.speed)

    def draw(self):
        pygame.draw.rect(self.screen, Color('aquamarine4'), self)
