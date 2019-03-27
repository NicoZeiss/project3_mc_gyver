import pygame
from pygame.locals import *
from classes import *
from functions import *

item_list = ["needle", "tube", "ether"]
item_dic = {}

def generate_items(window, maze):
    for item in item_list:
        # We create an object from class Items for each item in the list
        item = Items(item, maze)
        item.generate_item()
        item.show_item(window)
        item_dic[item] = [False]
    return item_dic

def collect_item(char_x, char_y):
    for item in item_dic:
        if char_x == item.pos_x:
            if char_y == item.pos_y:
                item = True
    return item_dic


