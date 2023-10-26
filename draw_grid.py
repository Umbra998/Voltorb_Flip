import pygame
from settings import *


def draw_grid():
    # draw vertical lines
    pygame.draw.line(SCREEN, 'black', (TILE_WIDTH, 0), (TILE_WIDTH, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'black', (TILE_WIDTH*2, 0), (TILE_WIDTH*2, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'black', (TILE_WIDTH*3, 0), (TILE_WIDTH*3, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'black', (TILE_WIDTH*4, 0), (TILE_WIDTH*4, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'red', (TILE_WIDTH*5, 0), (TILE_WIDTH*5, SCREEN_HEIGHT))

    # draw horizontal lines
    pygame.draw.line(SCREEN, 'black', (0, TILE_HEIGHT), (SCREEN_WIDTH, TILE_HEIGHT))
    pygame.draw.line(SCREEN, 'black', (0, TILE_HEIGHT*2), (SCREEN_WIDTH, TILE_HEIGHT*2))
    pygame.draw.line(SCREEN, 'black', (0, TILE_HEIGHT*3), (SCREEN_WIDTH, TILE_HEIGHT*3))
    pygame.draw.line(SCREEN, 'black', (0, TILE_HEIGHT*4), (SCREEN_WIDTH, TILE_HEIGHT*4))
    pygame.draw.line(SCREEN, 'red', (0, TILE_HEIGHT*5), (SCREEN_WIDTH, TILE_HEIGHT*5))
