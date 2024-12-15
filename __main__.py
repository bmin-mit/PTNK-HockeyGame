import pygame

if __name__ == "__main__":
    pygame.init()
    
    from screens.main_window import MainWindow
    MainWindow()
    
    pygame.quit()
