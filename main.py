import pygame
import random
from assets.board import draw_board, draw_players
from assets.player import Player
from game import roll_dice, apply_special_tiles

pygame.init()
pygame.mixer.init()

# Constants
WIDTH, HEIGHT = 600, 600
ROWS, COLS = 10, 10
TILE_SIZE = WIDTH // COLS
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snakes and Ladders")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

# Font colors
DICE_COLOR = (139, 0, 0)      # Dark red
MOVE_COLOR = (20, 120, 40)    # Dark green

# Load dice images
DICE_IMAGES = [pygame.image.load(f"assets/images/dice{i}.png") for i in range(1, 7)]
DICE_IMAGES = [pygame.transform.scale(img, (60, 60)) for img in DICE_IMAGES]

# Load sounds
roll_sound = pygame.mixer.Sound("assets/sounds/roll.wav")
win_sound = pygame.mixer.Sound("assets/sounds/win.wav")


# Players
players = [
    Player((255, 0, 0), "Player 1"),     # Red
    Player((255, 105, 180), "Player 2")  # Pink
]

current_player = 0
running = True
winner = None
last_roll_text = ""
rolling = False
frame = 0
dice_roll_result = 1
show_start_screen = True

def show_text_centered(text, y_offset=0):
    text_surface = font.render(text, True, (0, 0, 0))
    rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 + y_offset))
    screen.blit(text_surface, rect)

def show_dice():
    screen.blit(DICE_IMAGES[dice_roll_result - 1], (WIDTH - 80, HEIGHT - 80))

while running:
    screen.fill((255, 255, 255))

    # Start screen
    if show_start_screen:
        show_text_centered("Welcome to Snakes and Ladders!")
        show_text_centered("Press SPACE to Start", 40)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                show_start_screen = False
        pygame.display.flip()
        clock.tick(30)
        continue

    draw_board(screen)
    draw_players(screen, players, TILE_SIZE, COLS)
    show_dice()

    if winner:
        win_text = font.render(f"{winner} Wins! Press ESC to quit.", True, (200, 30, 30))
        screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
    else:
        if last_roll_text:
            # Split last_roll_text into roll message and move message
            if ". " in last_roll_text:
                roll_msg, move_msg = last_roll_text.split(". ", 1)
                roll_msg += "."
            else:
                roll_msg, move_msg = last_roll_text, ""

            # Top left: movement
            move_text = font.render(move_msg, True, MOVE_COLOR)
            screen.blit(move_text, (20, 20))
            # Bottom left: dice roll
            roll_text = font.render(roll_msg, True, DICE_COLOR)
            screen.blit(roll_text, (20, HEIGHT - 40))
        else:
            turn_msg = f"{players[current_player].name}'s Turn (Press SPACE to Roll)"
            screen.blit(font.render(turn_msg, True, DICE_COLOR), (20, HEIGHT - 40))

    # Dice animation
    if rolling:
        if frame < len(DICE_IMAGES):
            screen.blit(DICE_IMAGES[frame], (WIDTH - 80, HEIGHT - 80))
            frame += 1
        else:
            rolling = False
            steps = roll_dice()
            dice_roll_result = steps
            roll_sound.play()

            player = players[current_player]
            old_position = player.position
            player.move(steps)
            move_message = apply_special_tiles(player, steps)

            last_roll_text = f"{player.name} rolled a {steps}. {move_message}"

            if "Extra roll" in move_message:
                pass
            else:
                current_player = (current_player + 1) % len(players)

            if player.position >= 99:
                winner = player.name
                win_sound.play()

            frame = 0

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE and not rolling and winner is None:
                rolling = True
                frame = 0

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
