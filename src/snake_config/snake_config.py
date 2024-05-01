"""
Module containing the Snake class for the Snake game.

This module provides the Snake class, which represents the 
snake entity in the Snake game.
The Snake class handles the snake's movement, collision 
detection, and drawing on the screen.

Author: Eduardo Benatti
"""

# Import statements and code for the Snake class go here


import apple_config  # Import the apple_config module
from src import (BLOCK_SIZE, SH, SW, pygame)  # Import constants and libraries from the src module


class Snake:
    """
    Class to represent the snake in the Snake game.

    Attributes:
        x (int): x position of the snake's head.
        y (int): y position of the snake's head.
        xdir (int): Direction of the snake on the x-axis (-1 for left, 1 for right).
        ydir (int): Direction of the snake on the y-axis (-1 for up, 1 for down).
        head (pygame.Rect): Rectangle representing the snake's head.
        body (list): List of rectangles representing the snake's body.
        dead (bool): Indicates whether the snake is dead (True) or alive (False).
    """

    def __init__(self):
        """
        Initializes the snake's attributes.

        Initializes the snake's position, direction, head, and body.
        """
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self, apple: apple_config) -> None:
        """
        Updates the snake's position and checks for collisions.

        Args:
            apple (apple_config): Apple object to check for collisions.

        Returns:
            None
        """
        # Check for collisions with the snake's body or walls
        for square in self.body:
            if self.head.colliderect(square):
                self.dead = True
            if not (0 <= self.head.x < SW and 0 <= self.head.y < SH):
                self.dead = True

        # Handle snake death
        if self.dead:
            self.reset()

        # Update the snake's body
        self.body.insert(0, self.head.copy())
        if self.head.colliderect(apple.rect):
            apple.randomize()
        else:
            self.body.pop()

        # Move the snake's head
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE

    def reset(self) -> None:
        """
        Resets the snake.

        Reinitializes the snake's attributes to restart the game.

        Returns:
            None
        """
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.xdir = 1
        self.ydir = 0
        self.dead = False

    def draw(self, screen) -> None:
        """
        Draws the snake on the screen.

        Args:
            screen: Screen where the snake will be drawn.

        Returns:
            None
        """
        # Draw the snake's head
        pygame.draw.rect(screen, "green", self.head)
        # Draw the snake's body
        for square in self.body:
            pygame.draw.rect(screen, "green", square)
