import math
class Point:
    def __init__(self, radius, theta, window, mode):
        self.window = window
        self.radius = radius
        self.angle = theta
        self.mode = mode
        self.x = radius * math.cos(math.radians(self.angle))
        self.y = radius * math.sin(math.radians(self.angle))
        self.lostRadius = 0

    def run(self, lostRadius):
        c = self.window.gameEngine.character
        if self.mode == "simple": #this is the more framerate efficient method- not as good looking
            self.radius = c.radius * 1.25 + lostRadius / 360
            self.x = self.radius * math.cos(math.radians(self.angle))
            self.y = self.radius * math.sin(math.radians(self.angle))
            if c.y + self.y < 0:
                self.y = 0 - c.y
                self.x = self.radius * math.cos(math.radians(self.angle))
        else:
            self.radius = c.radius * 1.25 + lostRadius / 360
            if self.window.distance(0, 0, self.x, self.y) < self.radius:
                self.y += self.radius * math.sin(math.radians(self.angle)) * self.window.frameRate.TICK_SPEED * 10
                self.x += self.radius * math.cos(math.radians(self.angle)) * self.window.frameRate.TICK_SPEED * 10
            if self.window.distance(0, 0, self.x, self.y) >= self.radius * .9:
                self.x = self.radius * math.cos(math.radians(self.angle))
                self.y = self.radius * math.sin(math.radians(self.angle))
            if c.y + self.y < 0:
                self.y = 0 - c.y
            self.lostRadius = self.radius - self.window.distance(0, 0, self.x, self.y)
