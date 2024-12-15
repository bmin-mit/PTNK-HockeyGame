from screens.main_window import SCREEN_HEIGHT
from pygame.sprite import Sprite
from pygame import Rect


class PaddleSprite(Sprite):
    paddle_width: int = 20
    paddle_height: int = 100
    move_speed: int = 5
    rect: Rect

    def __init__(self, pos_x, pos_y):
        super().__init__()

        self.rect = Rect(pos_x, pos_y, self.paddle_width, self.paddle_height)

    def move_up(self):
        self.rect.y = max(0, self.rect.y - self.move_speed)

    def move_down(self):
        self.rect.y = min(SCREEN_HEIGHT, self.rect.y + self.move_speed)
