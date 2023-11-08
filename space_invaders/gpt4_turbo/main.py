import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
PLAYER_SIZE = 50
BULLET_SIZE = 5
ENEMY_SIZE = 50
PLAYER_COLOR = (0, 255, 0)
BULLET_COLOR = (255, 255, 0)
ENEMY_COLOR = (255, 0, 0)
ENEMY_POINTS = 100

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

# Load font
font = pygame.font.SysFont(None, 36)

# Player class
class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - PLAYER_SIZE
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.color = PLAYER_COLOR
        self.speed = 5
        self.bullet = None

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if direction == 'LEFT':
            self.x -= self.speed
        elif direction == 'RIGHT':
            self.x += self.speed

        # Keep the player within screen bounds
        self.x = max(self.x, 0)
        self.x = min(self.x, SCREEN_WIDTH - self.width)

    def shoot(self):
        if not self.bullet:
            self.bullet = Bullet(self.x + self.width // 2, self.y)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BULLET_SIZE
        self.height = BULLET_SIZE
        self.color = BULLET_COLOR
        self.speed = 10

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y -= self.speed

# Enemy class
class Enemy:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = ENEMY_SIZE
        self.width = ENEMY_SIZE
        self.height = ENEMY_SIZE
        self.color = ENEMY_COLOR
        self.speed = 2
        self.direction = 1  # 1 for right, -1 for left
        self.alive = True

    def draw(self, surface):
        if self.alive:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.alive:
            self.x += self.speed * self.direction
            # Change direction if enemy reaches the edge of the screen
            if self.x <= 0 or self.x >= SCREEN_WIDTH - self.width:
                self.direction *= -1
                self.y += self.height  # Move the enemy down each time it changes direction

# Game loop
def game_loop():
    player = Player()
    enemy = Enemy()
    clock = pygame.time.Clock()
    score = 0
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move('LEFT')
            if keys[pygame.K_RIGHT]:
                player.move('RIGHT')
            if keys[pygame.K_SPACE] and not player.bullet:
                player.shoot()

            screen.fill((0, 0, 0))  # Clear the screen

            # Update the player
            player.draw(screen)
            if player.bullet:
                player.bullet.move()
                player.bullet.draw(screen)
                if player.bullet.y < 0:  # Bullet has gone off screen
                    player.bullet = None
                # Check for collision with enemy
                elif enemy.alive and enemy.x < player.bullet.x < enemy.x + enemy.width and \
                        enemy.y < player.bullet.y < enemy.y + enemy.height:
                    enemy.alive = False  # Enemy is hit
                    player.bullet = None  # Remove the bullet
                    score += ENEMY_POINTS  # Increase the score

            # Update the enemy
            enemy.move()
            enemy.draw(screen)

            # Check for game over conditions
            if not enemy.alive or enemy.y >= SCREEN_HEIGHT - enemy.height:
                game_over = True

            # Display the score
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))
        else:
            # Game over display
            game_over_text = font.render('Game Over', True, (255, 255, 255))
            final_score_text = font.render(f'Final Score: {score}', True, (255, 255, 255))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - game_over_text.get_height() // 2))
            screen.blit(final_score_text, (SCREEN_WIDTH // 2 - final_score_text.get_width() // 2, SCREEN_HEIGHT // 2 + final_score_text.get_height()))

        pygame.display.flip()  # Update the full display
        clock.tick(60)  # Maintain 60 FPS

# Start the game
game_loop()
