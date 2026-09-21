# ===================================================
# PART 9: PYGAME - FIRST GAME WINDOW & GAME LOOP
# ===================================================

import pygame  # PyGame toolbox import kiya
import sys     # System Exit ke liye

# 1. PyGame Engine Initialize (Start) Kiya
pygame.init()

# 2. Window Size (Width, Height) aur Display Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game Window Ka Title (Name) Set Kiya
pygame.display.set_caption("MCA Game Dev Arena - Chapter 1")

# 3. Colors Define Kiye (RGB Format: Red, Green, Blue -> 0 to 255)
BACKGROUND_COLOR = (20, 30, 50)  # Dark Blue Accent

# Frame Rate Control (60 FPS Game Loop)
clock = pygame.time.Clock()

# Game Loop Control Variable
is_running = True


# ===================================================
# MAIN GAME LOOP
# ===================================================
while is_running:
    # --- A. EVENT HANDLING (Inputs check karna) ---
    for event in pygame.event.get():
        # Agar player ne Window ka Close (X) button dabaya
        if event.type == pygame.QUIT:
            is_running = False

    # --- B. GAME LOGIC / UPDATES ---
    # (Aage ke parts mein yahan player movement & score update hoga)

    # --- C. DRAW / RENDER GRAPHICS ---
    # Screen ko background color se fill karna
    screen.fill(BACKGROUND_COLOR)

    # Screen refresh / update karna
    pygame.display.flip()

    # Loop Speed Limit (60 Frames Per Second)
    clock.tick(60)

# Game Loop se bahar aane par PyGame aur Window Safely Close karna
pygame.quit()
sys.exit()