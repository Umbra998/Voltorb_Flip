import pygame
from settings import *
from grid import Level
from draw_grid import draw_grid
from button import Button
from text import draw_text
pygame.init()

# init level
level = Level(level_number)

# button
start_button = Button(TILE_WIDTH*5, TILE_HEIGHT*5,
                      pygame.image.load("img/Buttons/start.png"))
restart_button = Button(TILE_WIDTH * 5, TILE_HEIGHT * 5 + TILE_HEIGHT//2,
                        pygame.image.load("img/Buttons/restart.png"))
# grid buttons
question_mark_img = pygame.image.load("img/Buttons/question_mark.png")
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


# main loop
def main():
    running = True
    started = False
    # button pressed
    null_null_button_pressed = False
    null_one_button_pressed = False
    null_two_button_pressed = False
    null_three_button_pressed = False
    null_four_button_pressed = False
    one_null_button_pressed = False
    one_one_button_pressed = False
    one_two_button_pressed = False
    one_three_button_pressed = False
    one_four_button_pressed = False
    two_null_button_pressed = False
    two_one_button_pressed = False
    two_two_button_pressed = False
    two_three_button_pressed = False
    two_four_button_pressed = False
    three_null_button_pressed = False
    three_one_button_pressed = False
    three_two_button_pressed = False
    three_three_button_pressed = False
    three_four_button_pressed = False
    four_null_button_pressed = False
    four_one_button_pressed = False
    four_two_button_pressed = False
    four_three_button_pressed = False
    four_four_button_pressed = False
    while running:

        SCREEN.fill('dimgray')
        draw_grid()
        level.draw()

        if null_null_button.draw() and null_null_button_pressed is False and started is True:
            null_null_button_pressed = True
        if null_one_button.draw() and null_one_button_pressed is False and started is True:
            null_one_button_pressed = True
        if null_two_button.draw() and null_two_button_pressed is False and started is True:
            null_two_button_pressed = True
        if null_three_button.draw() and null_three_button_pressed is False and started is True:
            null_three_button_pressed = True
        if null_four_button.draw() and null_four_button_pressed is False and started is True:
            null_four_button_pressed = True
        if one_null_button.draw() and one_null_button_pressed is False and started is True:
            one_null_button_pressed = True
        if one_one_button.draw() and one_one_button_pressed is False and started is True:
            one_one_button_pressed = True
        if one_two_button.draw() and one_two_button_pressed is False and started is True:
            one_two_button_pressed = True
        if one_three_button.draw() and one_three_button_pressed is False and started is True:
            one_three_button_pressed = True
        if one_four_button.draw() and one_four_button_pressed is False and started is True:
            one_four_button_pressed = True
        if two_null_button.draw() and two_null_button_pressed is False and started is True:
            two_null_button_pressed = True
        if two_one_button.draw() and two_one_button_pressed is False and started is True:
            two_one_button_pressed = True
        if two_two_button.draw() and two_two_button_pressed is False and started is True:
            two_two_button_pressed = True
        if two_three_button.draw() and two_three_button_pressed is False and started is True:
            two_three_button_pressed = True
        if two_four_button.draw() and two_four_button_pressed is False and started is True:
            two_four_button_pressed = True
        if three_null_button.draw() and three_null_button_pressed is False and started is True:
            three_null_button_pressed = True
        if three_one_button.draw() and three_one_button_pressed is False and started is True:
            three_one_button_pressed = True
        if three_two_button.draw() and three_two_button_pressed is False and started is True:
            three_two_button_pressed = True
        if three_three_button.draw() and three_three_button_pressed is False and started is True:
            three_three_button_pressed = True
        if three_four_button.draw() and three_four_button_pressed is False and started is True:
            three_four_button_pressed = True
        if four_null_button.draw() and four_null_button_pressed is False and started is True:
            four_null_button_pressed = True
        if four_one_button.draw() and four_one_button_pressed is False and started is True:
            four_one_button_pressed = True
        if four_two_button.draw() and four_two_button_pressed is False and started is True:
            four_two_button_pressed = True
        if four_three_button.draw() and four_three_button_pressed is False and started is True:
            four_three_button_pressed = True
        if four_four_button.draw() and four_four_button_pressed is False and started is True:
            four_four_button_pressed = True

        if start_button.draw() and started is False:
            level.set_bombs_and_numbers()
            started = True

        if restart_button.draw() and started is True:
            level.reset()
            started = False
            null_null_button_pressed = False
            null_one_button_pressed = False
            null_two_button_pressed = False
            null_three_button_pressed = False
            null_four_button_pressed = False
            one_null_button_pressed = False
            one_one_button_pressed = False
            one_two_button_pressed = False
            one_three_button_pressed = False
            one_four_button_pressed = False
            two_null_button_pressed = False
            two_one_button_pressed = False
            two_two_button_pressed = False
            two_three_button_pressed = False
            two_four_button_pressed = False
            three_null_button_pressed = False
            three_one_button_pressed = False
            three_two_button_pressed = False
            three_three_button_pressed = False
            three_four_button_pressed = False
            four_null_button_pressed = False
            four_one_button_pressed = False
            four_two_button_pressed = False
            four_three_button_pressed = False
            four_four_button_pressed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

pygame.quit()
