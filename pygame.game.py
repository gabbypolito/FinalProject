import pygame
import random
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Albert the Gator vs the Seminole Arrows")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont("arial", 36)

clock = pygame.time.Clock()
FPS = 60

albert_width, albert_height = 60, 60
albert_x = 100
albert_y = HEIGHT // 2
albert_speed = 4

seminole_arrow_width, seminole_arrow_height = 10, 40
seminole_arrow_speed = 8
seminole_arrows = []

score = 0

MAIN_MENU = 0
PLAYING = 1
GAME_OVER = 2
game_state = MAIN_MENU


def draw_albert_the_gator(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, albert_width, albert_height))


def draw_seminole_arrow(x, y):
    pygame.draw.rect(screen, RED, (x, y, seminole_arrow_width, seminole_arrow_height))


def display_text(text, size, color, x, y):
    font_obj = pygame.font.SysFont("arial", size)
    text_surface = font_obj.render(text, True, color)
    screen.blit(text_surface, (x, y))


def reset_game():
    global seminole_arrows, score, albert_x, game_state
    seminole_arrows = []
    score = 0
    albert_x = 100
    albert_y = WIDTH // 2
    game_state = PLAYING

running = True
while running:
    screen.fill(WHITE)
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if game_state == MAIN_MENU:
        display_text("Albert Dodge", 50, BLACK, 270, 200)
        display_text("Press SPACE to Start", 30, BLACK, 260, 300)
        if keys[pygame.K_SPACE]:
            reset_game()

    elif game_state == PLAYING:

        if keys[pygame.K_UP] and albert_y > 0:
            albert_y -= albert_speed
        if keys[pygame.K_DOWN] and albert_y < HEIGHT - albert_height:
            albert_y += albert_speed
        if keys[pygame.K_RIGHT] and albert_x < WIDTH - albert_width:
            albert_x += albert_speed


        if random.randint(1, 25) == 1:
            arrow_y = random.randint(0, HEIGHT - seminole_arrow_height)
            seminole_arrows.append([WIDTH, arrow_y])




