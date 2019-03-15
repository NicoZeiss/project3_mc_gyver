#!/usr/bin/python3
# -*- coding: Utf-8 -*-


"""
Game : Mc Gyver has to escape from the maze
Don't forget to pick every item you will find
"""


import pygame
from pygame.locals import *
from classes import *
from constants import *

# We launch the game, and the main window
pygame.init()
window = pygame.display.set_mode((window_size, window_size))


# Main loop
keep_open = 1
while keep_open:
	# We load and display start menu picture
	start_menu = pygame.image.load(start_menu_pict).convert()
	window.blit(start_menu, (0,0))

	# Refreshing
	pygame.display.flip()

	# Start menu loop
	keep_menu_open = 1
	# Party loop
	keep_party_open = 1

	while keep_menu_open:
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			# If user quit, all loops are broken
			if event.type == QUIT:
				keep_menu_open = 0
				keep_party_open = 0
				keep_open = 0

			# If user press space bar we break start menu loop and we're going to the next
			elif event.type == KEYDOWN:
				if event.key == K_SPACE:
					keep_menu_open = 0

	while keep_party_open:

		# We launch the maze level
		background = pygame.image.load(background_pict).convert()
		window.blit(background, (0,0))
		maze = Maze("maze.txt")
		maze.generate_maze()
		maze.show_maze(window)

		# We launch our character
		mc_gyver = Character("pictures/mcgyver.png", maze)
		window.blit(mc_gyver.pict, (mc_gyver.x, mc_gyver.y))

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			if event.type == QUIT:
				keep_party_open = 0
				keep_open = 0

			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					keep_party_open = 0


		pygame.display.flip()








