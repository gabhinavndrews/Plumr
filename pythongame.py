import pygame
import sys

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

# game loop
running = True
while running:
    # RUN ALL GAME CODE BELOW THIS !!!!!!!!!!
    # level 1
    #column 1
    window.blit(straight_pipe, (25, 50))
    window.blit(straight_pipe, (25, 100))
    window.blit(straight_pipe, (25, 150))
    window.blit(straight_pipe, (25, 200))
    window.blit(straight_pipe, (25, 250))
    window.blit(straight_pipe, (25, 300))
    window.blit(straight_pipe, (25, 350))
    window.blit(straight_pipe, (25, 400))
    window.blit(straight_pipe, (25, 450))
    #column 2
    window.blit(straight_pipe, (75, 50))
    window.blit(straight_pipe, (75, 100))
    window.blit(straight_pipe, (75, 150))
    window.blit(straight_pipe, (75, 200))
    window.blit(straight_pipe, (75, 250))
    window.blit(straight_pipe, (75, 300))
    window.blit(straight_pipe, (75, 350))
    window.blit(straight_pipe, (75, 400))
    window.blit(straight_pipe, (75, 450))
    #column 3
    window.blit(straight_pipe, (125, 50))
    window.blit(straight_pipe, (125, 100))
    window.blit(straight_pipe, (125, 150))
    window.blit(straight_pipe, (125, 200))
    window.blit(straight_pipe, (125, 250))
    window.blit(straight_pipe, (125, 300))
    window.blit(straight_pipe, (125, 350))
    window.blit(straight_pipe, (125, 400))
    window.blit(straight_pipe, (125, 450))
    #column 4
    window.blit(straight_pipe, (175, 50))
    window.blit(straight_pipe, (175, 100))
    window.blit(straight_pipe, (175, 150))
    window.blit(straight_pipe, (175, 200))
    window.blit(straight_pipe, (175, 250))
    window.blit(straight_pipe, (175, 300))
    window.blit(straight_pipe, (175, 350))
    window.blit(straight_pipe, (175, 400))
    window.blit(straight_pipe, (175, 450))
    #column 5
    window.blit(straight_pipe, (225, 50))
    window.blit(straight_pipe, (225, 100))
    window.blit(straight_pipe, (225, 150))
    window.blit(straight_pipe, (225, 200))
    window.blit(straight_pipe, (225, 250))
    window.blit(straight_pipe, (225, 300))
    window.blit(straight_pipe, (225, 350))
    window.blit(straight_pipe, (225, 400))
    window.blit(straight_pipe, (225, 450))
    #column 6
    window.blit(straight_pipe, (275, 50))
    window.blit(straight_pipe, (275, 100))
    window.blit(straight_pipe, (275, 150))
    window.blit(straight_pipe, (275, 200))
    window.blit(straight_pipe, (275, 250))
    window.blit(straight_pipe, (275, 300))
    window.blit(straight_pipe, (275, 350))
    window.blit(straight_pipe, (275, 400))
    window.blit(straight_pipe, (275, 450))
    # column 7
    window.blit(straight_pipe, (325, 50))
    window.blit(straight_pipe, (325, 100))
    window.blit(straight_pipe, (325, 150))
    window.blit(straight_pipe, (325, 200))
    window.blit(straight_pipe, (325, 250))
    window.blit(straight_pipe, (325, 300))
    window.blit(straight_pipe, (325, 350))
    window.blit(straight_pipe, (325, 400))
    window.blit(straight_pipe, (325, 450))
    # column 8
    window.blit(straight_pipe, (375, 50))
    window.blit(straight_pipe, (375, 100))
    window.blit(straight_pipe, (375, 150))
    window.blit(straight_pipe, (375, 200))
    window.blit(straight_pipe, (375, 250))
    window.blit(straight_pipe, (375, 300))
    window.blit(straight_pipe, (375, 350))
    window.blit(straight_pipe, (375, 400))
    window.blit(straight_pipe, (375, 450))
    # column 9
    window.blit(straight_pipe, (425, 50))
    window.blit(straight_pipe, (425, 100))
    window.blit(straight_pipe, (425, 150))
    window.blit(straight_pipe, (425, 200))
    window.blit(straight_pipe, (425, 250))
    window.blit(straight_pipe, (425, 300))
    window.blit(straight_pipe, (425, 350))
    window.blit(straight_pipe, (425, 400))
    window.blit(straight_pipe, (425, 450))
    # column 10
    window.blit(straight_pipe, (475, 50))
    window.blit(straight_pipe, (475, 100))
    window.blit(straight_pipe, (475, 150))
    window.blit(straight_pipe, (475, 200))
    window.blit(straight_pipe, (475, 250))
    window.blit(straight_pipe, (475, 300))
    window.blit(straight_pipe, (475, 350))
    window.blit(straight_pipe, (475, 400))
    window.blit(straight_pipe, (475, 450))
    # column 11
    window.blit(straight_pipe, (525, 50))
    window.blit(straight_pipe, (525, 100))
    window.blit(straight_pipe, (525, 150))
    window.blit(straight_pipe, (525, 200))
    window.blit(straight_pipe, (525, 250))
    window.blit(straight_pipe, (525, 300))
    window.blit(straight_pipe, (525, 350))
    window.blit(straight_pipe, (525, 400))
    window.blit(straight_pipe, (525, 450))
    # column 12
    window.blit(straight_pipe, (575, 50))
    window.blit(straight_pipe, (575, 100))
    window.blit(straight_pipe, (575, 150))
    window.blit(straight_pipe, (575, 200))
    window.blit(straight_pipe, (575, 250))
    window.blit(straight_pipe, (575, 300))
    window.blit(straight_pipe, (575, 350))
    window.blit(straight_pipe, (575, 400))
    window.blit(straight_pipe, (575, 450))
    # column 13
    window.blit(straight_pipe, (625, 50))
    window.blit(straight_pipe, (625, 100))
    window.blit(straight_pipe, (625, 150))
    window.blit(straight_pipe, (625, 200))
    window.blit(straight_pipe, (625, 250))
    window.blit(straight_pipe, (625, 300))
    window.blit(straight_pipe, (625, 350))
    window.blit(straight_pipe, (625, 400))
    window.blit(straight_pipe, (625, 450))
    # column 14
    window.blit(straight_pipe, (675, 50))
    window.blit(straight_pipe, (675, 100))
    window.blit(straight_pipe, (675, 150))
    window.blit(straight_pipe, (675, 200))
    window.blit(straight_pipe, (675, 250))
    window.blit(straight_pipe, (675, 300))
    window.blit(straight_pipe, (675, 350))
    window.blit(straight_pipe, (675, 400))
    window.blit(straight_pipe, (675, 450))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
pygame.quit()
