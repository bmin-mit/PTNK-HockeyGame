import pygame
import random
import sys

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAIN_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("")

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
DARK_GRAY = (150, 150, 150)

# FPS (Tốc độ khung hình)
clock = pygame.time.Clock()
FPS = 60

# Kích thước giỏ và bóng
BASKET_WIDTH = 100
BASKET_HEIGHT = 20
BALL_RADIUS = 15

# Tạo giỏ
basket = pygame.Rect(SCREEN_WIDTH // 2 - BASKET_WIDTH // 2, SCREEN_HEIGHT - 50, BASKET_WIDTH, BASKET_HEIGHT)

# Tạo bóng
ball = {
    "x": random.randint(0, SCREEN_WIDTH - BALL_RADIUS),
    "y": 0,
    "speed": 5
}

# Điểm số
score = 0

# Font chữ
font = pygame.font.SysFont(None, 36)

# Tạo nút thoát
button_font = pygame.font.SysFont(None, 30)
button_text = button_font.render("Thoát Game", True, WHITE)
button_rect = pygame.Rect(SCREEN_WIDTH - 150, 10, 140, 40)

def draw_screen():
    """Vẽ màn hình trò chơi."""
    MAIN_SCREEN.fill(WHITE)
    pygame.draw.rect(MAIN_SCREEN, BLUE, basket)
    pygame.draw.circle(MAIN_SCREEN, RED, (ball["x"], ball["y"]), BALL_RADIUS)
    score_text = font.render(f"Điểm: {score}", True, BLACK)
    MAIN_SCREEN.blit(score_text, (10, 10))
    pygame.draw.rect(MAIN_SCREEN, GRAY, button_rect)
    MAIN_SCREEN.blit(button_text, (button_rect.x + 15, button_rect.y + 8))
    pygame.display.flip()

def move_basket(keys):
    """Di chuyển giỏ theo phím bấm."""
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and basket.right < SCREEN_WIDTH:
        basket.move_ip(10, 0)

def update_ball():
    """Cập nhật vị trí bóng và kiểm tra va chạm."""
    global score
    ball["y"] += ball["speed"]
    # Nếu bóng chạm đáy
    if ball["y"] > SCREEN_HEIGHT:
        reset_ball()
    # Nếu bóng va chạm với giỏ
    if basket.collidepoint(ball["x"], ball["y"]):
        score += 1
        reset_ball()

def reset_ball():
    """Đặt lại bóng về vị trí ban đầu."""
    ball["x"] = random.randint(0, SCREEN_WIDTH - BALL_RADIUS)
    ball["y"] = 0
    ball["speed"] += 0.2  # Tăng tốc độ bóng mỗi lần hứng thành công

def show_start_screen():
    """Hiển thị màn hình chờ trước khi bắt đầu trò chơi."""
    MAIN_SCREEN.fill(WHITE)
    title_font = pygame.font.SysFont(None, 60)
    title_text = title_font.render("Chào mừng đến với Game Hứng Bóng!", True, BLACK)
    MAIN_SCREEN.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 2 - 100))

    instruction_font = pygame.font.SysFont(None, 36)
    instruction_text = instruction_font.render("Nhấn phím bất kỳ để bắt đầu...", True, BLACK)
    MAIN_SCREEN.blit(instruction_text, (SCREEN_WIDTH // 2 - instruction_text.get_width() // 2, SCREEN_HEIGHT // 2))

    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

# Vòng lặp chính
def main():
    """Vòng lặp chính của trò chơi."""
    global score
    show_start_screen()  # Hiển thị màn hình chờ trước khi trò chơi bắt đầu

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    running = False

        # Lấy trạng thái bàn phím
        keys = pygame.key.get_pressed()
        move_basket(keys)
        update_ball()
        draw_screen()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
