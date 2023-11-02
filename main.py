import pygame
from settings import *
from level import Level
from draw_grid import draw_grid
from button import Button
from text import draw_text
from grid_buttons import GridButtons
from fade import fade
from display_text import draw_grid_text, draw_level_text
pygame.init()

# init level and grid
level = Level(1)
grid = GridButtons()

# button images
start_image = pygame.image.load("img/Buttons/start.png")
start_image = pygame.transform.scale(start_image, (TILE_WIDTH, TILE_HEIGHT//2))
restart_image = pygame.image.load("img/Buttons/restart.png")
restart_image = pygame.transform.scale(restart_image, (TILE_WIDTH, TILE_HEIGHT//2))
continue_image = pygame.image.load("img/Buttons/continue.png")
continue_image = pygame.transform.scale(continue_image, (TILE_WIDTH, TILE_HEIGHT//2))

# button
start_button = Button(SCREEN_WIDTH, SCREEN_HEIGHT//2,
                      start_image)
restart_button = Button(SCREEN_WIDTH, TILE_HEIGHT * 5 + TILE_HEIGHT//4,
                        restart_image)
continue_button = Button(SCREEN_WIDTH, SCREEN_HEIGHT//2,
                         continue_image)


# main loop
def main(state, running):

    while running:
        SCREEN.fill('dimgray')
        draw_level_text(level)
        if state == 1:
            draw_grid()
            grid.update(level)
            draw_grid_text(level)
            game_completion = level.check_for_clear()
            if game_completion == 0:
                state = 2
            if game_completion == 1:
                state = 4

        if state == 0 and start_button.draw():
            level.set_bombs_and_numbers()
            state = 1

        if state == 1 and restart_button.draw():
            fade(SCREEN_WIDTH, SCREEN_HEIGHT)
            level.reset()
            grid.reset()
            state = 0
            level.level = 1

        if state == 2:
            draw_grid()
            draw_grid_text(level)
            grid.reveal()
            grid.update_images(level)
            if continue_button.draw():
                level.level = level.level//2
                state = 3

        if state == 3:
            fade(SCREEN_WIDTH, SCREEN_HEIGHT)
            level.reset()
            grid.reset()
            state = 0

        if state == 4:
            draw_grid()
            draw_grid_text(level)
            grid.reveal()
            grid.update_images(level)
            if continue_button.draw():
                if level.level != 4:
                    level.level += 1
                state = 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main(game_state, running=True)

pygame.quit()
