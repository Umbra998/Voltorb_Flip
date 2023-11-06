import pygame
import random
from settings import *


def generate_level(self):
    # level
    set_level_restrictions(self)
    # put bombs
    for bomb in range(self.bombs):
        if self.bombs == self.bombs_set:
            break
        coordinates = generate_coordinates(self)
        x = coordinates[0]
        y = coordinates[1]
        self.grid[x][y] = 0
        self.bombs_set += 1
    # put numbers 2 and 3
    z = random.randint(0, self.max_threes)
    self.max_threes = z
    update_max_level(self)
    for twos in range(self.max_twos):
        coordinates = generate_coordinates(self)
        x = coordinates[0]
        y = coordinates[1]
        self.grid[x][y] = 2
    for threes in range(self.max_threes):
        coordinates = generate_coordinates(self)
        x = coordinates[0]
        y = coordinates[1]
        self.grid[x][y] = 3
    # put number 1s
    for num_x in range(5):
        for num_y in range(5):
            if self.grid[num_x][num_y] == -1:
                self.grid[num_x][num_y] = 1
    # update row and column grid
    for row in range(5):
        for column in range(5):
            if self.grid[row][column] == 0:
                self.grid_row[column][0] += 1
                self.grid_column[row][0] += 1
            else:
                self.grid_row[column][1] += self.grid[row][column]
                self.grid_column[row][1] += self.grid[row][column]


def set_level_restrictions(self):
    if self.level == 1:
        self.bombs = 6
        self.max_twos = 5
        self.max_threes = 3
    elif self.level == 2:
        self.bombs = 7
        self.max_twos = 6
        self.max_threes = 4
    elif self.level == 3:
        self.bombs = 8
        self.max_twos = 7
        self.max_threes = 4
    elif self.level == 4:
        self.bombs = 9
        self.max_twos = 8
        self.max_threes = 5
    elif self.level == 5:
        self.bombs = 10
        self.max_twos = 9
        self.max_threes = 5
    elif self.level == 6:
        self.bombs = 10
        self.max_twos = 8
        self.max_threes = 6
    elif self.level == 7:
        self.bombs = 10
        self.max_twos = 9
        self.max_threes = 6


def update_max_level(self):
    if self.level == 1:
        if self.max_threes == 0:
            self.max_twos = 5
        elif self.max_threes == 1:
            self.max_twos = 3
        elif self.max_threes == 2:
            self.max_twos = 2
        elif self.max_threes == 3:
            self.max_twos = 0
    if self.level == 2:
        if self.max_threes == 0:
            self.max_twos = 6
        if self.max_threes == 1:
            self.max_twos = 5
        if self.max_threes == 2:
            self.max_twos = 3
        if self.max_threes == 3:
            self.max_twos = 1
        if self.max_threes == 4:
            self.max_twos = 0
    if self.level == 3:
        if self.max_threes == 0:
            self.max_twos = 6
        if self.max_threes == 1:
            self.max_twos = 6
        if self.max_threes == 2:
            self.max_twos = 4
        if self.max_threes == 3:
            self.max_twos = 2
        if self.max_threes == 4:
            self.max_twos = 0
    if self.level == 4:
        if self.max_threes == 0:
            self.max_twos = 8
        if self.max_threes == 1:
            self.max_threes = 2
            self.max_twos = 5
        if self.max_threes == 2:
            self.max_twos = 5
        if self.max_threes == 3:
            self.max_twos = 3
        if self.max_threes == 4:
            self.max_twos = 2
        if self.max_threes == 5:
            self.max_twos = 0
    if self.level == 5:
        if self.max_threes == 0:
            self.max_twos = 9
        if self.max_threes == 1:
            self.max_twos = 7
        if self.max_threes == 2:
            self.max_twos = 6
        if self.max_threes == 3:
            self.max_twos = 4
        if self.max_threes == 4:
            self.max_threes = 3
            self.max_twos = 4
        if self.max_threes == 5:
            self.max_twos = 1
    if self.level == 6:
        if self.max_threes == 0:
            self.max_threes = 1
        if self.max_threes == 1:
            self.max_twos = 8
        if self.max_threes == 2:
            self.max_threes = 3
        if self.max_threes == 3:
            self.max_twos = 5
        if self.max_threes == 4:
            self.max_twos = 3
        if self.max_threes == 5:
            self.max_twos = 2
        if self.max_threes == 6:
            self.max_twos = 2
            self.max_threes = 5
    if self.level == 7:
        if self.max_threes == 0:
            self.max_threes = 1
        if self.max_threes == 1:
            self.max_twos = 9
        if self.max_threes == 2:
            self.max_twos = 7
        if self.max_threes == 3:
            self.max_twos = 6
        if self.max_threes == 4:
            self.max_twos = 4
        if self.max_threes == 5:
            self.max_threes = 6
        if self.max_threes == 6:
            self.max_twos = 1


def generate_coordinates(self):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if self.grid[x][y] == -1:
        return x, y
    else:
        return generate_coordinates(self)
