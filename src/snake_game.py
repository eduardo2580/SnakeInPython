"""
This module provides a simple implementation of the classic 
Snake game using the Pygame library.
It defines the main function `snake_game()` to run the game.

Author: Eduardo Benatti
"""

import sys

sys.path.append(rf"C:\Users\erics\PycharmProjects\snakeinpython")

from src import (SH, SW, FONT, screen, clock, pygame)
import apple_config
import snake_config

def snake_game() -> None:
    """
    Main function to run the Snake game.
    
    Initializes the snake and apple objects, and enters the game loop.
    Handles user input to change the snake's direction.
    Updates the game state, draws game elements on the screen, and controls game speed.
    """
    snake_obj = snake_config.Snake()
    apple_obj = apple_config.Apple()

    score = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                # Handle key presses to change snake direction
                if event.key == pygame.K_DOWN and snake_obj.ydir != -1:
                    snake_obj.ydir = 1
                    snake_obj.xdir = 0
                elif event.key == pygame.K_UP and snake_obj.ydir != 1:
                    snake_obj.ydir = -1
                    snake_obj.xdir = 0
                elif event.key == pygame.K_RIGHT and snake_obj.xdir != -1:
                    snake_obj.ydir = 0
                    snake_obj.xdir = 1
                elif event.key == pygame.K_LEFT and snake_obj.xdir != 1:
                    snake_obj.ydir = 0
                    snake_obj.xdir = -1

        # Update snake and apple
        snake_obj.update(apple_obj)

        # Draw game elements on the screen
        screen.fill('black')
        snake_obj.draw(screen)
        apple_obj.draw(screen)

        # Check for apple collision and update score
        if snake_obj.head.colliderect(apple_obj.rect):
            score += 1

        # Display score on the screen
        score_text = FONT.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (SW // 2 - score_text.get_width() // 2, SH // 20))

        # Update display and control game speed
        pygame.display.update()
        clock.tick(10)
    

if __name__ == "__main__":
    snake_game()
