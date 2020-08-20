import pygame, sys
import level, player
from main import Button
import vectormath

pygame.init()

g = vectormath.vector.Vector2(0, 2)

size_screen = 1280, 720
size_buttons = 300, 50
size = 1280, 20
pos = 0, 690
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

screen = pygame.display.set_mode(size_screen, 0, 32)
rect = pygame.Rect(pos, size)
player = player.Player(20, 0, g)
level = level.Level([player, rect])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    pygame.draw.rect(screen, blue, rect)
    player.draw(screen, white)
    player.move()
    pygame.display.update()