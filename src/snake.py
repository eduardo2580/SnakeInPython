import pygame
import sys
import random

pygame.init()

SW, SH = 650, 650

BLOCK_SIZE = 50
FONT = pygame.font.Font(None, BLOCK_SIZE * 2)

screen = pygame.display.set_mode((SW, SH))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        # Initialize snake attributes
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False

    def update(self):
        global apple

        # Check for collisions with snake body or walls
        for square in self.body:
            if self.head.colliderect(square):
                self.dead = True
            if not (0 <= self.head.x < SW and 0 <= self.head.y < SH):
                self.dead = True

        # Handle snake death
        if self.dead:
            self.reset()
            apple = Apple()

        # Update snake's body
        self.body.insert(0, self.head.copy())
        if self.head.colliderect(apple.rect):
            apple.randomize()
        else:
            self.body.pop()

        # Move snake's head
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE

    def reset(self):
        # Reset snake attributes
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.xdir = 1
        self.ydir = 0
        self.dead = False

    def draw(self, screen):
        # Draw snake on the screen
        pygame.draw.rect(screen, "green", self.head)
        for square in self.body:
            pygame.draw.rect(screen, "green", square)

class Apple:
    def __init__(self):
        # Initialize apple attributes
        self.rect = pygame.Rect(0, 0, BLOCK_SIZE, BLOCK_SIZE)
        self.randomize()

    def randomize(self):
        # Randomize apple position
        self.rect.x = random.randint(0, SW - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        self.rect.y = random.randint(0, SH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE

    def draw(self, screen):
        # Draw apple on the screen
        pygame.draw.rect(screen, "red", self.rect)

snake = Snake()
apple = Apple()

score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # Handle key presses to change snake direction
            if event.key == pygame.K_DOWN and snake.ydir != -1:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir != 1:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir != -1:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir != 1:
                snake.ydir = 0
                snake.xdir = -1

    # Update snake and apple
    snake.update()

    # Draw game elements on the screen
    screen.fill('black')
    snake.draw(screen)
    apple.draw(screen)

    # Check for apple collision and update score
    if snake.head.colliderect(apple.rect):
        score += 1

    # Display score on the screen
    score_text = FONT.render(f"Score: {score}", True, "white")
    screen.blit(score_text, (SW // 2 - score_text.get_width() // 2, SH // 20))

    # Update display and control game speed
    pygame.display.update()
    clock.tick(10)
