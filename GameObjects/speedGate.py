__author__ = 'psheppard16'
import math

from GameObjects.mobile import Mobile


class SpeedGate(Mobile):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.sweepX = self.x
        self.sweepY = self.y
        self.cap1X = self.x
        self.cap1Y = self.y
        self.cap2X = self.x
        self.cap2Y = self.y
        self.angle = 90
        self.alive = True
        self.sweep = -.8
        self.sweepRadius = 10
        self.capRadius = 25
        self.cannotDespawn = 0
        self.length = 1000

    def run(self, p, localScale, width, distance, TICK_SPEED):
        self.sweepRadius = 10
        self.capRadius = 30
        self.length = 450
        if self.sweep + 10 * TICK_SPEED < .8:
            self.sweep += 10 * TICK_SPEED
        else:
            self.sweep = -.8
        self.cannotDespawn -= TICK_SPEED
        self.angle = p.getAngle() - 90
        self.cap1X = self.x + .5 * self.length * math.cos(math.radians(self.angle))
        self.cap1Y = self.y + .5 * self.length * math.sin(math.radians(self.angle))
        self.cap2X = self.x - .5 * self.length * math.cos(math.radians(self.angle))
        self.cap2Y = self.y - .5 * self.length * math.sin(math.radians(self.angle))
        self.sweepX = self.x + .5 * self.length * self.sweep * math.cos(math.radians(self.angle))
        self.sweepY = self.y + .5 * self.length * self.sweep * math.sin(math.radians(self.angle))
        self.sweepX2 = self.x + .5 * self.length * -self.sweep * math.cos(math.radians(self.angle))
        self.sweepY2 = self.y + .5 * self.length * -self.sweep * math.sin(math.radians(self.angle))
        if distance(p.x, p.y, self.cap1X, self.cap1Y) < p.radius + self.capRadius:
            self.alive = False
        if distance(p.x, p.y, self.cap2X, self.cap2Y) < p.radius + self.capRadius:
            self.alive = False
        if distance(p.x, p.y, self.sweepX, self.sweepY) < p.radius + self.sweepRadius or distance(p.x, p.y, self.sweepX2, self.sweepY2) < p.radius + self.sweepRadius:
            xAcc = (self.window.save.starSpeedGateLevel / 5 + 1) * 100 * p.getXVel() * TICK_SPEED
            yAcc = (self.window.save.starSpeedGateLevel / 5 + 1) * 100 * p.getYVel() * TICK_SPEED
            p.accelerate(xAcc, yAcc)
            p.changePosition(xAcc / 10, yAcc / 10)
        if distance(p.x + width * 5 / 4 / localScale, p.y, self.x, self.y) > width * 1.5 / localScale and self.cannotDespawn < 0:
            self.alive = False