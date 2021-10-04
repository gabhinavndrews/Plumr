import pygame
import sys

pygame.init()   # initializing pygame
sys.init() # initializing sys

pygame.display.set_caption('Plumbr')    # creating title of game
WIDTH, HEIGHT = 900, 500    # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))   # creating window

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False