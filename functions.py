#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import pygame

from constants import *

# pygame.init()

"""Here, you will find some functions we will use in main.py"""

def win_message(window):
	font = pygame.font.Font(None, 50)
	win_mess = font.render("YOU WIN !!!", 1, (255,255,255))
	window.blit(win_mess, (200,200))

def load_pict(pict, x, y, alpha):
	"""This function will load pict and convert them to the right size. 
	Pict arg is the name of the pict
	x and y args are the required size
	alpha is a bolean which let us know if we have to convert_alpha the pict"""

	if alpha == True:
		object_pict = pygame.image.load(pict).convert_alpha()
		resized_pict = pygame.transform.scale(object_pict, (x,y))
	else:
		object_pict = pygame.image.load(pict).convert()
		resized_pict = pygame.transform.scale(object_pict, (x,y))
	return resized_pict

