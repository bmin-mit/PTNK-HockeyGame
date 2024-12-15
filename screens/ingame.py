import pygame
import pygame.colordict as colors

class Ingame:
    __screen: pygame.Surface

    def __init__(self, screen):
        self.__screen = screen
        
        self.__draw()
        
        self.__main_loop()

    def __draw(self):
        """Vẽ màn hình trò chơi."""
        self.__screen.fill(pygame.Color('white'))
        pygame.display.flip()
    
    def __main_loop(self):
        while True:
            pass
        