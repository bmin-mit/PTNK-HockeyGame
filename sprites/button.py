from pygame.color import Color
from pygame import Rect
from utils import fonts
import pygame

class Button(Rect):
    width: int = 225
    height: int = 50
    rect: Rect
    screen: pygame.Surface

    def __init__(self, screen, pos_x, pos_y, text):
        from screens.main_window import SCREEN_HEIGHT, SCREEN_WIDTH

        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.text = text

        super().__init__(pos_x - (self.width // 2), pos_y, self.width, self.height)
        self.screen = screen

    def draw(self):
        pygame.draw.rect(self.screen, Color('white'), self, border_radius=10)
        btn_text = fonts.OPTION_TEXT_STYLE.render(self.text, True, Color('black'))
        self.screen.blit(btn_text, (self.x + self.width // 2 - btn_text.get_width() // 2, self.y + self.height // 2 - btn_text.get_height() // 2))
