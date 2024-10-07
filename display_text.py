import pygame
from settings import *
from text import draw_text


def draw_grid_text(self):
    for grid_row in range(5):
        for grid_column in range(5):
            draw_text(f"Bombs: {self.grid_column[grid_row][0]}", FONT_GAME_STATUS, 'red',
                      TILE_WIDTH * 5 + TILE_WIDTH // 8, TILE_HEIGHT * grid_row + TILE_HEIGHT // 5)
            draw_text(f"Total: {self.grid_column[grid_row][1]}", FONT_GAME_STATUS, 'green',
                      TILE_WIDTH * 5 + TILE_WIDTH // 8, TILE_HEIGHT * grid_row + TILE_HEIGHT // 1.5)
            draw_text(f"Bombs: {self.grid_row[grid_column][0]}", FONT_GAME_STATUS, 'red',
                      TILE_WIDTH * grid_column + TILE_WIDTH // 8, TILE_HEIGHT * 5 + TILE_HEIGHT // 5)
            draw_text(f"Total: {self.grid_row[grid_column][1]}", FONT_GAME_STATUS, 'green',
                      TILE_WIDTH * grid_column + TILE_WIDTH // 8, TILE_HEIGHT * 5 + TILE_HEIGHT // 1.5)
    draw_text("Score:", FONT_GAME_STATUS, 'orange',
              TILE_WIDTH * 5 + MARGIN // 4, TILE_HEIGHT * 5 + TILE_HEIGHT // 5)
    draw_text(f"{self.score}", FONT_SCORE, 'orange',
              TILE_WIDTH * 5 + MARGIN // 2.5, TILE_HEIGHT * 5 + TILE_HEIGHT // 2)


def draw_level_text(self):
    draw_text("Level:", FONT_LEVEL, 'orange',
              SCREEN_WIDTH + MARGIN//20, 0)
    draw_text(f"{self.level}", FONT_LEVEL, 'orange',
              SCREEN_WIDTH + MARGIN//2.5, TILE_HEIGHT//2)


def draw_score_text(game_score):
    draw_text("Score:", FONT_LEVEL, 'orange',
              SCREEN_WIDTH + MARGIN // 20, TILE_HEIGHT)
    if game_score < 10:
        draw_text(f"{game_score}", FONT_LEVEL, 'orange',
                  SCREEN_WIDTH + MARGIN // 2.5, TILE_HEIGHT * 2 - TILE_HEIGHT // 2)

    elif game_score < 100:
        draw_text(f"{game_score}", FONT_LEVEL, 'orange',
                  SCREEN_WIDTH + MARGIN // 3, TILE_HEIGHT * 2 - TILE_HEIGHT // 2)
    elif game_score < 1000:
        draw_text(f"{game_score}", FONT_LEVEL, 'orange',
                  SCREEN_WIDTH + MARGIN // 3.8, TILE_HEIGHT * 2 - TILE_HEIGHT // 2)
    elif game_score < 10000:
        draw_text(f"{game_score}", FONT_LEVEL, 'orange',
                  SCREEN_WIDTH + MARGIN // 4.7, TILE_HEIGHT * 2 - TILE_HEIGHT // 2)
    else:
        draw_text(f"{game_score}", FONT_LEVEL, 'orange',
                  SCREEN_WIDTH + MARGIN // 6, TILE_HEIGHT * 2 - TILE_HEIGHT // 2)
