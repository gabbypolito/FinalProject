import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Albert the Gator vs the Seminole Arrows")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.SysFont("arial", 36)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Albert settings
albert_width, albert_height = 60, 60
albert_x = WIDTH // 2
albert_y = HEIGHT - albert_height - 10
albert_speed = 7

# Seminole Arrow settings
seminole_arrow_width, seminole_arrow_height = 10, 40
seminole_arrow_speed = 8
seminole_arrows = []

# Score
score = 0

# Game States
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
    albert_x = WIDTH // 2
    game_state = PLAYING


