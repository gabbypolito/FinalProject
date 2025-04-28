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
GREEN = (0, 255, 0)

font = pygame.font.SysFont("arial", 36)

clock = pygame.time.Clock()
FPS = 60

albert_width, albert_height = 60, 60    #
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
GAME_WIN = 3


# Need to load the imaged before the loop instead of in the classes, otherwise the game becomes glitchy
gator_image = pygame.image.load('florida-gators-2-logo-png-transparent.png').convert_alpha()
gator_image = pygame.transform.scale(gator_image, (100,100))
seminole_arrow_image = pygame.image.load('arrows-2-logo-png-transparent.png').convert_alpha()
seminole_arrow_image = pygame.transform.scale(seminole_arrow_image, (80,60))
finishline_image = pygame.image.load('finish_line.png').convert_alpha()
finishline_image = pygame.transform.scale(finishline_image, (40,800))

def draw_albert_the_gator(x, y):
    screen.blit(gator_image, (x, y))


def draw_seminole_arrow(x, y):
    screen.blit(seminole_arrow_image, (x, y))


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

finish_line_rect = pygame.Rect(760, 0, 40, 800)
def draw_finish_line():
    screen.blit(finishline_image, finish_line_rect.topleft)


running = True
while running:
    screen.fill(WHITE)
    draw_finish_line()
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

        new_arrows = []
        for arrow in seminole_arrows:
            arrow[0] -= seminole_arrow_speed
            if arrow[0] + seminole_arrow_width < 0:
                score += 1
            else:
                new_arrows.append(arrow)
        seminole_arrows = new_arrows

        draw_albert_the_gator(albert_x, albert_y)
        for arrow in seminole_arrows:
            draw_seminole_arrow(arrow[0], arrow[1])

        display_text(f"Score: {score}", 28, BLACK, 10, 10)

        albert_rect = pygame.Rect(albert_x, albert_y, albert_width, albert_height)
        for arrow in seminole_arrows:
            if isinstance(arrow[0], (int, float)) and isinstance(arrow[1], (int, float)):
                arrow_rect = pygame.Rect(arrow[0], arrow[1], seminole_arrow_width, seminole_arrow_height)

                if albert_rect.colliderect(arrow_rect):
                    game_state = GAME_OVER
                elif albert_rect.colliderect(finish_line_rect):
                    game_state = GAME_WIN
            else:
                print("Invalid arrow data:", arrow)

    elif game_state == GAME_OVER:
        display_text("Game Over", 50, RED, 280, 220)
        display_text(f"Final Score: {score}", 32, BLACK, 290, 300)
        display_text("Press SPACE to return to Menu", 24, BLACK, 240, 370)
        if keys[pygame.K_SPACE]:
            game_state = MAIN_MENU
    elif game_state == GAME_WIN:
        display_text("YOU SAVED ALBERTA!", 50, GREEN, 280, 220)
        display_text("Press SPACE to return to Menu", 24, BLACK, 240, 370)


    pygame.display.flip()
    clock.tick(FPS)





