import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 250))
FPSCLOCK = pygame.time.Clock()


def main():

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        pygame.draw.line(SURFACE, (255, 0, 0), (10, 80), (200, 80))

        pygame.draw.line(SURFACE, (255, 0, 0), (10, 150), (200, 150), 15)

        pygame.display.update()
        FPSCLOCK.tick(3)


if __name__ == '__main__':
    main()
