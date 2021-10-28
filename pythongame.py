import pygame
import sys
import os

pygame.init()  # initializing pygame

pygame.display.set_caption('Plumr')  # creating title of game

# loading assets
favicon = pygame.image.load('pipe.png')  # favicon
pygame.display.set_icon(favicon)
background = pygame.image.load('PlumrBGNew.png')
straight_pipe = pygame.image.load('StraightPipe.png')
t_pipe = pygame.image.load('TPipe.png')
plus_pipe = pygame.image.load('PlusPipe.png')
curve_pipe = pygame.image.load('CurvedPipe.png')
logo = pygame.image.load('Logo.png')

WIDTH, HEIGHT = 750, 500  # width: 900, height: 500
window = pygame.display.set_mode((WIDTH, HEIGHT))  # creating window
FPS = 60
COLOUR = (0, 0, 0)
pipe = straight_pipe


def draw_window(pipe, coord):
    window.fill(COLOUR)
    window.blit(background, (0, 0))
    # RUN ALL GAME CODE BELOW THIS !!!!!!!!!!
    # level 1
    window.blit(pipe, (coord[0], coord[1]))


def rotate_tile(x, pipe):
    pipe_copy = pipe.copy()
    pipe_copy = pygame.transform.rotate(pipe_copy, 90)
    return pipe_copy


def map_tile(Mouse_pos):
    for i in range(25, 675, 50):
        for j in range(50, 450, 50):
            if(i <= Mouse_pos[0] <= i+50):
                if(j <= Mouse_pos[1] <= j+50):
                    return i, j


def main():
    pipe = curve_pipe
    CLOCK = pygame.time.Clock()
    # game loop
    running = True
    while running:
        CLOCK.tick(FPS)
        draw_window(pipe, (25, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_pos = pygame.mouse.get_pos()
                tile_coordinates = map_tile(Mouse_pos)
                pipe_copy = rotate_tile(Mouse_pos, pipe)
                pipe = pipe_copy
                draw_window(pipe, tile_coordinates)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
