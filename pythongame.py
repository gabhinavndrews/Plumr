import pygame
import sys

pygame.init()   # initializing pygame

pygame.display.set_caption('Plumbr')    # creating title of game
favicon = pygame.image.load('pipe.png') # favicon  
pygame.display.set_icon(favicon)

WIDTH, HEIGHT = 900, 500    # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))   # creating window

background = pygame.image.load("plumbrback.png")

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill((255,255,255))
    pygame.display.update()

    pygame.gameDisplay.blit(background, (0,0))