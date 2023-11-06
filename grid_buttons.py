import pygame
from settings import *
from button import Button
from draw_grid import draw_bomb_image, draw_one_image, draw_two_image, draw_three_image

# grid buttons
question_mark_img = pygame.transform.scale(question_mark_img, (TILE_WIDTH, TILE_HEIGHT))
null_null_button = Button(0, 0, question_mark_img)
null_one_button = Button(TILE_WIDTH, 0, question_mark_img)
null_two_button = Button(TILE_WIDTH*2, 0, question_mark_img)
null_three_button = Button(TILE_WIDTH*3, 0, question_mark_img)
null_four_button = Button(TILE_WIDTH*4, 0, question_mark_img)
one_null_button = Button(0, TILE_HEIGHT, question_mark_img)
one_one_button = Button(TILE_WIDTH, TILE_HEIGHT, question_mark_img)
one_two_button = Button(TILE_WIDTH*2, TILE_HEIGHT, question_mark_img)
one_three_button = Button(TILE_WIDTH*3, TILE_HEIGHT, question_mark_img)
one_four_button = Button(TILE_WIDTH*4, TILE_HEIGHT, question_mark_img)
two_null_button = Button(0, TILE_HEIGHT*2, question_mark_img)
two_one_button = Button(TILE_WIDTH, TILE_HEIGHT*2, question_mark_img)
two_two_button = Button(TILE_WIDTH*2, TILE_HEIGHT*2, question_mark_img)
two_three_button = Button(TILE_WIDTH*3, TILE_HEIGHT*2, question_mark_img)
two_four_button = Button(TILE_WIDTH*4, TILE_HEIGHT*2, question_mark_img)
three_null_button = Button(0, TILE_HEIGHT*3, question_mark_img)
three_one_button = Button(TILE_WIDTH, TILE_HEIGHT*3, question_mark_img)
three_two_button = Button(TILE_WIDTH*2, TILE_HEIGHT*3, question_mark_img)
three_three_button = Button(TILE_WIDTH*3, TILE_HEIGHT*3, question_mark_img)
three_four_button = Button(TILE_WIDTH*4, TILE_HEIGHT*3, question_mark_img)
four_null_button = Button(0, TILE_HEIGHT*4, question_mark_img)
four_one_button = Button(TILE_WIDTH, TILE_HEIGHT*4, question_mark_img)
four_two_button = Button(TILE_WIDTH*2, TILE_HEIGHT*4, question_mark_img)
four_three_button = Button(TILE_WIDTH*3, TILE_HEIGHT*4, question_mark_img)
four_four_button = Button(TILE_WIDTH*4, TILE_HEIGHT*4, question_mark_img)


