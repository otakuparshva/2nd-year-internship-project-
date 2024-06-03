import os
import random
import math
import pygame
from os.path import join

# initialization and setup
pygame.init()
pygame.display.set_caption("One Piece: The Unreal Adventure")

# GLOBAL VARIABLES
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1500, 800
FPS = 60
PLAYER_VEL = 5

# creating window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# FIND GAME VARIABLES (No. of bg tiles needed)
def bg_need(bg_width):
    tiles = math.ceil(WIDTH / bg_width) + 1  # Adding one more tile to ensure seamless scrolling
    return tiles

# LOADING BACKGROUND
def get_background(name):
    # Print the current working directory for debugging
    print(f"Current working directory: {os.getcwd()}")
    # Construct the path
    path = join("..", "assets", "Background", name)
    # Print the constructed path for debugging
    print(f"Constructed path: {path}")

    # Check if the file exists
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No file '{path}' found in working directory '{os.getcwd()}'")
    
    bg = pygame.image.load(path)
    bg_width = bg.get_width()
    return bg, bg_width

# DRAWING ASSETS (SCROLLING BACKGROUND, ..)
def draw(window, background, BG_WIDTH, tiles, scroll):
    for i in range(tiles):
        window.blit(background, (i * BG_WIDTH + scroll, 0))
    pygame.display.update()

# MAIN FUNCTION
def main(window):
    clock = pygame.time.Clock()
    background, BG_WIDTH = get_background('generalSkyBg.jpg')
    tiles = bg_need(BG_WIDTH)

    scroll = 0
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw(window, background, BG_WIDTH, tiles, scroll)
        scroll -= 5

        # RESET SCROLL 
        if abs(scroll) >= BG_WIDTH:
            scroll = 0

    pygame.quit()
    quit()

if __name__ == "__main__":
    main(window)
