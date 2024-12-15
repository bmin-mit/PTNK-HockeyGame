import pygame

class PaddleSprite(pygame.Rect):
    paddle_width: int = 20
    paddle_height: int = 100
    move_speed: int = 5

    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, self.paddle_width, self.paddle_height)
    
    def move_up(self):
        self.y = max(0, self.y - self.move_speed)
    
    def move_down(self):
        self.move_ip(0, self.move_speed)