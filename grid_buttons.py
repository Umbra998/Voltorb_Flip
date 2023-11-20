import pygame
from settings import *
from button import Button
from draw_grid import draw_bomb_image, draw_one_image, draw_two_image, draw_three_image, draw_question_mark_image

# grid buttons
question_mark_img = pygame.transform.scale(question_mark_img, (TILE_WIDTH, TILE_HEIGHT))

# create button group
button_group = pygame.sprite.Group()


def create_buttons():
    for y in range(0, 5):
        for x in range(0, 5):
            grid_button = GridButton(x, y)
            button_group.add(grid_button)


def update_buttons(level):
    for button in button_group:
        GridButton.update(button, level)


def reveal_buttons():
    for button in button_group:
        GridButton.reveal(button)


def reset_buttons():
    for button in button_group:
        GridButton.reset(button)


def update_button_images(level):
    for button in button_group:
        GridButton.update_images(button, level)


class GridButton(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.button_pressed = False
        self.x = x
        self.y = y
        self.button = Button(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, question_mark_img)

    def update(self, level):
        self.update_buttons(level)
        self.update_images(level)

    def update_images(self, level):
        if self.button_pressed:
            if level.grid[self.y][self.x] == 0:
                draw_bomb_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 1, bomb_image)
            elif level.grid[self.y][self.x] == 1:
                draw_one_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 1, num_one_image)
            elif level.grid[self.y][self.x] == 2:
                draw_two_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 1, num_two_image)
            elif level.grid[self.y][self.x] == 3:
                draw_three_image(self.x * TILE_WIDTH, self.y * TILE_HEIGHT, 1, num_three_image)

    def update_buttons(self, level):
        if self.button_pressed is False and self.button.draw():
            self.button_pressed = True
            level.score *= level.grid[self.y][self.x]
            if level.grid[self.y][self.x] == 0:
                level.grid_found[self.y][self.x] = 0
            elif level.grid[self.y][self.x] == 1:
                level.grid_found[self.y][self.x] = 2
            elif level.grid[self.y][self.x] == 2 or level.grid[self.y][self.x] == 3:
                level.grid_found[self.y][self.x] = 1

    def reveal(self):
        self.button_pressed = True

    def reset(self):
        self.button_pressed = False
        Button.reset(self)
