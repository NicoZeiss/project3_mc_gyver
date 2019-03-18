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

	# We launch the maze level
	background = pygame.image.load(background_pict).convert()
	window.blit(background, (0,0))
	maze = Maze("maze.txt")
	maze.generate_maze()
	maze.show_maze(window)

	# We launch our character
	mc_gyver = Character("pictures/mcgyver.png", maze)
	window.blit(mc_gyver.pict, (mc_gyver.x, mc_gyver.y))

	# Game loop
	while keep_party_open:

		pygame.time.Clock().tick(30)

		for event in pygame.event.get():

			if event.type == QUIT:
				keep_party_open = 0
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

		# Display new position
		window.blit(background,(0,0))
		maze.show_maze(window)
		window.blit(mc_gyver.pict, (mc_gyver.x, mc_gyver.y))
		pygame.display.flip()

		if maze.maze[mc_gyver.pos_x][mc_gyver.pos_y] == "M":
			keep_party_open = 0
