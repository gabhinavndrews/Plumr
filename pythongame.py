import pygame
import sys

pygame.init()   # initializing pygame

pygame.display.set_caption('Plumr')    # creating title of game
favicon = pygame.image.load('pipe.png') # favicon  
pygame.display.set_icon(favicon)

# background
background = pygame.image.load('PlumrBG.png')

WIDTH, HEIGHT = 900, 500    # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))   # creating window

window.fill((0,0,0))
window.blit(background,(0,0))

# game loop
running = True
while running:
    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
