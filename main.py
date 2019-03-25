#!/usr/bin/python3
# -*- coding: Utf-8 -*-


"""
Game : Mc Gyver has to escape from the maze
Don't forget to pick every item you will find
"""


import pygame
from pygame.locals import *
import random

from functions import *
from classes import *
from constants import *

# We launch the game, and the main window
pygame.init()
window = pygame.display.set_mode((window_size, window_size))
# Window title
pygame.display.set_caption(window_title)
# Set an icon
icon = pygame.image.load(mcgyver_pict)
pygame.display.set_icon(icon)

# Main loop
keep_open = 1
while keep_open:
    # We load and display start menu picture
    start_menu = load_pict(start_menu_pict, window_size, window_size, False)
    window.blit(start_menu, (0,0))

    # Refreshing
    pygame.display.flip()

    # Start menu loop
    keep_menu_open = 1
    # Party loop
    keep_party_open = 1
    # Win loop
    win_loop = 1

    while keep_menu_open:
        pygame.time.Clock().tick(30)

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

    # We launch the maze level
    background = load_pict(background_pict, window_size, window_size, False)
    maze = Maze("maze.txt")
    maze.generate_maze()
    maze.show_maze(window)

    # We launch our character
    mc_gyver = Character(mcgyver_pict, maze)

    # Launch items in a list and dic
    item_list = ["needle", "tube", "ether"]
    item_dic = {}
    for i in range(len(item_list)):
        # We create an object from class Items for each item in the list
        item_list[i] = Items(item_list[i], maze)
        item_list[i].generate_item()
        item_list[i].show_item(window)
        item_dic[i] = [item_list[i], True]

    # Game loop
    while keep_party_open:

        pygame.time.Clock().tick(30)

        for event in pygame.event.get():

			if event.type == QUIT:
				keep_party_open = 0
				win_loop = 0
				keep_open = 0

			elif event.type == KEYDOWN:
				# Go back to start menu with Escape
				if event.key == K_ESCAPE:
					keep_party_open = 0

				# Binding to move our character
				elif event.key == K_RIGHT:
					mc_gyver.move_char("right")
				elif event.key == K_LEFT:
					mc_gyver.move_char("left")
				elif event.key == K_UP:
					mc_gyver.move_char("up")
				elif event.key == K_DOWN:
					mc_gyver.move_char("down")

		# Check if Mc Gyver collect an objet
		for i in range(len(item_dic)):
			if mc_gyver.pos_x == item_dic[i][0].pos_x:
				if mc_gyver.pos_y == item_dic[i][0].pos_y:
					item_dic[i][1] = False

		# Raise meter count
		count = 0
		for i in range(len(item_dic)):
			if item_dic[i][1] == False:
				count += 1
        # Display a meter to let player know how many items are remaining
        meter_text = "{} / {} items collected:".format(count, len(item_dic))
        font = pygame.font.Font(None, 30)
        meter_display = font.render(meter_text, 1, (255,255,255))

        # Display new position
        window.blit(background,(0,0))
        maze.show_maze(window)
        window.blit(mc_gyver.pict, (mc_gyver.x, mc_gyver.y))
        window.blit(meter_display, (10,12))

        # Show item not yet collected and display on the top items collected
        for i in range(len(item_dic)):
			if item_dic[i][1] == True:
				item_dic[i][0].show_item(window)
			else:
				x = 5 * sprite_size + i * sprite_size
				item_dic[i][0].item_check(window, x)
				
        # Refreshing window
        pygame.display.flip()

        # Win conditions and win message
        if maze.maze[mc_gyver.pos_x][mc_gyver.pos_y] == "M":
            # Check if all items are collected, to win
            if count == len(item_list):
                keep_party_open = 0
                win_mess = win_message(window, True)
            # If not, player loses
            else:
                keep_party_open = 0
                win_mess = win_message(window, False)
            pygame.display.flip()
            # Keep win screen open
            while win_loop:
                pygame.time.Clock().tick(30)
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE or event.key == K_ESCAPE:
                            win_loop = 0
                        elif event.type == QUIT:
                            win_loop = 0
                            keep_open = 0
			
				

#prob range avec première solution for pour supp items
