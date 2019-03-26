#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Functions used in main.py to display messages and pictures
"""

import pygame
from constants import *
from pygame.locals import *


def win_message(check):
    """Display the win message when mcgyver reach murdoc with all items"""
    # Player win if he has collected all items
    if check is True:
        font = pygame.font.Font(None, 50)
        win_mess = font.render("YOU WIN !!!", 1, (255, 255, 255))
    # If not, he loses
    elif check is False:
        font = pygame.font.Font(None, 50)
        win_mess = font.render("Ops, Murdoc just killed you...", 1, (255, 255, 255))
    return win_mess

def load_pict(pict, coord_x, coord_y, alpha):
    """This function will load pict and convert them to the right size.
    Pict arg is the name of the pict
    x and y args are the required size
    alpha is a bolean which let us know if we have to convert_alpha the pict"""

    if alpha is True:
        object_pict = pygame.image.load(pict).convert_alpha()
        resized_pict = pygame.transform.scale(object_pict, (coord_x, coord_y))
    else:
        object_pict = pygame.image.load(pict).convert()
        resized_pict = pygame.transform.scale(object_pict, (coord_x, coord_y))
    return resized_pict

def main_loop(window):
    # We load and display start menu picture
    start_menu = load_pict(start_menu_pict, window_size, window_size, False)
    window.blit(start_menu, (0, 0))
    # Refreshing
    pygame.display.flip()

def startmenu_loop():
    for event in pygame.event.get():
        # If user quit, all loops are broken
        if event.type == QUIT:
            keep_menu_open = 0
            keep_party_open = 0
            win_loop = 0
            keep_open = 0

        # If user press space bar we break start menu loop and we're going to the next
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                keep_menu_open = 0
