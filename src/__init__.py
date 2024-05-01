"""
Main package

This package provides a simple implementation of the classic Snake game using the Pygame library.
It consists of three modules: 

1. `__init__.py`: Defines the main function `snake_game()` to run the game.
2. `config_apple.py`: Contains the Apple class, which represents an apple object in the game.
3. `config_snake.py`: Contains the Snake class, which represents the snake entity in the Snake game.
"""

# Author
__author__ = "Eduardo Benatti"

# Version
__version__ = "1.1.0"

# Import
import pygame

""" Game configuration """

# Initialize Pygame
pygame.init()

# Screen dimensions
SW, SH = 650, 650

# Block size for snake and other game elements
BLOCK_SIZE = 50

# Font used for the game
FONT = pygame.font.Font(None, BLOCK_SIZE * 2)

# Create the game screen
screen = pygame.display.set_mode((SW, SH))

# Create a clock object to control frame rate
clock = pygame.time.Clock()

# Set the window caption
pygame.display.set_caption("Snake!")
