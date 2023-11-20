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


def draw_bomb_image(x, y, state, img):
    if state == 1:
        img = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    elif state == 2:
        img = pygame.transform.scale(img, (TILE_WIDTH//2, TILE_HEIGHT//2))
    SCREEN.blit(img, (x, y))


def draw_one_image(x, y, state, img):
    if state == 1:
        img = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    elif state == 2:
        img = pygame.transform.scale(img, (TILE_WIDTH//2, TILE_HEIGHT//2))
    SCREEN.blit(img, (x, y))


def draw_two_image(x, y, state, img):
    if state == 1:
        img = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    elif state == 2:
        img = pygame.transform.scale(img, (TILE_WIDTH//2, TILE_HEIGHT//2))
    SCREEN.blit(img, (x, y))


def draw_three_image(x, y, state, img):
    if state == 1:
        img = pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    elif state == 2:
        img = pygame.transform.scale(img, (TILE_WIDTH//2, TILE_HEIGHT//2))
    SCREEN.blit(img, (x, y))


def draw_question_mark_image(x, y, img):
    pygame.transform.scale(img, (TILE_WIDTH, TILE_HEIGHT))
    SCREEN.blit(img, (x, y))


def draw_hitbox(num):
    if num == 0:
        pygame.draw.rect(SCREEN, 'red',
                         (SCREEN_WIDTH, TILE_HEIGHT * 3,
                          TILE_WIDTH//2, TILE_HEIGHT//2), 1)
    if num == 1:
        pygame.draw.rect(SCREEN, 'blue',
                         (SCREEN_WIDTH + TILE_WIDTH//2, TILE_HEIGHT * 3,
                          TILE_WIDTH//2, TILE_HEIGHT//2), 1)
    if num == 2:
        pygame.draw.rect(SCREEN, 'blue',
                         (SCREEN_WIDTH, TILE_HEIGHT * 3 + TILE_HEIGHT // 2,
                          TILE_WIDTH//2, TILE_HEIGHT//2), 1)
    if num == 3:
        pygame.draw.rect(SCREEN, 'blue',
                         (SCREEN_WIDTH + TILE_WIDTH // 2, TILE_HEIGHT * 3 + TILE_HEIGHT//2,
                          TILE_WIDTH//2, TILE_HEIGHT//2), 1)
    if num == 4:
        pygame.draw.rect(SCREEN, 'red',
                         (SCREEN_WIDTH, SCREEN_HEIGHT - TILE_HEIGHT * 2,
                          TILE_WIDTH, TILE_HEIGHT), 1)
