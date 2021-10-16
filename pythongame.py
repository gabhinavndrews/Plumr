import pygame
import sys

pygame.init()   # initializing pygame

pygame.display.set_caption('Plumr')    # creating title of game

#loading assets
favicon = pygame.image.load('pipe.png') # favicon  
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBG.png')
straight_pipe = pygame.image.load('StraightPipe.png')
tpipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

WIDTH, HEIGHT = 750, 500    # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))   # creating window

window.fill((0,0,0))
window.blit(background,(0,0))

# game loop
running = True
while running:
    # RUN ALL GAME CODE BELOW THIS !!!!!!!!!!
        # level 1
    window.blit(straight_pipe, (10, 0))
    window.blit(straight_pipe,(10, 50))
    window.blit(curve_pipe, (10, 100))
    window.blit(straight_pipe, (50, 100))
    window.blit(curve_pipe,(100,100))
    window.blit(straight_pipe, (100,150))
    window.blit(straight_pipe, (100,200))
    window.blit(straight_pipe, (100,250))
    window.blit(curve_pipe, (100,300))
    window.blit(straight_pipe, (150, 300))
    window.blit(curve_pipe, (200,300))
    window.blit(straight_pipe,(200,250))
    window.blit(curve_pipe, (200,200))
    window.blit(straight_pipe,(250,200))
    window.blit(curve_pipe,(300, 200))
    window.blit(curve_pipe,(300,250))
    window.blit(straight_pipe,(350,250))
    window.blit(straight_pipe,(400,250))
    window.blit(curve_pipe, (450, 250))
    window.blit(straight_pipe,(450, 200))
    window.blit(straight_pipe,(450, 150))
    window.blit(straight_pipe,(450, 100))
    window.blit(curve_pipe, (450, 50))
    window.blit(curve_pipe, (500, 50))
    window.blit(straight_pipe,(500, 100))
    window.blit(straight_pipe,(500, 150))
    window.blit(curve_pipe,(500,200))
    window.blit(straight_pipe,(550, 200))
    window.blit(curve_pipe,(600, 200))
    window.blit(straight_pipe, (600, 250))
    window.blit(straight_pipe, (600, 300))
    window.blit(curve_pipe,(600,350))
    window.blit(straight_pipe,(650,350))
    window.blit(straight_pipe,(700,350))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
