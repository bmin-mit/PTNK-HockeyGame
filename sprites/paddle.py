from pygame.color import Color
from pygame import Rect
import pygame

class Paddle(Rect):
    width: int = 20
    height: int = 100
    speed: int = 7
    rect: Rect
    screen: pygame.Surface
    sound: pygame.mixer.Sound

    def __init__(self, screen, pos_x, pos_y, speed=7):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH

        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.speed = speed

        super().__init__(pos_x, pos_y, self.width, self.height)
        self.screen = screen
        self.sound = pygame.mixer.Sound('./assets/pong.mp3')
        self.sound.set_volume(3)

    def move_up(self):
        if self.y > 0:
            self.move_ip(0, -self.speed)

    def move_down(self):
        if self.y + self.height < self.SCREEN_HEIGHT:
            self.move_ip(0, self.speed)

    def draw(self):
        pygame.draw.rect(self.screen, Color('aquamarine4'), self)

    def play_sound(self):
        self.sound.play()
