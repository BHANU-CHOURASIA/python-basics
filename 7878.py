# ===================================================
# MINI GAME: GOLD COLLECTOR (PYGAME INTERACTIVE)
# ===================================================

import pygame
import random
import sys

# 1. Pygame Setup
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("🎮 Gold Collector Game - Bhanu's Arena")

clock = pygame.time.Clock()

# 2. Colors (RGB Format)
DARK_NAVY = (15, 23, 42)
HERO_GREEN = (34, 197, 94)
GOLD_YELLOW = (234, 179, 8)
WHITE = (255, 255, 255)

# 3. Player (Hero) Properties
# Rect(x, y, width, height)
player_rect = pygame.Rect(375, 275, 40, 40)
player_speed = 6

# 4. Gold Coin Properties
coin_rect = pygame.Rect(random.randint(50, 750), random.randint(50, 550), 25, 25)

# 5. Score & Font Setup
score = 0
game_font = pygame.font.SysFont("Arial", 28, bold=True)

# Main Game Loop
is_running = True

while is_running:
    # --- A. EVENT HANDLING (Window Close Check) ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # --- B. KEYBOARD INPUTS (Hero Movement) ---
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_rect.left > 0:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player_rect.right < SCREEN_WIDTH:
        player_rect.x += player_speed
    if keys[pygame.K_UP] and player_rect.top > 0:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN] and player_rect.bottom < SCREEN_HEIGHT:
        player_rect.y += player_speed

    # --- C. COLLISION DETECTION (Hero touches Coin) ---
    # colliderect() check karta hai ki kya dono shapes apas mein takraye hain
    if player_rect.colliderect(coin_rect):
        score += 10  # Score increase
        # Coin ko random nayi jagah bhej do
        coin_rect.x = random.randint(50, SCREEN_WIDTH - 50)
        coin_rect.y = random.randint(50, SCREEN_HEIGHT - 50)

    # --- D. DRAW GRAPHICS ---
    # 1. Screen fill
    screen.fill(DARK_NAVY)

    # 2. Hero (Green Square) Draw karna
    pygame.draw.rect(screen, HERO_GREEN, player_rect, border_radius=6)

    # 3. Gold Coin (Yellow Circle/Square) Draw karna
    pygame.draw.ellipse(screen, GOLD_YELLOW, coin_rect)

    # 4. Scoreboard Print karna
    score_text = game_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (20, 20))

    # 5. Screen Update
    pygame.display.flip()

    # 6. 60 FPS Lock
    clock.tick(60)

pygame.quit()
sys.exit()