import pygame
import sys

# game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plumbr")

WHITE = (255, 255, 255)

def window():
    WIN.fill(WHITE)
    pygame.display.update()


def main(): # WINDOW CLOSES IMMEDIATELY 10/4/21 NEEDS FIX
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT():
                    run = False
        pygame.quit()
    except SystemExit:
        pygame.quit()


