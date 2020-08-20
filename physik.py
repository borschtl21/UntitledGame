import vectormath
import pygame


class PhysicsObj:
    def __init__(self, x_global, y_global, vel, size, grav=True):
        self.rect = pygame.Rect(x_global, y_global, size[0], size[1])
        self.x_global = x_global
        self.y_global = y_global
        self.vel = vel
        self.feel_grav = grav

    def move(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def is_collided(self, object2):
        return self.rect.colliderect(object2)

