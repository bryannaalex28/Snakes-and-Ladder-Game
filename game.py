import random

def roll_dice():
    return random.randint(1, 6)

special_tiles = {
    "extra_roll": [8, 15, 23, 32, 55, 67, 88, 94],
    "reverse_snake": [14, 19, 28, 53, 77],
    "teleport": {
        10: 30,
        22: 45,
        35: 5, # Teleport backwards
        50: 75, # Teleport forwards
        68: 2 # Teleport to near start
    }
}


snakes = {
    16: 6,
    47: 26,
    62: 19,
    98: 78,
    95: 56,
    92: 75,
    87: 57,
    66: 48,
}

ladders = {
    1: 38,
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    36: 44,
    51: 67,
    71: 91,
    80: 100,
    58: 79,
    60: 83,
    70: 91,
    63: 85,
    76: 97,
}

def apply_special_tiles(player, dice_roll):
    old_position = player.position - dice_roll
    final_position = player.position

    # Teleport
    if final_position in special_tiles["teleport"]:
        new_position = special_tiles["teleport"][final_position]
        player.position = new_position
        return f"Teleported from {final_position} to {new_position}!", "teleport"

    # Extra roll
    if final_position in special_tiles["extra_roll"]:
        return f"Moved from {old_position} to {final_position}. Extra roll!", "extra_roll"

    # Reverse snake (example effect: move forward 5 tiles)
    if final_position in special_tiles["reverse_snake"]:
        new_position = final_position + 5
        player.position = min(new_position, 99)
        return f"Reverse snake at {final_position}! Jumped forward to {player.position}!", "reverse_snake"

    # Ladders
    if final_position in ladders:
        new_position = ladders[final_position]
        player.position = new_position
        return f"Climbed a ladder from {final_position} to {new_position}!", "ladder"

    # Snakes
    if final_position in snakes:
        new_position = snakes[final_position]
        player.position = new_position
        return f"Got bitten by a snake from {final_position} to {new_position}!", "snake"

    # Normal move
    return f"Moved from {old_position} to {final_position}", "move"
