import pygame
pygame.init()

SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (800, 800)
TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT) = (SCREEN_WIDTH//6, SCREEN_HEIGHT//6)
# variables
SQUARE = 5
level_number = 1
# def font
FONT_GAME_STATUS = pygame.font.SysFont('Bauhaus 93', 40)
FONT_SCORE = pygame.font.SysFont('Bauhaus 93', 30)
# set window size
SCREEN = pygame.display.set_mode(SIZE)
# set title
pygame.display.set_caption("Voltorb Flip")
# enable clock (fps)
clock = pygame.time.Clock()
