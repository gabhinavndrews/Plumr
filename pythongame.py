import pygame

# game window
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plumbr")

WHITE = (255, 255, 255)
# events
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        WIN.fill(WHITE)
    
    pygame.quit()
