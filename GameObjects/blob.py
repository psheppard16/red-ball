__author__ = 'psheppard16'
import random
import math
from GameObjects.mobile import Mobile
class Blob(Mobile):
    def __init__(self, window, x, y, xVel, yVel, mass):
        super().__init__(window, x, y, xVel, yVel)
        self.mass = mass
        self.window = window
        self.startRadius = math.sqrt(self.mass / math.pi)
        self.radius = self.startRadius
        self.radiusOsc = 1.0
        self.grow = True
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 128, 0), (255, 255, 0), (0, 255, 255), (128, 0, 255), (255, 0, 255)]
        self.color = random.choice(self.colors)
        self.alive = True
        self.cannotDespawn = 0

    def run(self, p, localScale, width, distance, TICK_SPEED):
        self.cannotDespawn -= TICK_SPEED
        if self.grow:
            self.radiusOsc += 3.0 * self.window.frameRate.TICK_SPEED
        else:
            self.radiusOsc -= 3.0 * self.window.frameRate.TICK_SPEED
        if self.radiusOsc > 1.25 and self.grow:
            self.radiusOsc = 1.25
            self.grow = False
        if self.radiusOsc < .75 and not self.grow:
            self.radiusOsc = .75
            self.grow = True
        self.radius = self.startRadius * self.radiusOsc * 2
        if distance(p.x, p.y, self.x, self.y) < p.radius + self.radius:
            p.addMass(self.mass * p.growthRate)
            self.alive = False
        self.move()
        if distance(p.x + width * 5 / 4 / localScale, p.y, self.x, self.y) > width * 1.5 / localScale and self.cannotDespawn < 0:
            self.alive = False