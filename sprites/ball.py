import pygame
from pygame.color import Color


class Ball:
    x: int
    y: int
    screen: pygame.Surface

    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, Color('darkblue'), (self.x, self.y), 20)