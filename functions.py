#!/usr/bin/python3
# -*- coding: Utf-8 -*-


"""All functions we need to run the game: generate items, maze, char -> display them"""


import pygame
from pygame.locals import *
from constants import sprite_size, window_size, background_pict, mcgyver_pict, start_menu_pict
from classes import Maze, Items, Character
from design import win_message

def start_menu(window):
    """ We load and display start menu picture"""

    menu = pygame.image.load(start_menu_pict).convert()
    resized_menu = pygame.transform.scale(menu, (window_size, window_size))
    window.blit(resized_menu, (0, 0))
    # Refreshing
    pygame.display.flip()

def launch_party():
    """ Launching background, maze and mac gyver"""

    background = pygame.image.load(background_pict).convert()
    resized_background = pygame.transform.scale(background, (window_size, window_size))

    maze = Maze("maze.txt")
    maze.generate_maze()

    mc_gyver = Character(mcgyver_pict, maze)

    return resized_background, maze, mc_gyver

def display_new_pos(window, background, maze, mc_gyver):
    """We display mac gyver at new position"""

    window.blit(background, (0, 0))
    maze.show_maze(window)
    window.blit(mc_gyver.pict, (mc_gyver.x_pix, mc_gyver.y_pix))

def generate_items(maze):
    """We generate randomly items in the maze, and save themn in a dic"""

    item_list = ["needle", "tube", "ether"]
    item_dic = {}
    for i, item in enumerate(item_list):
        # We create an object from class Items for each item in the list
        item_list[i] = Items(item, maze)
        item_list[i].generate_item()
        item_dic[i] = [item_list[i], True]
    return item_dic

def show_items(window, item_dic, mc_gyver):
    """Check if mac gyver collect an object, and show it if not"""

    # Check item
    for i in item_dic:
        if mc_gyver.pos_x == item_dic[i][0].pos_x:
            if mc_gyver.pos_y == item_dic[i][0].pos_y:
                item_dic[i][1] = False
    # If mc gyver collect item we del it from maze and show it in inventory
    for i in item_dic:
        if item_dic[i][1] is True:
            item_dic[i][0].show_item(window)
        else:
            coord_x = 5 * sprite_size + i * sprite_size
            item_dic[i][0].item_check(window, coord_x)

def check_win(window, mc_gyver, maze, count):
    """If mac gyver has collected all items and reach murloc, player win"""
    if maze.maze[mc_gyver.pos_x][mc_gyver.pos_y] == "M":
        if count == 3:
            win_mess = win_message(window, True)
            window.blit(win_mess, (280, 365))
        # If not, player loses
        else:
            win_mess = win_message(window, False)
            window.blit(win_mess, (140, 365))
        return True
    else:
        return False
