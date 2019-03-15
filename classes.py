"""Here are the different classes we'll used in our game"""

import pygame

from pygame.locals import *
from constants import *

class Maze:
	"""Thanks to this class we'll create a maze, converting .txt to list"""
	def __init__(self, file):
		self.file = file
		self.maze = 0

	def generate_maze(self):
		"""We create a list which contains all row from maze.txt"""
		with open(self.file, "r") as file:
			global_maze =  []
			# We iterate on each row contained in our file .txt
			for row in file:
				maze_row = []
				# We iretate on each sprite from rows, to create lists with each value
				for sprite in row:
					if sprite != "\n":
						maze_row.append(sprite)

				# We append each list (row) to our global list which represent our maze
				global_maze.append(maze_row)

			self.maze = global_maze

	def show_maze(self, window):
		"""With this method we'll show the maze in pygame"""
		# We load pictures
		start = pygame.image.load(start_pict).convert()
		murdoc = pygame.image.load(murdoc_pict).convert_alpha()
		wall_oversized = pygame.image.load(wall_pict).convert()
		wall = pygame.transform.scale(wall_oversized, (45,45))

		num_row = 0
		# We iterate on each row, an then each sprite
		for row in self.maze:
			num_column = 0
			for sprite in row:
				# We convert sprite position in pixels
				x = num_column * sprite_size
				y = num_row * sprite_size
				# We show a different picture for each kind of sprite
				if sprite == "W":
					window.blit(wall, (x,y))
				elif sprite == "S":
					window.blit(start, (x,y))
				elif sprite == "M":
					window.blit(murdoc, (x,y))
				num_column += 1
			num_row += 1
					

class Character(self):
	"""Thanks to this class we'll create our character"""

	def __init__(self, level)
		pygame.image.load("pictures/mcgyver.png").convert_alpha()
		# That's the position of mc gyver (in sprites)
		self.pos_x = 0
		self.pos_y = 0
		# Position in pixels
		self.x = 0
		self.y = 0
		# That's the level where the character is
		self.level = level

	def move_char(self, direction):
		"""This method will calculate the new position of mc gyver, after each move"""
		
		# Move to right side
		if direction == "right":
			# We check if the move is possible (in the window)
			if self.pos_x < (sprites_per_side - 1):
				# We check if the move is possible (not a wall)
				if self.level.maze[self.pos_y][self.pos_x + 1] != "W":
					# New position of mc gyver, in sprites
					self.pos_x += 1
					# Real new position in pixels
					self.x = self.pos_x * sprite_size

		# Move to left side
		if direction == "left":
			if self.pos_x > 0:
				if self.level.maze[self.pos_y][self.pos_x - 1] != "W":
					self.pos_x -= 1
					self.x = self.pos_x * sprite_size

		# Move to the top side
		if direction == "top":
			if self.pos_x > 0:
				if self.level.maze[self.pos_y - 1][self.pos_x] != "W":
					self.pos_y -= 1
					self.y = self.pos_y * sprite_size

		# Move to the bottom side
		if direction == "bottom":
			if self.pos_x < (sprites_per_side - 1):
				if self.level.maze[self.pos_y + 1][self.pos_x] != "W":
					self.pos_y += 1
					self.y = self.pos_y * sprite_size


