#!/usr/bin/python3
# -*- coding: Utf-8 -*-

import pygame

"""Here, you will find some functions we will use in main.py"""

def win_message(window):
	font = pygame.font.Font(None, 50)
	win_mess = font.render("YOU WIN !!!", 1, (255,255,255))
	window.blit(win_mess, (200,200))

