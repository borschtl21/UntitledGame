import physik
import pygame
# hier alles was  der player in game dann macht verusacht ereleidet




class Player(physik.PhysicsObj):
    def __init__(self, x_global, y_global, vel, size):
        super().__init__(x_global, y_global, vel, size)

#    def move(self):
#        self.rect.x += self.vel.x
#        self.rect.y += self.vel.y

    def jump(self):
        self.y_global += 100




if __name__ == '__main__':
    import pygame
