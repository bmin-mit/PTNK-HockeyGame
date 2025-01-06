import pygame
from pygame.color import Color
from math import radians, cos, sin
from random import randint


class Ball:
    x: int
    y: int
    direction: float
    speed: int
    screen: pygame.Surface
    RADIUS: int = 20

    def __init__(self, screen, x, y, speed):
        self.x = x
        self.y = y
        self.direction = randint(-45, 45) if randint(
            0, 1) else randint(135, 225)
        if self.direction == 0:
            self.direction = randint(1, 45) if randint(0, 1) else randint(-45, -1)
        self.screen = screen
        self.speed = speed

    def draw(self):
        pygame.draw.circle(self.screen, Color(
            'darkblue'), (self.x, self.y), self.RADIUS)

    def move(self):
        rad = radians(self.direction)

        self.x += cos(rad) * self.speed
        self.y -= sin(rad) * self.speed

        self.draw()

    def bounce_left(self):
        self.direction += 180
        self.direction %= 360
        self.direction = -self.direction

    def bounce_right(self):
        self.direction += 180
        self.direction %= 360
        self.direction += 2 * (180 - self.direction)
    
    def bounce_top(self):
        self.direction += 180
        self.direction %= 360
        self.direction += 2 * (-90 - self.direction)
    
    def bounce_bottom(self):
        self.direction *= -1
        self.direction %= 360
