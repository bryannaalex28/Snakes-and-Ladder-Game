import pygame
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from game import snakes, ladders  # Import the snakes and ladders dictionaries

# Initialize pygame
pygame.init()

# Set up display dimensions
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
TILE_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")

current_dir = os.path.dirname(os.path.abspath(__file__))

# Load images with relative path
snake_img_path = os.path.join(current_dir, 'images', 'snake.png')
ladder_img_path = os.path.join(current_dir, 'images', 'ladder.png')

# Load images
snake_img = pygame.image.load(snake_img_path)
ladder_img = pygame.image.load(ladder_img_path)

# Resize images to fit tiles
snake_img = pygame.transform.scale(snake_img, (TILE_SIZE, TILE_SIZE))
ladder_img = pygame.transform.scale(ladder_img, (TILE_SIZE, TILE_SIZE))

# Colors
WHITE = (255, 255, 255)
PINK = (255, 182, 193)
RED = (255, 102, 102)
BLACK = (0, 0, 0)
TILE_COLORS = [WHITE, PINK, RED]

# Snakes and ladders positions (tile numbers, 1-based)
font = pygame.font.SysFont(None, 20)

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            # Draw the tile (coloring)
            color_index = (row * COLS + col) % len(TILE_COLORS)
            color = TILE_COLORS[color_index]
            x = col * TILE_SIZE
            y = row * TILE_SIZE
            pygame.draw.rect(screen, color, (x, y, TILE_SIZE, TILE_SIZE))

            # Draw the tile number (for reference)
            tile_num = row * COLS + col + 1
            num_text = font.render(str(tile_num), True, (0, 0, 0))  
            text_rect = num_text.get_rect(center=(x + TILE_SIZE // 2, y + TILE_SIZE // 2))
            screen.blit(num_text, text_rect)

            # Draw the snake and ladder images where applicable
            if tile_num in snakes:
                screen.blit(snake_img, (x, y))
            if tile_num in ladders:
                screen.blit(ladder_img, (x, y))


def draw_players(screen, players, tile_size, cols):
    for idx, player in enumerate(players):
        row = player.position // cols
        col = player.position % cols
        if row % 2 == 1:
            col = cols - 1 - col

        x = col * tile_size + tile_size // 4 + (idx * 10)
        y = (9 - row) * tile_size + tile_size // 4

        pygame.draw.circle(screen, player.color, (x, y), 10)
