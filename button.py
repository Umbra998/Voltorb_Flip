import pygame.mask
from settings import *


class Button:
    def __init__(self, button_x, button_y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = button_x
        self.rect.y = button_y
        self.clicked = False
        self.hiding = False

    def move(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    def draw(self):
        action = False
        if self.hiding is False:

            # get mouse position
            mouse_pos = pygame.mouse.get_pos()

            # check mouseover and clicked conditions
            if self.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                    action = True
                    self.clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # draw button
            SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def reset(self):
        self.hiding = False
