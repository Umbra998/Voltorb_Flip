import pygame
pygame.init()

SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT) = (900, 800)
TILE_SIZE = (TILE_WIDTH, TILE_HEIGHT) = (SCREEN_WIDTH//6, SCREEN_HEIGHT//6)
MARGIN = TILE_WIDTH
# variables
SQUARE = 5
game_state = 0
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
