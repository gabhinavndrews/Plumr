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


def draw_window(pipe):
    window.fill(COLOUR)
    window.blit(background, (0, 0))
    # RUN ALL GAME CODE BELOW THIS !!!!!!!!!!
    # level 1
    window.blit(pipe, (25, 50))


def rotate_tile(x):
    print(x[0], x[1])
    pipe_copy = straight_pipe.copy()

    pipe_copy = pygame.transform.rotate(pipe_copy, 90)
    return pipe_copy


def main():
    pipe = straight_pipe
    CLOCK = pygame.time.Clock()
    # game loop
    running = True
    while running:
        CLOCK.tick(FPS)
        draw_window(pipe)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_pos = pygame.mouse.get_pos()
                pipe_copy = rotate_tile(Mouse_pos)
                pipe = pipe_copy
                draw_window(pipe)

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
