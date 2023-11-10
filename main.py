import random

import pygame
from settings import *
from level import Level
from draw_grid import draw_grid
from button import Button
from text import draw_text
from grid_buttons import create_buttons, update_buttons, reveal_buttons, reset_buttons, update_button_images
from edit_images import create_edits, update_edit_images, draw_images, clear_images
from fade import fade
from display_text import draw_grid_text, draw_level_text, draw_score_text
pygame.init()

# init level and grid
level = Level(1)

# button
start_button = Button(SCREEN_WIDTH, SCREEN_HEIGHT//2,
                      start_image)
restart_button = Button(SCREEN_WIDTH, TILE_HEIGHT * 5 + TILE_HEIGHT//4,
                        restart_image)
continue_button = Button(SCREEN_WIDTH, SCREEN_HEIGHT//2,
                         continue_image)
edit_button = Button(SCREEN_WIDTH, SCREEN_HEIGHT//3,
                     edit_image)
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


# main loop
def main(state, game_score, running):
    no_failure_in_row = 0
    edit_num = -1
    create_buttons()
    create_edits()

    while running:
        SCREEN.fill('dimgray')
        draw_level_text(level)
        draw_score_text(game_score)
        if state == 1:
            draw_grid()
            update_buttons(level)
            draw_images(level)
            draw_grid_text(level)
            game_completion = level.check_for_clear()
            if game_completion == 0:
                state = 2
            if game_completion == 1:
                state = 4
            if restart_button.draw():
                fade(SCREEN_WIDTH, SCREEN_HEIGHT)
                no_failure_in_row = 0
                level.reset()
                reset_buttons()
                game_score = 0
                state = 0
                level.level = 1
            if edit_button.draw():
                state = 5

        if state == 0 and start_button.draw():
            level.set_bombs_and_numbers()
            state = 1

        if state == 2:
            draw_grid()
            draw_grid_text(level)
            reveal_buttons()
            update_button_images(level)
            if continue_button.draw():
                if level.level == 8:
                    x = random.randint(1, (level.level - 1))
                else:
                    x = random.randint(0, (level.level - 1))
                level.level -= x
                no_failure_in_row = 0
                state = 3

        if state == 3:
            fade(SCREEN_WIDTH, SCREEN_HEIGHT)
            level.reset()
            reset_buttons()
            clear_images()
            state = 0

        if state == 4:
            draw_grid()
            draw_grid_text(level)
            reveal_buttons()
            update_button_images(level)
            if continue_button.draw():
                if level.level < 7:
                    level.level += 1
                    no_failure_in_row += 1
                elif no_failure_in_row >= 5:
                    level.level = 8
                else:
                    level.level = 7
                if game_score < 50000:
                    game_score += level.score
                    if game_score > 50000:
                        game_score = 50000
                state = 3

        if state == 5:
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
            draw_grid()
            update_edit_images(level, edit_num)
            update_button_images(level)
            draw_images(level)
            draw_grid_text(level)
            if edit_button.draw():
                state = 1
                edit_num = -1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(game_state, score, running=True)

pygame.quit()
