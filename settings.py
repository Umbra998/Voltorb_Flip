import pygame
pygame.init()

SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (900, 800)
TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT) = (SCREEN_WIDTH//6, SCREEN_HEIGHT//6)
MARGIN = TILE_WIDTH
# variables
SQUARE = 5
game_state = 0
score = 0
# images
start_image = pygame.image.load("img/Buttons/start.png")
start_image = pygame.transform.scale(start_image, (TILE_WIDTH, TILE_HEIGHT//2))
restart_image = pygame.image.load("img/Buttons/restart.png")
restart_image = pygame.transform.scale(restart_image, (TILE_WIDTH, TILE_HEIGHT//2))
continue_image = pygame.image.load("img/Buttons/continue.png")
continue_image = pygame.transform.scale(continue_image, (TILE_WIDTH, TILE_HEIGHT//2))
edit_image = pygame.image.load("img/Buttons/edit.png")
edit_image = pygame.transform.scale(edit_image, (TILE_WIDTH, TILE_HEIGHT//2))
question_mark_img = pygame.image.load("img/Buttons/question_mark.png")
bomb_image = pygame.image.load("img/Buttons/bomb.png")
num_one_image = pygame.image.load("img/Buttons/num_one.png")
num_two_image = pygame.image.load("img/Buttons/num_two.png")
num_three_image = pygame.image.load("img/Buttons/num_three.png")

# def font
FONT_GAME_STATUS = pygame.font.SysFont('Bauhaus 93', TILE_WIDTH//4)
FONT_SCORE = pygame.font.SysFont('Bauhaus 93', int(TILE_HEIGHT/1.5))
FONT_LEVEL = pygame.font.SysFont('Bauhaus 93', int(TILE_HEIGHT/2))
# set window size
SCREEN = pygame.display.set_mode((SCREEN_WIDTH + MARGIN, SCREEN_HEIGHT))
# set title
pygame.display.set_caption("Voltorb Flip")
# enable clock (fps)
clock = pygame.time.Clock()
