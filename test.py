import pygame, sys
import level, player
from main import Button
import vectormath

pygame.init()

g = vectormath.vector.Vector2(0, 10)

size_screen = 1280, 720
size_buttons = 300, 50
size_player = 100, 100
size = 1280, 20
pos = 0, 690
black = 0, 0, 0
white = 255, 255, 255
blue = 0, 0, 255

# Startwert vom Level einsetzen bevor start, update der Position jeden Frame und Initialisierung eines neuen Player_objs
x_global_player = 20
y_global_player = 20
# gravitation vom Level einsetzen undf jeden Frame updaten
player_velo = g

screen = pygame.display.set_mode(size_screen, 0, 32)
rect = pygame.Rect(pos, size)
player1 = player.Player(20, 20, g, size_player)



while 1:
    screen.fill(black)
    pygame.draw.rect(screen, blue, rect)


    if not player1.is_collided(rect):
        player1.vel.y = g.y

    else:
        player1.vel.y = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print('a')
                player1.vel = vectormath.vector.Vector2(-10, 0)
            if event.key == pygame.K_d:
                print('d')
                player1.vel = vectormath.vector.Vector2(10, 0)
            if event.key == pygame.K_w:
                print('w')
                player1.vel = vectormath.vector.Vector2(0, -50)
            if event.key == pygame.K_s and not player1.is_collided(rect):
                print('s')
                player1.vel = vectormath.vector.Vector2(0, 10)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print('-a')
                player1.vel = vectormath.vector.Vector2(0, 0)
            if event.key == pygame.K_d:
                print('-d')
                player1.vel = vectormath.vector.Vector2(0, 0)
            if event.key == pygame.K_w:
                print('-w')
                player1.vel = vectormath.vector.Vector2(0, 0)
            if event.key == pygame.K_s and not player1.is_collided(rect):
                print('-s')
                player1.vel = vectormath.vector.Vector2(0, 0)

    player1.move()


    player1.draw(screen, white)

    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(30)
