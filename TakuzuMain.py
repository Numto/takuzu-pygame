import pygame
from TakuzuFunctions import *

'''
This is the main function of the game. It initializes pygame, windows' size
and windows' title then call the main menu function
all game's functions are located in a separate file TakuzuFunctions.py
For more details, please find the technical document
'''

def MainFunc():
    
    pygame.init()
    
    DisplayMainMenu()

MainFunc()
