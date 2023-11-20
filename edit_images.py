import pygame
from settings import *
from draw_grid import draw_bomb_image, draw_one_image, draw_two_image, draw_three_image
from button import Button

edit_group = []

# grid buttons
question_mark_img = pygame.transform.scale(question_mark_img, (TILE_WIDTH, TILE_HEIGHT))
img = pygame.transform.scale(bomb_image, (TILE_WIDTH//2, TILE_HEIGHT//2))
bomb_button = Button(SCREEN_WIDTH, TILE_HEIGHT * 3,
                     img)
img = pygame.transform.scale(bomb_image, (TILE_WIDTH, TILE_HEIGHT))
bomb_button_full = Button(SCREEN_WIDTH, SCREEN_HEIGHT - TILE_HEIGHT * 2,
                          img)
img = pygame.transform.scale(num_one_image, (TILE_WIDTH//2, TILE_HEIGHT//2))
one_button = Button(SCREEN_WIDTH + TILE_WIDTH//2, TILE_HEIGHT * 3,
                    img)
img = pygame.transform.scale(num_two_image, (TILE_WIDTH//2, TILE_HEIGHT//2))
two_button = Button(SCREEN_WIDTH, TILE_HEIGHT * 3 + TILE_HEIGHT // 2,
                    img)
img = pygame.transform.scale(num_three_image, (TILE_WIDTH//2, TILE_HEIGHT//2))
three_button = Button(SCREEN_WIDTH + TILE_WIDTH // 2, TILE_HEIGHT * 3 + TILE_HEIGHT//2,
                      img)


def edit_image_buttons_draw(edit_num):
    if bomb_button.draw():
        edit_num = 0
    if one_button.draw():
        edit_num = 1
    if two_button.draw():
        edit_num = 2
    if three_button.draw():
        edit_num = 3
    if bomb_button_full.draw():
        edit_num = 4
    return edit_num


def create_edits():
    for y in range(0, 5):
        for x in range(0, 5):
            edit_img = EditImages(x, y)
            edit_group.append(edit_img)


def update_edit_images(level, num):
    for edit in edit_group:
        EditImages.update(edit, level, num)


def draw_images(level):
    for edit in edit_group:
        EditImages.draw(edit, level)


def clear_images(level, state):
    for edit in edit_group:
        EditImages.clear(edit, level, state)


class EditImages:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.button = Button(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, question_mark_img)
        self.image_bomb = False
        self.image_one = False
        self.image_two = False
        self.image_three = False
        self.image_bomb_full = False

    def update(self, level, num):
        if level.grid_found[self.y][self.x] == -1:
            if self.button.draw():
                if num == 0:
                    self.image_bomb = not self.image_bomb
                    if self.image_bomb is True:
                        self.image_bomb_full = False
                if num == 1:
                    self.image_one = not self.image_one
                    if self.image_one is True:
                        self.image_bomb_full = False
                if num == 2:
                    self.image_two = not self.image_two
                    if self.image_two is True:
                        self.image_bomb_full = False
                if num == 3:
                    self.image_three = not self.image_three
                    if self.image_three is True:
                        self.image_bomb_full = False
                if num == 4:
                    self.image_bomb_full = not self.image_bomb_full
                    if self.image_bomb_full is True:
                        self.image_bomb = False
                        self.image_one = False
                        self.image_two = False
                        self.image_three = False

    def draw(self, level):
        if self.image_bomb is True:
            draw_bomb_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 2, bomb_image)
        if self.image_one is True:
            draw_one_image(self.x * TILE_WIDTH + TILE_WIDTH//2, self.y * TILE_HEIGHT, 2, num_one_image)
        if self.image_two is True:
            draw_two_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT + TILE_HEIGHT//2, 2, num_two_image)
        if self.image_three is True:
            draw_three_image(self.x * TILE_WIDTH + TILE_WIDTH//2, self.y * TILE_HEIGHT + TILE_HEIGHT//2,
                             2, num_three_image)
        if self.image_bomb_full is True:
            draw_bomb_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 1, bomb_image)

    def clear(self, level, state):
        if state == 1 or level.grid_found[self.y][self.x] != -1:
            self.image_bomb = False
            self.image_one = False
            self.image_two = False
            self.image_three = False
            self.image_bomb_full = False
