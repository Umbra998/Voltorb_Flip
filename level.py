import pygame
from settings import *
from generate_level import generate_level
from text import draw_text
from draw_grid import draw_grid


class Level:
    def __init__(self, lvl):
        grid = []
        grid_row = []
        grid_column = []
        grid_found = []
        for row in range(5):
            r = [-1] * 5
            c = [0] * 2
            grid.append(r)
            grid_found.append(r.copy())
            grid_row.append(c)
            grid_column.append(c.copy())
        self.level = lvl
        self.grid = grid
        self.grid_found = grid_found
        self.grid_row = grid_row
        self.grid_column = grid_column
        self.max_twos = 0
        self.max_threes = 0
        self.twos_set = 0
        self.threes_set = 0
        self.bombs = 6
        self.bombs_set = 0
        self.empty = True
        self.score = 1
        self.cleared = False

    def set_bombs_and_numbers(self):
        # 0 = bombs, 1 = 1s, 2 = 2s, 3 = 3s
        if self.empty is True:
            generate_level(self)
            self.empty = False

    def check_for_clear(self):
        num_found = 0
        bomb_found = False
        for col in range(5):
            for row in range(5):
                if self.grid[row][col] == 2 and self.grid_found[row][col] == 1\
                        or self.grid[row][col] == 3 and self.grid_found[row][col] == 1:
                    num_found += 1
                if self.grid[row][col] == 0 and self.grid_found[row][col] == 0:
                    bomb_found = True
        if bomb_found:
            return 0
        if num_found == (self.max_twos+self.max_threes):
            return 1
        else:
            return -1

    def reset(self):
        for grid_row in range(5):
            for grid_column in range(5):
                self.grid[grid_row][grid_column] = -1
                self.grid_found[grid_row][grid_column] = -1
        for row in range(5):
            for col in range(2):
                self.grid_row[row][col] = 0
                self.grid_column[row][col] = 0
        # self.level = 1
        self.twos_set = 0
        self.threes_set = 0
        self.max_twos = -1
        self.max_threes = -1
        self.bombs_set = 0
        self.empty = True
        self.score = 1
