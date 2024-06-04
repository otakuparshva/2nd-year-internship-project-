import os
import math
import pygame
from os.path import join

# Initialization and setup
pygame.init()
pygame.display.set_caption("One Piece: The Unreal Adventure")

# Global variables
BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1500, 800
FPS = 60
PLAYER_VEL = 5
PLAYER_HEALTH = 100
ENEMY_DAMAGE = 10
ENEMY_SPAWN_X = WIDTH + 200  # Initial position of enemy
ENEMY_Y = HEIGHT - 100  # Y position of enemy
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
SMART_ENEMY_SPEED = 2

# Creating window
window = pygame.display.set_mode((WIDTH, HEIGHT))

# Finding the number of background tiles needed
def bg_need(bg_width):
    tiles = math.ceil(WIDTH / bg_width) + 1  # Adding one more tile to ensure seamless scrolling
    return tiles

# Loading background
def get_background(name):
    # Construct the path
    path = join("..", "assets", "Background", name)
    # Check if the file exists
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No file '{path}' found in working directory '{os.getcwd()}'")
    return pygame.image.load(path)

# Drawing assets (scrolling background, player, enemy)
def draw(window, background, BG_WIDTH, tiles, scroll, player, enemies):
    # Draw background
    for i in range(tiles):
        window.blit(background, (i * BG_WIDTH + max(scroll, -505), 0))  # Ensure background constraint at (505, y)
    
    # Draw border
    pygame.draw.rect(window, (0, 0, 0), (0, 0, WIDTH, HEIGHT), 2)  # Border around the window
    
    # Draw player
    player.draw(window)
    
    # Draw enemies
    for enemy in enemies:
        enemy.draw(window)
    
    # Draw health bar
    draw_health_bar(window, player)
    
    pygame.display.update()

# Draw health bar
def draw_health_bar(window, player):
    bar_width = 200
    bar_height = 20
    fill = (player.health / PLAYER_HEALTH) * bar_width
    outline_rect = pygame.Rect(10, 10, bar_width, bar_height)
    fill_rect = pygame.Rect(10, 10, fill, bar_height)
    pygame.draw.rect(window, (255, 0, 0), fill_rect)
    pygame.draw.rect(window, (0, 0, 0), outline_rect, 2)

# Player class
class Player:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration_y = 0.5
        self.jump_velocity = -10
        self.is_jumping = False
        self.health = PLAYER_HEALTH
        self.blast_radius = 10
        self.blast_color = (255, 255, 0)
        self.blast_speed = 10
        self.blasts = []

    def update(self):
        self.velocity_y += self.acceleration_y
        self.y += self.velocity_y

        if self.y >= HEIGHT - self.height:
            self.y = HEIGHT - self.height
            self.velocity_y = 0
            self.is_jumping = False

        self.x += self.velocity_x

        # Update blasts
        for blast in self.blasts:
            blast['x'] += self.blast_speed

    def jump(self):
        if not self.is_jumping:
            self.velocity_y = self.jump_velocity
            self.is_jumping = True

    def move_left(self):
        self.velocity_x = -PLAYER_VEL

    def move_right(self):
        self.velocity_x = PLAYER_VEL

    def stop_moving(self):
        self.velocity_x = 0

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y, self.width, self.height))

        # Draw blasts
        for blast in self.blasts:
            pygame.draw.circle(window, self.blast_color, (blast['x'], blast['y']), self.blast_radius)

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def range_attack(self):
        blast = {'x': self.x + self.width, 'y': self.y + self.height // 2}
        self.blasts.append(blast)

# Enemy class
class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def update(self, player_x):
        # Implement smart enemy logic here
        if self.x < player_x:
            self.x += self.speed
        elif self.x > player_x:
            self.x -= self.speed

    def draw(self, window):
        pygame.draw.rect(window, (0, 0, 255), (self.x, self.y, self.width, self.height))

# Main function
def main(window):
    clock = pygame.time.Clock()
    background = get_background('generalSkyBg.jpg')
    BG_WIDTH = background.get_width()
    tiles = bg_need(BG_WIDTH)

scroll = 0  # Define the scroll variable

run = True
player = Player(WIDTH // 2, HEIGHT - 100, 50, 50)
enemies = [Enemy(ENEMY_SPAWN_X, ENEMY_Y, ENEMY_WIDTH, ENEMY_HEIGHT, SMART_ENEMY_SPEED)]

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()
            if event.key == pygame.K_q:
                player.range_attack()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player.velocity_x < 0:
                player.stop_moving()
            if event.key == pygame.K_RIGHT and player.velocity_x > 0:
                player.stop_moving()

    # Update player and enemies
    player.update()
    for enemy in enemies:
        enemy.update(player.x)

    # Adjust scroll based on player's movement
    if player.x > WIDTH // 2:
        scroll -= player.velocity_x

    draw(window, background, BG_WIDTH, tiles, scroll, player, enemies)

    # Check for player health
    if player.health <= 0:
        print("Game Over")
        run = False

pygame.quit()
quit()

if __name__ == "__main__":
    main(window)

