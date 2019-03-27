#!/usr/bin/python3
# -*- coding: Utf-8 -*-


"""
Game : Mc Gyver has to escape from the maze
Don't forget to pick every item you will find
"""

import pygame
from pygame.locals import *
from functions import *
from constants import window_size, window_title, mcgyver_pict
from design import *

def main():
    """that's the main function wich allows to launch the game"""

    pygame.init()
    window = pygame.display.set_mode((window_size, window_size))
    # Window title
    pygame.display.set_caption(window_title)
    # Set an icon
    icon = pygame.image.load(mcgyver_pict)
    pygame.display.set_icon(icon)

    main_open = 1
    while main_open :
        menu_open = 1
        party_open = 1
        win_loop = 1

        while menu_open:
            #start menu loop
            start_menu(window)

            for event in pygame.event.get():
                # If user quit, all loops are broken
                if event.type == QUIT:
                    main_open = 0
                    menu_open = 0
                    party_open = 0
                    win_loop = 0

                # If user press space bar we break start menu loop and we're going to the next
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        menu_open = 0

        background, maze, mc_gyver = launch_party(window)
        item_dic = generate_items(window, maze)

        while party_open:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():

                if event.type == QUIT:
                    main_open = 0
                    party_open = 0
                    win_loop = 0

                elif event.type == KEYDOWN:
                    # Go back to start menu with Escape
                    if event.key == K_ESCAPE:
                        party_open = 0
                        win_loop = 0

                    # Binding to move our character
                    elif event.key == K_RIGHT:
                        mc_gyver.move_char("right")
                    elif event.key == K_LEFT:
                        mc_gyver.move_char("left")
                    elif event.key == K_UP:
                        mc_gyver.move_char("up")
                    elif event.key == K_DOWN:
                        mc_gyver.move_char("down")

            # We display all new position
            display_new_pos(window, background, maze, mc_gyver)
            show_items(window, item_dic, mc_gyver)
            count = display_meter(window, item_dic)
            # We check if player win
            win = check_win(window, mc_gyver, maze, count)
            pygame.display.flip()
            if win is True:
                party_open = 0

        while win_loop:
            pygame.time.Clock().tick(30)

            for event in pygame.event.get():
                if event.type == QUIT:
                    main_open = 0
                    win_loop = 0
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        win_loop = 0

if __name__ == "__main__":
    main()
