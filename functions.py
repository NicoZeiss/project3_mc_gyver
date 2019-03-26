#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Functions used in main.py to display messages and pictures
"""

import pygame


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
