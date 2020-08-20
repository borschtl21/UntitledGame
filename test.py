import pygame, sys
import level, player
from main import Button
import vectormath

pygame.init()

g = vectormath.vector.Vector2(0, 1)

size_screen = 1280, 720
size_buttons = 300, 50
size_player = 100, 100
size = 1280, 20
pos = 0, 690
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

screen = pygame.display.set_mode(size_screen, 0, 32)
rect = pygame.Rect(pos, size)
player1 = player.Player(20, 20, g, size_player)



while 1:
    screen.fill(black)

    pygame.draw.rect(screen, blue, rect)


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('a')
                player1.vel = vectormath.vector.Vector2(-1, 0)
            if event.key == pygame.K_d:
                print('d')
                player1.vel = vectormath.vector.Vector2(1, 0)
            if event.key == pygame.K_w:
                print('w')
                player1.vel = vectormath.vector.Vector2(0, -1)
            if event.key == pygame.K_s:
                print('s')
                player1.vel = vectormath.vector.Vector2(0, 1)

    player1.draw(screen, white)

    if not player1.is_collided(rect):
        player1.move()
    else:
        player1.vel = vectormath.vector.Vector2()
#    player1.move()

    pygame.display.update()
