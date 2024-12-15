import pygame
import pygame.colordict as colors

class IngameScreen:
    main_screen: pygame.Surface

    def __init__(self, main_screen):
        self.main_screen = main_screen

    def draw_screen(self):
        """Vẽ màn hình trò chơi."""
        self.main_screen.fill(pygame.Color('white'))
        pygame.draw.rect(self.main_screen, pygame.Color('blue'), basket)
        pygame.draw.circle(self.main_screen, RED, (ball["x"], ball["y"]), BALL_RADIUS)
        score_text = font.render(f"Điểm: {score}", True, BLACK)
        self.main_screen.blit(score_text, (10, 10))
        pygame.draw.rect(self.main_screen, GRAY, button_rect)
        self.main_screen.blit(button_text, (button_rect.x + 15, button_rect.y + 8))
        pygame.display.flip()