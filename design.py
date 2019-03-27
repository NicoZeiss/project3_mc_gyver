#!/usr/bin/python3
# -*- coding: Utf-8 -*-

"""
Functions used in main.py to display messages and pictures
"""

import pygame
from constants import *
from pygame.locals import *


def win_message(window, check):
    """Display the win message when mcgyver reach murdoc with all items"""
    # Player win if he has collected all items
    if check is True:
        font = pygame.font.Font(None, 50)
        win_mess = font.render("YOU WIN !!!", 1, (255, 255, 255))
        window.blit(win_mess, (280, 365))

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

def display_meter(window, item_dic):
    """We display a meter to count how many items are collected"""
    count = 0
    for i, item in enumerate(item_dic):
        if item_dic[i][1] is False:
            count += 1
    # Display a meter to let player know how many items are remaining
    meter_text = "{} / {} items collected:".format(count, len(item_dic))
    font = pygame.font.Font(None, 30)
    meter_display = font.render(meter_text, 1, (255, 255, 255))
    window.blit(meter_display, (10, 12))
    return count
