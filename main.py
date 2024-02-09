import pygame
import random

# initializing the game
pygame.init()

#set up display
WIDTH , HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mountain Top")

#colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
WHITE = (0, 255, 255)
WHITE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

#game variables
player_position = {RED: 0, GREEN: 0, BLUE: 0, YELLOW: 0}
player_colors = [RED, GREEN, BLUE, YELLOW]
current_player = 0
dice_value = 1

#main game loop
running = True
while running:
    screen.fill(WHITE)

    for eb=vent in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dice_value = random.randint(1, 6)
                player_position[player_colors[current_player]] += dice_value
                current_player = (current_player + 1) % 4


    #draw the board
    pygame.draw.rect(screen, RED, (50, 50, 500, 500))
    pygame.draw.rect(screen, WHITE, (100, 100, 400, 400))

    #draw player token
    for color, position in player_position.items():
        x = 100 + (position % 4) * 100
        y = 100 + (position // 4) * 100
        pygame.draw.circle(screen, color, (x, y), 40)


    #draw the dice value
    font = pygame.font.Font(None, 36)
    text = font.render(f"Dice: {dice_value}", True,BLACK)
    screen.blit(text, (20, 20))

    pygame.display.flip()