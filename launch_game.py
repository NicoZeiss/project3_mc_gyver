import pygame
from pygame.locals import *
from classes import *
from constants import *




pygame.init()
window = pygame.display.set_mode((675,675))
background = pygame.image.load("pictures/background.png").convert()
window.blit(background, (0,0))
pygame.display.flip()

def main():
	continuer = 1
	while continuer:
		m = Maze("maze.txt")
		m.generate_maze()
		m.show_maze(window)
		for event in pygame.event.get():
			if event.type == QUIT:
				continuer = 0
		pygame.display.flip()

main()
