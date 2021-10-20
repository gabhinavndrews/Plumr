import pygame
import sys

from pygame import MOUSEBUTTONDOWN, MOUSEBUTTONUP

pygame.init()  # initializing pygame

pygame.display.set_caption('Plumr')  # creating title of game

# loading assets
favicon = pygame.image.load('pipe.png')  # favicon
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBGNew.png')
straight_pipe = pygame.image.load('StraightPipe.png')
tpipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

WIDTH, HEIGHT = 750, 500  # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))  # creating window

window.fill((0, 0, 0))
window.blit(background, (0, 0))
clicking = False
# game loop
running = True
while running:
    # RUN ALL GAME CODE BELOW THIS !!!!!!!!!!
    # level 1
    # column 1
    y = 25
    for k in range(14):
        x = 50
        for i in range(9):
            window.blit(straight_pipe, (y, x))
            x += 50
        y += 50
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()

    pygame.display.update()
pygame.quit()
