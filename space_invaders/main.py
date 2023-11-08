import pygame

# Initialize Pygame
pygame.init()

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Player attributes
PLAYER_COLOR = (0, 255, 0)  # Green color
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_VELOCITY = 5

# Bullet attributes
BULLET_COLOR = (255, 0, 0)  # Red color
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_VELOCITY = 15

# Enemy attributes
ENEMY_COLOR = (0, 0, 255)  # Blue color
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_VELOCITY = 2
ENEMY_DROP_STEP = 20  # The vertical distance the enemy moves down each time
ENEMY_DROP_INTERVAL = 170  # Number of horizontal moves before stepping down
ENEMY_ROWS = 3  # Number of rows of enemies
ENEMY_COLUMNS = 8  # Number of enemies per row
ENEMY_BLOCK_SPACING = WINDOW_WIDTH // 4  # Adjust this for spacing between blocks
ENEMY_BLOCK_OFFSET = ENEMY_BLOCK_SPACING // 2  # Offset to center blocks or move them as desired
ENEMY_SPACING = 10  # Spacing between enemies
ADDITIONAL_COLUMN_SPACING = 50  # Extra space after half the columns


# Frames per second
FPS = 60
clock = pygame.time.Clock()

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Simplified Space Invaders")

# Player representation
player = pygame.Rect(WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2, WINDOW_HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)

# Bullet representation
bullet = None

# Enemy representation
enemies = [
    pygame.Rect(x, 50, ENEMY_WIDTH, ENEMY_HEIGHT) for x in range(100, WINDOW_WIDTH - 100, 250)
]
enemy_direction = 1
enemy_move_count = 0

# Game variables
score = 0

# Initialize enemies with spacing between two blocks
enemies = []
for row in range(ENEMY_ROWS):
    for column in range(ENEMY_COLUMNS):
        # Calculate the basic x coordinate for enemy placement
        enemy_x = column * (ENEMY_WIDTH + ENEMY_SPACING) + ENEMY_SPACING

        # Check if we've reached the halfway point of the columns
        if column >= ENEMY_COLUMNS // 2:
            # Add additional space for all columns after the halfway point
            enemy_x += ADDITIONAL_COLUMN_SPACING

        enemy_y = row * (ENEMY_HEIGHT + ENEMY_SPACING) + ENEMY_SPACING
        enemy_rect = pygame.Rect(enemy_x, enemy_y, ENEMY_WIDTH, ENEMY_HEIGHT)
        enemies.append(enemy_rect)


# Function to draw the window, player, enemy, bullet, and score
def draw_window():
    window.fill((0, 0, 0))  # Fill the window with black color
    pygame.draw.rect(window, PLAYER_COLOR, player)  # Draw the player
    
    for enemy in enemies:  # Draw enemies
        pygame.draw.rect(window, ENEMY_COLOR, enemy)
    
    if bullet:  # Draw the bullet if it exists
        pygame.draw.rect(window, BULLET_COLOR, bullet)
    
    # Display the score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the display

# Main game loop
running = True
while running:
    clock.tick(FPS)  # Control the frame rate

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= PLAYER_VELOCITY
    if keys[pygame.K_RIGHT] and player.right < WINDOW_WIDTH:
        player.x += PLAYER_VELOCITY

    # Shooting mechanics
    if keys[pygame.K_SPACE] and bullet is None:
        bullet = pygame.Rect(player.centerx - BULLET_WIDTH // 2, player.top, BULLET_WIDTH, BULLET_HEIGHT)

    # Bullet movement
    if bullet:
        bullet.y -= BULLET_VELOCITY
        if bullet.bottom < 0:
            bullet = None

    # Enemy movement and boundary logic
    if enemies:
        for enemy in enemies:
            enemy.x += ENEMY_VELOCITY * enemy_direction
        
        enemy_move_count += 1
        if enemy_move_count >= ENEMY_DROP_INTERVAL:
            enemy_move_count = 0
            enemy_direction *= -1  # Change horizontal direction
            for enemy in enemies:
                enemy.y += ENEMY_DROP_STEP  # Move down vertically

    # Collision detection for bullets and enemies
    for enemy in enemies[:]:  # Copy of the list to avoid modification during iteration
        if bullet and enemy.colliderect(bullet):
            score += 10  # Increase the score
            enemies.remove(enemy)  # Remove the enemy that was hit
            bullet = None  # Remove the bullet
            break  # Only one enemy can be hit at a time

    # Game Over condition if any enemy reaches the bottom
    if any(enemy.bottom >= WINDOW_HEIGHT for enemy in enemies):
        print(f"Game Over! Your score is {score}.")
        running = False
    elif not enemies:  # Victory condition
        print("Victory! You've destroyed all the enemies.")
        running = False

    draw_window()  # Update the window

pygame.quit()
