__author__ = 'psheppard16'
import math
from GameObjects.mobile import Mobile
class Star(Mobile):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.window = window
        self.radius = 100
        self.alive = True
        self.angle = 0
        self.cannotDespawn = 0
        self.pointList = []
        self.largeRadius = True
        for angle in range(0, 360, 36):
            if self.largeRadius:
                self.largeRadius = False
                x = self.radius * math.sin(angle) * self.window.gameEngine.scaleEngine.getScale()
                y = self.radius * math.cos(angle) * self.window.gameEngine.scaleEngine.getScale()
            else:
                self.largeRadius = True
                x = self.radius * math.sin(angle) * self.window.gameEngine.scaleEngine.getScale() / 2
                y = self.radius * math.cos(angle) * self.window.gameEngine.scaleEngine.getScale() / 2
            self.pointList.append((x, y))

    def run(self, p, localScale, width, distance, TICK_SPEED):
        #rotate star
        if self.angle < 360 + 360 * self.window.frameRate.TICK_SPEED:
            self.angle += 180 * self.window.frameRate.TICK_SPEED
        else:
            self.angle = 0

        #check for despawn
        self.cannotDespawn -= TICK_SPEED
        if distance(p.x, p.y, self.x, self.y) < p.radius + self.radius:
            self.alive = False
            p.stars += 1
        if distance(p.x + width * 5 / 4 / localScale, p.y, self.x, self.y) > width * 1.5 / localScale and self.cannotDespawn < 0:
            self.alive = False

        #update outline
        self.pointList.clear()
        for angle in range(0, 360, 36):
            if self.largeRadius:
                self.largeRadius = False
                x = self.radius * math.sin(math.radians(angle - self.angle)) * self.window.gameEngine.scaleEngine.getScale()
                y = self.radius * math.cos(math.radians(angle - self.angle)) * self.window.gameEngine.scaleEngine.getScale()
            else:
                self.largeRadius = True
                x = self.radius * math.sin(math.radians(angle - self.angle)) * self.window.gameEngine.scaleEngine.getScale() / 2
                y = self.radius * math.cos(math.radians(angle - self.angle)) * self.window.gameEngine.scaleEngine.getScale() / 2
            self.pointList.append((x, y))