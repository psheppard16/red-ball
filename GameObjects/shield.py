__author__ = 'psheppard16'
from GameObjects.mobile import Mobile
class Shield(Mobile):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = 100
        self.alive = True
        self.cannotDespawn = 0

    def run(self, p, localScale, width, distance, TICK_SPEED):
        self.cannotDespawn -= TICK_SPEED
        if distance(p.x, p.y, self.x, self.y) < p.radius + self.radius:
            self.alive = False
            if p.shield < p.maxShield:
                p.shield += 1
        if distance(p.x + width * 5 / 4 / localScale, p.y, self.x, self.y) > width * 1.5 / localScale and self.cannotDespawn < 0:
            self.alive = False