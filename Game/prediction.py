__author__ = 'psheppard16'
import math
class Prediction:
    def __init__(self, window, p, secondsAhead):
        self.radius = 10
        self.window = window
        self.p = p
        self.secondsAhead = secondsAhead
        self.alive = True
        self.y = self.p.y + self.p.getYVel() * self.secondsAhead - .5 * self.p.GRAVITY * self.p.antiGrav * self.secondsAhead ** 2
        self.x = self.p.x + self.p.getXVel() * self.secondsAhead
        self.bounceNumber = 0
        self.totalTime = 0
        self.ySpeedAtStart = 0
        self.xSpeedAtStart = 0
        self.timeToZero = 0
        self.lastTimeToZero = 0
        while self.y < self.p.radius and self.bounceNumber < 10:
            if self.bounceNumber == 0:
                self.x = self.p.x
                #finds the velocity of the player just before they hit the ground
                ySpeed = abs(self.p.getYVel())
                yDisplacement = abs(self.p.radius - self.p.y)
                self.ySpeedAtStart = math.sqrt(ySpeed ** 2 + (self.p.GRAVITY * self.p.antiGrav) * 2 * yDisplacement)
                self.xSpeedAtStart = self.p.getXVel()

                #finds the time it will take fore the player to hit the ground
                if self.p.getYVel() < 0:
                    self.timeToZero = abs((ySpeed - self.ySpeedAtStart) / (self.p.GRAVITY * self.p.antiGrav))
                else:
                    self.timeToZero = 2 * abs(self.ySpeedAtStart) / (self.p.GRAVITY * self.p.antiGrav) - abs((ySpeed - self.ySpeedAtStart) / (self.p.GRAVITY * self.p.antiGrav))
            else:
                ySpeedAtBounce = abs(self.ySpeedAtStart * (1.0 - .3 * self.p.friction) ** self.bounceNumber)
                self.timeToZero = 2 * ySpeedAtBounce / (self.p.GRAVITY * self.p.antiGrav)

            self.bounceNumber += 1
            self.totalTime += self.timeToZero
            timeAfterBounce = self.secondsAhead - self.totalTime
            ySpeedAtBounce = abs(self.ySpeedAtStart * (1.0 - .3 * self.p.friction) ** self.bounceNumber)
            self.y = ySpeedAtBounce * timeAfterBounce - .5 * (self.p.GRAVITY * self.p.antiGrav) * timeAfterBounce ** 2 + self.p.radius

            xSpeedAtBounce = self.xSpeedAtStart * (1.0 - .3 * self.p.friction) ** (self.bounceNumber - 1)
            self.x += xSpeedAtBounce * self.timeToZero
        self.x += self.xSpeedAtStart * (1.0 - .3 * self.p.friction) ** self.bounceNumber * (self.secondsAhead - self.totalTime)
        if self.y < self.p.radius:
            self.y = self.p.radius