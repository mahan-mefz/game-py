import pygame
import sys

# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات صفحه
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simple Pygame Example')

# رنگ‌ها
black = (0, 0, 0)
white = (255, 255, 255)

# متغیرهای بازیکن
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_speed = 5

# حلقه اصلی بازی
running = True
while running:
    # بررسی رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # گرفتن ورودی کلیدها
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # پر کردن صفحه
    screen.fill(black)

    # رسم بازیکن
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # به‌روزرسانی صفحه
    pygame.display.flip()

    # تنظیم فریم ریت
    pygame.time.Clock().tick(60)