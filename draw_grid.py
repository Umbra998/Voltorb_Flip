import pygame
from settings import *


def draw_grid():
    # draw vertical lines
    pygame.draw.line(SCREEN, 'orange', (TILE_WIDTH, 0), (TILE_WIDTH, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'orange', (TILE_WIDTH*2, 0), (TILE_WIDTH*2, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'orange', (TILE_WIDTH*3, 0), (TILE_WIDTH*3, SCREEN_HEIGHT))
    pygame.draw.line(SCREEN, 'orange', (TILE_WIDTH*4, 0), (TILE_WIDTH*4, SCREEN_HEIGHT))

    # draw horizontal lines
    pygame.draw.line(SCREEN, 'orange', (0, TILE_HEIGHT), (SCREEN_WIDTH, TILE_HEIGHT))
    pygame.draw.line(SCREEN, 'orange', (0, TILE_HEIGHT*2), (SCREEN_WIDTH, TILE_HEIGHT*2))
    pygame.draw.line(SCREEN, 'orange', (0, TILE_HEIGHT*3), (SCREEN_WIDTH, TILE_HEIGHT*3))
    pygame.draw.line(SCREEN, 'orange', (0, TILE_HEIGHT*4), (SCREEN_WIDTH, TILE_HEIGHT*4))

    # draw horizontal cutoff line
    pygame.draw.line(SCREEN, 'black', (TILE_WIDTH*5, 0), (TILE_WIDTH*5, SCREEN_HEIGHT))
    # draw vertical cutoff line
    pygame.draw.line(SCREEN, 'black', (0, TILE_HEIGHT*5), (SCREEN_WIDTH, TILE_HEIGHT*5))


def draw_bomb_image(x, y):
    bomb_img = pygame.image.load("img/Buttons/bomb.png")
    bomb_img = pygame.transform.scale(bomb_img, (TILE_WIDTH, TILE_HEIGHT))
    SCREEN.blit(bomb_img, (x, y))


def draw_one_image(x, y):
    num_one_img = pygame.image.load("img/Buttons/num_one.png")
    num_one_img = pygame.transform.scale(num_one_img, (TILE_WIDTH, TILE_HEIGHT))
    SCREEN.blit(num_one_img, (x, y))


def draw_two_image(x, y):
    num_two_img = pygame.image.load("img/Buttons/num_two.png")
    num_two_img = pygame.transform.scale(num_two_img, (TILE_WIDTH, TILE_HEIGHT))
    SCREEN.blit(num_two_img, (x, y))


def draw_three_image(x, y):
    num_three_img = pygame.image.load("img/Buttons/num_three.png")
    num_three_img = pygame.transform.scale(num_three_img, (TILE_WIDTH, TILE_HEIGHT))
    SCREEN.blit(num_three_img, (x, y))
