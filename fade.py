import pygame
from settings import *


def fade(width, height):
    fade_screen = pygame.Surface((width, height))
    fade_screen.fill('black')
    for alpha in range(0, 100):
        fade_screen.set_alpha(alpha)
        SCREEN.blit(fade_screen, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)
