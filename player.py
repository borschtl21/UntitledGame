import physik
import pygame
# hier alles was  der player in game dann macht verusacht ereleidet

size = 50, 50


class Player(physik.PhysicsObj):
    def __init__(self, x_global, y_global, vel):
        super().__init__(x_global, y_global, vel)
        self.rect = pygame.Rect((self.x_global, self.y_global), size)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, self.rect)

    def move(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y




if __name__ == '__main__':
    import pygame
