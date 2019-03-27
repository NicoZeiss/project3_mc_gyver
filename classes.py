#!/usr/bin/python3
# -*- coding: Utf-8 -*-


"""
Here are the different classes we'll used in our game
"""

import random

from constants import sprites_per_side, sprite_size, murdoc_pict, wall_pict, start_pict
from design import load_pict

class Maze(object):
    """Thanks to this class we'll create a maze, converting .txt to list"""
    def __init__(self, maze_file):
        self.maze = maze_file

    def generate_maze(self):
        """We create a list which contains all row from maze.txt"""
        with open(self.maze, "r") as file:
            global_maze = []
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
        # We load pictures from function load_pict
        start = load_pict(start_pict, sprite_size, sprite_size, True)
        murdoc = load_pict(murdoc_pict, sprite_size, sprite_size, True)
        wall = load_pict(wall_pict, sprite_size, sprite_size, False)

        num_row = 0
        # We iterate on each row, an then each sprite
        for row in self.maze:
            num_column = 0
            for sprite in row:
                # We convert sprite position in pixels
                x_pix = num_column * sprite_size
                y_pix = num_row * sprite_size
                # We show a different picture for each kind of sprite
                if sprite == "W":
                    window.blit(wall, (x_pix, y_pix))
                elif sprite == "S":
                    window.blit(start, (x_pix, y_pix))
                elif sprite == "M":
                    window.blit(murdoc, (x_pix, y_pix))
                num_column += 1
            num_row += 1


class Character(object):
    """Thanks to this class we'll create our character"""

    def __init__(self, pict, level):
        self.pict = load_pict(pict, sprite_size, sprite_size, True)
        # That's the position of mc gyver (in sprites)
        self.pos_x = 1
        self.pos_y = 1
        # Position in pixels
        self.x_pix = sprite_size
        self.y_pix = sprite_size
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
                    self.x_pix = self.pos_x * sprite_size

        # Move to left side
        if direction == "left":
            if self.pos_x > 0:
                if self.level.maze[self.pos_y][self.pos_x - 1] != "W":
                    self.pos_x -= 1
                    self.x_pix = self.pos_x * sprite_size

        # Move to the top side
        if direction == "up":
            if self.pos_y > 0:
                if self.level.maze[self.pos_y - 1][self.pos_x] != "W":
                    self.pos_y -= 1
                    self.y_pix = self.pos_y * sprite_size

        # Move to the bottom side
        if direction == "down":
            if self.pos_y < (sprites_per_side - 1):
                if self.level.maze[self.pos_y + 1][self.pos_x] != "W":
                    self.pos_y += 1
                    self.y_pix = self.pos_y * sprite_size


class Items(object):
    """This method will randomly create items to pick-up, to win the game"""

    def __init__(self, pict, level):
        self.pict = load_pict("pictures/{}.png".format(pict), sprite_size, sprite_size, True)
        # Picture for check item is smaller
        self.pict_check = load_pict("pictures/{}.png".format(pict), 30, 30, True)
        # Item position in pixels
        self.x_pix = 0
        self.y_pix = 0
        # Item position in spites
        self.pos_x = 0
        self.pos_y = 0
        self.level = level

    def generate_item(self):
        """We generate an item with random position in the maze"""

        loop = 1
        while loop:
            row = random.randint(0, 14)
            column = random.randint(0, 14)
            if self.level.maze[row][column] == "0":
                self.pos_y = row
                self.pos_x = column
                self.y_pix = row * sprite_size
                self.x_pix = column * sprite_size
                loop = 0

    def show_item(self, window):
        """We display the item in the maze"""

        window.blit(self.pict, (self.x_pix, self.y_pix))

    def item_check(self, window, pos_x):
        """If player collect an item, we display it on the top list"""

        window.blit(self.pict_check, (pos_x, 8))