class GridButtons:
    def __init__(self):
        # button pressed
        self.null_null_button_pressed = False
        self.null_one_button_pressed = False
        self.null_two_button_pressed = False
        self.null_three_button_pressed = False
        self.null_four_button_pressed = False
        self.one_null_button_pressed = False
        self.one_one_button_pressed = False
        self.one_two_button_pressed = False
        self.one_three_button_pressed = False
        self.one_four_button_pressed = False
        self.two_null_button_pressed = False
        self.two_one_button_pressed = False
        self.two_two_button_pressed = False
        self.two_three_button_pressed = False
        self.two_four_button_pressed = False
        self.three_null_button_pressed = False
        self.three_one_button_pressed = False
        self.three_two_button_pressed = False
        self.three_three_button_pressed = False
        self.three_four_button_pressed = False
        self.four_null_button_pressed = False
        self.four_one_button_pressed = False
        self.four_two_button_pressed = False
        self.four_three_button_pressed = False
        self.four_four_button_pressed = False

    def update(self, level):
        self.update_buttons(level)
        self.update_images(level)

    def update_images(self, level):
        if self.null_null_button_pressed:
            if level.grid[0][0] == 0:
                draw_bomb_image(0, 0)
            elif level.grid[0][0] == 1:
                draw_one_image(0, 0)
            elif level.grid[0][0] == 2:
                draw_two_image(0, 0)
            elif level.grid[0][0] == 3:
                draw_three_image(0, 0)
        if self.null_one_button_pressed:
            if level.grid[0][1] == 0:
                draw_bomb_image(TILE_WIDTH, 0)
            elif level.grid[0][1] == 1:
                draw_one_image(TILE_WIDTH, 0)
            elif level.grid[0][1] == 2:
                draw_two_image(TILE_WIDTH, 0)
            elif level.grid[0][1] == 3:
                draw_three_image(TILE_WIDTH, 0)
        if self.null_two_button_pressed:
            if level.grid[0][2] == 0:
                draw_bomb_image(TILE_WIDTH * 2, 0)
            elif level.grid[0][2] == 1:
                draw_one_image(TILE_WIDTH * 2, 0)
            elif level.grid[0][2] == 2:
                draw_two_image(TILE_WIDTH * 2, 0)
            elif level.grid[0][2] == 3:
                draw_three_image(TILE_WIDTH * 2, 0)
        if self.null_three_button_pressed:
            if level.grid[0][3] == 0:
                draw_bomb_image(TILE_WIDTH * 3, 0)
            elif level.grid[0][3] == 1:
                draw_one_image(TILE_WIDTH * 3, 0)
            elif level.grid[0][3] == 2:
                draw_two_image(TILE_WIDTH * 3, 0)
            elif level.grid[0][3] == 3:
                draw_three_image(TILE_WIDTH * 3, 0)
        if self.null_four_button_pressed:
            if level.grid[0][4] == 0:
                draw_bomb_image(TILE_WIDTH * 4, 0)
            elif level.grid[0][4] == 1:
                draw_one_image(TILE_WIDTH * 4, 0)
            elif level.grid[0][4] == 2:
                draw_two_image(TILE_WIDTH * 4, 0)
            elif level.grid[0][4] == 3:
                draw_three_image(TILE_WIDTH * 4, 0)
        if self.one_null_button_pressed:
            if level.grid[1][0] == 0:
                draw_bomb_image(0, TILE_HEIGHT)
            elif level.grid[1][0] == 1:
                draw_one_image(0, TILE_HEIGHT)
            elif level.grid[1][0] == 2:
                draw_two_image(0, TILE_HEIGHT)
            elif level.grid[1][0] == 3:
                draw_three_image(0, TILE_HEIGHT)
        if self.one_one_button_pressed:
            if level.grid[1][1] == 0:
                draw_bomb_image(TILE_WIDTH, TILE_HEIGHT)
            elif level.grid[1][1] == 1:
                draw_one_image(TILE_WIDTH, TILE_HEIGHT)
            elif level.grid[1][1] == 2:
                draw_two_image(TILE_WIDTH, TILE_HEIGHT)
            elif level.grid[1][1] == 3:
                draw_three_image(TILE_WIDTH, TILE_HEIGHT)
        if self.one_two_button_pressed:
            if level.grid[1][2] == 0:
                draw_bomb_image(TILE_WIDTH * 2, TILE_HEIGHT)
            elif level.grid[1][2] == 1:
                draw_one_image(TILE_WIDTH * 2, TILE_HEIGHT)
            elif level.grid[1][2] == 2:
                draw_two_image(TILE_WIDTH * 2, TILE_HEIGHT)
            elif level.grid[1][2] == 3:
                draw_three_image(TILE_WIDTH * 2, TILE_HEIGHT)
        if self.one_three_button_pressed:
            if level.grid[1][3] == 0:
                draw_bomb_image(TILE_WIDTH * 3, TILE_HEIGHT)
            elif level.grid[1][3] == 1:
                draw_one_image(TILE_WIDTH * 3, TILE_HEIGHT)
            elif level.grid[1][3] == 2:
                draw_two_image(TILE_WIDTH * 3, TILE_HEIGHT)
            elif level.grid[1][3] == 3:
                draw_three_image(TILE_WIDTH * 3, TILE_HEIGHT)
        if self.one_four_button_pressed:
            if level.grid[1][4] == 0:
                draw_bomb_image(TILE_WIDTH * 4, TILE_HEIGHT)
            elif level.grid[1][4] == 1:
                draw_one_image(TILE_WIDTH * 4, TILE_HEIGHT)
            elif level.grid[1][4] == 2:
                draw_two_image(TILE_WIDTH * 4, TILE_HEIGHT)
            elif level.grid[1][4] == 3:
                draw_three_image(TILE_WIDTH * 4, TILE_HEIGHT)
        if self.two_null_button_pressed:
            if level.grid[2][0] == 0:
                draw_bomb_image(0, TILE_HEIGHT * 2)
            elif level.grid[2][0] == 1:
                draw_one_image(0, TILE_HEIGHT * 2)
            elif level.grid[2][0] == 2:
                draw_two_image(0, TILE_HEIGHT * 2)
            elif level.grid[2][0] == 3:
                draw_three_image(0, TILE_HEIGHT * 2)
        if self.two_one_button_pressed:
            if level.grid[2][1] == 0:
                draw_bomb_image(TILE_WIDTH, TILE_HEIGHT * 2)
            elif level.grid[2][1] == 1:
                draw_one_image(TILE_WIDTH, TILE_HEIGHT * 2)
            elif level.grid[2][1] == 2:
                draw_two_image(TILE_WIDTH, TILE_HEIGHT * 2)
            elif level.grid[2][1] == 3:
                draw_three_image(TILE_WIDTH, TILE_HEIGHT * 2)
        if self.two_two_button_pressed:
            if level.grid[2][2] == 0:
                draw_bomb_image(TILE_WIDTH * 2, TILE_HEIGHT * 2)
            elif level.grid[2][2] == 1:
                draw_one_image(TILE_WIDTH * 2, TILE_HEIGHT * 2)
            elif level.grid[2][2] == 2:
                draw_two_image(TILE_WIDTH * 2, TILE_HEIGHT * 2)
            elif level.grid[2][2] == 3:
                draw_three_image(TILE_WIDTH * 2, TILE_HEIGHT * 2)
        if self.two_three_button_pressed:
            if level.grid[2][3] == 0:
                draw_bomb_image(TILE_WIDTH * 3, TILE_HEIGHT * 2)
            elif level.grid[2][3] == 1:
                draw_one_image(TILE_WIDTH * 3, TILE_HEIGHT * 2)
            elif level.grid[2][3] == 2:
                draw_two_image(TILE_WIDTH * 3, TILE_HEIGHT * 2)
            elif level.grid[2][3] == 3:
                draw_three_image(TILE_WIDTH * 3, TILE_HEIGHT * 2)
        if self.two_four_button_pressed:
            if level.grid[2][4] == 0:
                draw_bomb_image(TILE_WIDTH * 4, TILE_HEIGHT * 2)
            elif level.grid[2][4] == 1:
                draw_one_image(TILE_WIDTH * 4, TILE_HEIGHT * 2)
            elif level.grid[2][4] == 2:
                draw_two_image(TILE_WIDTH * 4, TILE_HEIGHT * 2)
            elif level.grid[2][4] == 3:
                draw_three_image(TILE_WIDTH * 4, TILE_HEIGHT * 2)
        if self.three_null_button_pressed:
            if level.grid[3][0] == 0:
                draw_bomb_image(0, TILE_HEIGHT * 3)
            elif level.grid[3][0] == 1:
                draw_one_image(0, TILE_HEIGHT * 3)
            elif level.grid[3][0] == 2:
                draw_two_image(0, TILE_HEIGHT * 3)
            elif level.grid[3][0] == 3:
                draw_three_image(0, TILE_HEIGHT * 3)
        if self.three_one_button_pressed:
            if level.grid[3][1] == 0:
                draw_bomb_image(TILE_WIDTH, TILE_HEIGHT * 3)
            elif level.grid[3][1] == 1:
                draw_one_image(TILE_WIDTH, TILE_HEIGHT * 3)
            elif level.grid[3][1] == 2:
                draw_two_image(TILE_WIDTH, TILE_HEIGHT * 3)
            elif level.grid[3][1] == 3:
                draw_three_image(TILE_WIDTH, TILE_HEIGHT * 3)
        if self.three_two_button_pressed:
            if level.grid[3][2] == 0:
                draw_bomb_image(TILE_WIDTH * 2, TILE_HEIGHT * 3)
            elif level.grid[3][2] == 1:
                draw_one_image(TILE_WIDTH * 2, TILE_HEIGHT * 3)
            elif level.grid[3][2] == 2:
                draw_two_image(TILE_WIDTH * 2, TILE_HEIGHT * 3)
            elif level.grid[3][2] == 3:
                draw_three_image(TILE_WIDTH * 2, TILE_HEIGHT * 3)
        if self.three_three_button_pressed:
            if level.grid[3][3] == 0:
                draw_bomb_image(TILE_WIDTH * 3, TILE_HEIGHT * 3)
            elif level.grid[3][3] == 1:
                draw_one_image(TILE_WIDTH * 3, TILE_HEIGHT * 3)
            elif level.grid[3][3] == 2:
                draw_two_image(TILE_WIDTH * 3, TILE_HEIGHT * 3)
            elif level.grid[3][3] == 3:
                draw_three_image(TILE_WIDTH * 3, TILE_HEIGHT * 3)
        if self.three_four_button_pressed:
            if level.grid[3][4] == 0:
                draw_bomb_image(TILE_WIDTH * 4, TILE_HEIGHT * 3)
            elif level.grid[3][4] == 1:
                draw_one_image(TILE_WIDTH * 4, TILE_HEIGHT * 3)
            elif level.grid[3][4] == 2:
                draw_two_image(TILE_WIDTH * 4, TILE_HEIGHT * 3)
            elif level.grid[3][4] == 3:
                draw_three_image(TILE_WIDTH * 4, TILE_HEIGHT * 3)
        if self.four_null_button_pressed:
            if level.grid[4][0] == 0:
                draw_bomb_image(0, TILE_HEIGHT * 4)
            elif level.grid[4][0] == 1:
                draw_one_image(0, TILE_HEIGHT * 4)
            elif level.grid[4][0] == 2:
                draw_two_image(0, TILE_HEIGHT * 4)
            elif level.grid[4][0] == 3:
                draw_three_image(0, TILE_HEIGHT * 4)
        if self.four_one_button_pressed:
            if level.grid[4][1] == 0:
                draw_bomb_image(TILE_WIDTH, TILE_HEIGHT * 4)
            elif level.grid[4][1] == 1:
                draw_one_image(TILE_WIDTH, TILE_HEIGHT * 4)
            elif level.grid[4][1] == 2:
                draw_two_image(TILE_WIDTH, TILE_HEIGHT * 4)
            elif level.grid[4][1] == 3:
                draw_three_image(TILE_WIDTH, TILE_HEIGHT * 4)
        if self.four_two_button_pressed:
            if level.grid[4][2] == 0:
                draw_bomb_image(TILE_WIDTH * 2, TILE_HEIGHT * 4)
            elif level.grid[4][2] == 1:
                draw_one_image(TILE_WIDTH * 2, TILE_HEIGHT * 4)
            elif level.grid[4][2] == 2:
                draw_two_image(TILE_WIDTH * 2, TILE_HEIGHT * 4)
            elif level.grid[4][2] == 3:
                draw_three_image(TILE_WIDTH * 2, TILE_HEIGHT * 4)
        if self.four_three_button_pressed:
            if level.grid[4][3] == 0:
                draw_bomb_image(TILE_WIDTH * 3, TILE_HEIGHT * 4)
            elif level.grid[4][3] == 1:
                draw_one_image(TILE_WIDTH * 3, TILE_HEIGHT * 4)
            elif level.grid[4][3] == 2:
                draw_two_image(TILE_WIDTH * 3, TILE_HEIGHT * 4)
            elif level.grid[4][3] == 3:
                draw_three_image(TILE_WIDTH * 3, TILE_HEIGHT * 4)
        if self.four_four_button_pressed:
            if level.grid[4][4] == 0:
                draw_bomb_image(TILE_WIDTH * 4, TILE_HEIGHT * 4)
            elif level.grid[4][4] == 1:
                draw_one_image(TILE_WIDTH * 4, TILE_HEIGHT * 4)
            elif level.grid[4][4] == 2:
                draw_two_image(TILE_WIDTH * 4, TILE_HEIGHT * 4)
            elif level.grid[4][4] == 3:
                draw_three_image(TILE_WIDTH * 4, TILE_HEIGHT * 4)

    def update_buttons(self, level):
        if self.null_null_button_pressed is False and null_null_button.draw():
            self.null_null_button_pressed = True
            level.score *= level.grid[0][0]
            if level.grid[0][0] == 0:
                level.grid_found[0][0] = 0
            elif level.grid[0][0] == 2 or level.grid[0][0] == 3:
                level.grid_found[0][0] = 1
        if self.null_one_button_pressed is False and null_one_button.draw():
            self.null_one_button_pressed = True
            level.score *= level.grid[0][1]
            if level.grid[0][1] == 0:
                level.grid_found[0][1] = 0
            elif level.grid[0][1] == 2 or level.grid[0][1] == 3:
                level.grid_found[0][1] = 1
        if self.null_two_button_pressed is False and null_two_button.draw():
            self.null_two_button_pressed = True
            level.score *= level.grid[0][2]
            if level.grid[0][2] == 0:
                level.grid_found[0][2] = 0
            elif level.grid[0][2] == 2 or level.grid[0][2] == 3:
                level.grid_found[0][2] = 1
        if self.null_three_button_pressed is False and null_three_button.draw():
            self.null_three_button_pressed = True
            level.score *= level.grid[0][3]
            if level.grid[0][3] == 0:
                level.grid_found[0][3] = 0
            elif level.grid[0][3] == 2 or level.grid[0][3] == 3:
                level.grid_found[0][3] = 1
        if self.null_four_button_pressed is False and null_four_button.draw():
            self.null_four_button_pressed = True
            level.score *= level.grid[0][4]
            if level.grid[0][4] == 0:
                level.grid_found[0][4] = 0
            elif level.grid[0][4] == 2 or level.grid[0][4] == 3:
                level.grid_found[0][4] = 1
        if self.one_null_button_pressed is False and one_null_button.draw():
            self.one_null_button_pressed = True
            level.score *= level.grid[1][0]
            if level.grid[1][0] == 0:
                level.grid_found[1][0] = 0
            elif level.grid[1][0] == 2 or level.grid[1][0] == 3:
                level.grid_found[1][0] = 1
        if self.one_one_button_pressed is False and one_one_button.draw():
            self.one_one_button_pressed = True
            level.score *= level.grid[1][1]
            if level.grid[1][1] == 0:
                level.grid_found[1][1] = 0
            elif level.grid[1][1] == 2 or level.grid[1][1] == 3:
                level.grid_found[1][1] = 1
        if self.one_two_button_pressed is False and one_two_button.draw():
            self.one_two_button_pressed = True
            level.score *= level.grid[1][2]
            if level.grid[1][2] == 0:
                level.grid_found[1][2] = 0
            elif level.grid[1][2] == 2 or level.grid[1][2] == 3:
                level.grid_found[1][2] = 1
        if self.one_three_button_pressed is False and one_three_button.draw():
            self.one_three_button_pressed = True
            level.score *= level.grid[1][3]
            if level.grid[1][3] == 0:
                level.grid_found[1][3] = 0
            elif level.grid[1][3] == 2 or level.grid[1][3] == 3:
                level.grid_found[1][3] = 1
        if self.one_four_button_pressed is False and one_four_button.draw():
            self.one_four_button_pressed = True
            level.score *= level.grid[1][4]
            if level.grid[1][4] == 0:
                level.grid_found[1][4] = 0
            elif level.grid[1][4] == 2 or level.grid[1][4] == 3:
                level.grid_found[1][4] = 1
        if self.two_null_button_pressed is False and two_null_button.draw():
            self.two_null_button_pressed = True
            level.score *= level.grid[2][0]
            if level.grid[2][0] == 0:
                level.grid_found[2][0] = 0
            elif level.grid[2][0] == 2 or level.grid[2][0] == 3:
                level.grid_found[2][0] = 1
        if self.two_one_button_pressed is False and two_one_button.draw():
            self.two_one_button_pressed = True
            level.score *= level.grid[2][1]
            if level.grid[2][1] == 0:
                level.grid_found[2][1] = 0
            elif level.grid[2][1] == 2 or level.grid[2][1] == 3:
                level.grid_found[2][1] = 1
        if self.two_two_button_pressed is False and two_two_button.draw():
            self.two_two_button_pressed = True
            level.score *= level.grid[2][2]
            if level.grid[2][2] == 0:
                level.grid_found[2][2] = 0
            elif level.grid[2][2] == 2 or level.grid[2][2] == 3:
                level.grid_found[2][2] = 1
        if self.two_three_button_pressed is False and two_three_button.draw():
            self.two_three_button_pressed = True
            level.score *= level.grid[2][3]
            if level.grid[2][3] == 0:
                level.grid_found[2][3] = 0
            elif level.grid[2][3] == 2 or level.grid[2][3] == 3:
                level.grid_found[2][3] = 1
        if self.two_four_button_pressed is False and two_four_button.draw():
            self.two_four_button_pressed = True
            level.score *= level.grid[2][4]
            if level.grid[2][4] == 0:
                level.grid_found[2][4] = 0
            elif level.grid[2][4] == 2 or level.grid[2][4] == 3:
                level.grid_found[2][4] = 1
        if self.three_null_button_pressed is False and three_null_button.draw():
            self.three_null_button_pressed = True
            level.score *= level.grid[3][0]
            if level.grid[3][0] == 0:
                level.grid_found[3][0] = 0
            elif level.grid[3][0] == 2 or level.grid[3][0] == 3:
                level.grid_found[3][0] = 1
        if self.three_one_button_pressed is False and three_one_button.draw():
            self.three_one_button_pressed = True
            level.score *= level.grid[3][1]
            if level.grid[3][1] == 0:
                level.grid_found[3][1] = 0
            elif level.grid[3][1] == 2 or level.grid[3][1] == 3:
                level.grid_found[3][1] = 1
        if self.three_two_button_pressed is False and three_two_button.draw():
            self.three_two_button_pressed = True
            level.score *= level.grid[3][2]
            if level.grid[3][2] == 0:
                level.grid_found[3][2] = 0
            elif level.grid[3][2] == 2 or level.grid[3][2] == 3:
                level.grid_found[3][2] = 1
        if self.three_three_button_pressed is False and three_three_button.draw():
            self.three_three_button_pressed = True
            level.score *= level.grid[3][3]
            if level.grid[3][3] == 0:
                level.grid_found[3][3] = 0
            elif level.grid[3][3] == 2 or level.grid[3][3] == 3:
                level.grid_found[3][3] = 1
        if self.three_four_button_pressed is False and three_four_button.draw():
            self.three_four_button_pressed = True
            level.score *= level.grid[3][4]
            if level.grid[3][4] == 0:
                level.grid_found[3][4] = 0
            elif level.grid[3][4] == 2 or level.grid[3][4] == 3:
                level.grid_found[3][4] = 1
        if self.four_null_button_pressed is False and four_null_button.draw():
            self.four_null_button_pressed = True
            level.score *= level.grid[4][0]
            if level.grid[4][0] == 0:
                level.grid_found[4][0] = 0
            elif level.grid[4][0] == 2 or level.grid[4][0] == 3:
                level.grid_found[4][0] = 1
        if self.four_one_button_pressed is False and four_one_button.draw():
            self.four_one_button_pressed = True
            level.score *= level.grid[4][1]
            if level.grid[4][1] == 0:
                level.grid_found[4][1] = 0
            elif level.grid[4][1] == 2 or level.grid[4][1] == 3:
                level.grid_found[4][1] = 1
        if self.four_two_button_pressed is False and four_two_button.draw():
            self.four_two_button_pressed = True
            level.score *= level.grid[4][2]
            if level.grid[4][2] == 0:
                level.grid_found[4][2] = 0
            elif level.grid[4][2] == 2 or level.grid[4][2] == 3:
                level.grid_found[4][2] = 1
        if self.four_three_button_pressed is False and four_three_button.draw():
            self.four_three_button_pressed = True
            level.score *= level.grid[4][3]
            if level.grid[4][3] == 0:
                level.grid_found[4][3] = 0
            elif level.grid[4][3] == 2 or level.grid[4][3] == 3:
                level.grid_found[4][3] = 1
        if self.four_four_button_pressed is False and four_four_button.draw():
            self.four_four_button_pressed = True
            level.score *= level.grid[4][4]
            if level.grid[4][4] == 0:
                level.grid_found[4][4] = 0
            elif level.grid[4][4] == 2 or level.grid[4][4] == 3:
                level.grid_found[4][4] = 1

    def reveal(self):
        self.null_null_button_pressed = True
        self.null_one_button_pressed = True
        self.null_two_button_pressed = True
        self.null_three_button_pressed = True
        self.null_four_button_pressed = True
        self.one_null_button_pressed = True
        self.one_one_button_pressed = True
        self.one_two_button_pressed = True
        self.one_three_button_pressed = True
        self.one_four_button_pressed = True
        self.two_null_button_pressed = True
        self.two_one_button_pressed = True
        self.two_two_button_pressed = True
        self.two_three_button_pressed = True
        self.two_four_button_pressed = True
        self.three_null_button_pressed = True
        self.three_one_button_pressed = True
        self.three_two_button_pressed = True
        self.three_three_button_pressed = True
        self.three_four_button_pressed = True
        self.four_null_button_pressed = True
        self.four_one_button_pressed = True
        self.four_two_button_pressed = True
        self.four_three_button_pressed = True
        self.four_four_button_pressed = True

    def reset(self):
        self.null_null_button_pressed = False
        self.null_one_button_pressed = False
        self.null_two_button_pressed = False
        self.null_three_button_pressed = False
        self.null_four_button_pressed = False
        self.one_null_button_pressed = False
        self.one_one_button_pressed = False
        self.one_two_button_pressed = False
        self.one_three_button_pressed = False
        self.one_four_button_pressed = False
        self.two_null_button_pressed = False
        self.two_one_button_pressed = False
        self.two_two_button_pressed = False
        self.two_three_button_pressed = False
        self.two_four_button_pressed = False
        self.three_null_button_pressed = False
        self.three_one_button_pressed = False
        self.three_two_button_pressed = False
        self.three_three_button_pressed = False
        self.three_four_button_pressed = False
        self.four_null_button_pressed = False
        self.four_one_button_pressed = False
        self.four_two_button_pressed = False
        self.four_three_button_pressed = False
        self.four_four_button_pressed = False
        null_null_button.reset()
        null_one_button.reset()
        null_two_button.reset()
        null_three_button.reset()
        null_four_button.reset()
        one_null_button.reset()
        one_one_button.reset()
        one_two_button.reset()
        one_three_button.reset()
        one_four_button.reset()
        two_null_button.reset()
        two_one_button.reset()
        two_two_button.reset()
        two_three_button.reset()
        two_four_button.reset()
        three_null_button.reset()
        three_one_button.reset()
        three_two_button.reset()
        three_three_button.reset()
        three_four_button.reset()
        four_null_button.reset()
        four_one_button.reset()
        four_two_button.reset()
        four_three_button.reset()
        four_four_button.reset()
