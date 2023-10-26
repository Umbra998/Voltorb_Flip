import pygame
from settings import *
from generate_level import generate_level
from text import draw_text


class Level:
    def __init__(self, lvl):
        grid = []
        grid_row = []
        grid_column = []
        for row in range(5):
            r = [-1] * 5
            c = [0] * 2
            grid.append(r)
            grid_row.append(c)
            grid_column.append(c.copy())
        self.level = lvl
        self.grid = grid
        self.grid_row = grid_row
        self.grid_column = grid_column
        self.max_twos = 5
        self.max_threes = 3
        self.twos_set = 0
        self.threes_set = 0
        self.bombs = 5+self.level
        self.bombs_set = 0
        self.empty = True

    def draw(self):
        for grid_row in range(5):
            for grid_column in range(5):
                draw_text(f"Bombs: {self.grid_row[grid_row][0]}", FONT_GAME_STATUS, 'blue',
                          TILE_WIDTH * 5, TILE_HEIGHT * grid_row)
                draw_text(f"Score: {self.grid_row[grid_row][1]}", FONT_GAME_STATUS, 'blue',
                          TILE_WIDTH * 5, TILE_HEIGHT * grid_row + TILE_HEIGHT//2)
                draw_text(f"Bombs: {self.grid_column[grid_column][0]}", FONT_GAME_STATUS, 'blue',
                          TILE_WIDTH * grid_column, TILE_HEIGHT * 5)
                draw_text(f"Score: {self.grid_column[grid_column][1]}", FONT_GAME_STATUS, 'blue',
                          TILE_WIDTH * grid_column, TILE_HEIGHT * 5 + TILE_HEIGHT//2)

    def set_bombs_and_numbers(self):
        # 0 = bombs
        # 1 = 1s
        # 2 = 2s
        # 3 = 3s
        if self.empty is True:
            generate_level(self)
            self.empty = False

    def reset(self):
        for grid_row in range(5):
            for grid_column in range(5):
                self.grid[grid_row][grid_column] = -1
        for row in range(5):
            for col in range(2):
                self.grid_row[row][col] = 0
                self.grid_column[row][col] = 0
        self.level = 1
        self.twos_set = 0
        self.threes_set = 0
        self.max_twos = 5
        self.max_threes = 3
        self.bombs_set = 0
        self.empty = True
