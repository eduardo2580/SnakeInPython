"""
This module provides the Apple class, which represents an 
apple object in the game. The apple is an item that the 
player can collect for points.

Author: Eduardo Benatti
"""

import random
from src import (BLOCK_SIZE, SH, SW, pygame)

class Apple:
    """
    A class to represent an apple in the game.

    Attributes:
    - rect (pygame.Rect): A rectangle representing the apple's position and size on the screen.

    Methods:
    - __init__(): Initializes the apple attributes and randomly places it on the screen.
    - randomize(): Randomly places the apple on the screen.
    - draw(screen): Draws the apple on the given screen.
    """

    def __init__(self):
        """
        Initialize an Apple object.

        Sets the initial position of the apple to (0, 0) and then randomizes its position.
        """
        self.rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self.randomize()

    def randomize(self) -> None:
        """
        Randomize the position of the apple.

        Randomly sets the x and y coordinates of the apple within the boundaries of the screen.
        """
        self.rect.x = random.randint(0, SW - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        self.rect.y = random.randint(0, SH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE

    def draw(self, screen) -> None:
        """
        Draw the apple on the screen.

        Args:
        - screen: The surface on which the apple will be drawn.
        """
        pygame.draw.rect(screen, "red", self.rect)
