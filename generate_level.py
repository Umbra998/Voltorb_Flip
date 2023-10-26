import pygame
import random
from settings import *


def generate_level(self):
    print("Level generated!")
    if self.level == 1:
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
        for num in range(self.max_twos+self.max_threes):
            if self.twos_set == self.max_twos and self.threes_set == self.max_threes:
                break
            coordinates = generate_coordinates(self)
            x = coordinates[0]
            y = coordinates[1]
            update_max_level_one(self)
            z = random.randint(2, 3)
            if z == 2 and self.twos_set < self.max_twos:
                self.grid[x][y] = 2
                self.twos_set += 1
            elif z == 3 and self.threes_set < self.max_twos:
                self.grid[x][y] = 3
                self.threes_set += 1
    for num_x in range(5):
        for num_y in range(5):
            if self.grid[num_x][num_y] == -1:
                self.grid[num_x][num_y] = 1
    print(self.grid)
    for row in range(5):
        for column in range(5):
            if self.grid[row][column] == 0:
                self.grid_row[column][0] += 1
                self.grid_column[row][0] += 1
            else:
                self.grid_row[column][1] += self.grid[row][column]
                self.grid_column[row][1] += self.grid[row][column]
    print(self.grid_row)
    print(self.grid_column)


def update_max_level_one(self):
    if self.twos_set == 1:
        self.max_threes = 2
    elif self.twos_set == 3:
        self.max_threes = 1
    elif self.twos_set == 4:
        self.max_threes = 0
    if self.threes_set == 1:
        self.max_twos = 3
    elif self.threes_set == 2:
        self.max_twos = 2
    elif self.threes_set == 3:
        self.max_twos = 0


def generate_coordinates(self):
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    if self.grid[x][y] == -1:
        return x, y
    else:
        return generate_coordinates(self)
