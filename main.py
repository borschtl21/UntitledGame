import pygame
from pygame.locals import *
import sys

pygame.init()
size = width, height = 320, 240
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255


screen = pygame.display.set_mode(size, 0, 32)
screen.fill(black)


def mainloop():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            pygame.draw.rect(screen, white, (0, 0, 100, 100))
            pygame.draw.rect(screen,white, (150, 0, 100, 100))
            pygame.display.update()


if __name__ == '__main__':
    mainloop()
