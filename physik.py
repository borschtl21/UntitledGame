import vectormath


class PhysicsObj:
    def __init__(self, x_global, y_global, vel):
        self.x_global = x_global
        self.y_global = y_global
        self.vel = vel

    def move(self):
        pass
