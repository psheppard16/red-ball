__author__ = 'psheppard16'
import math
class Prediction:
    def __init__(self, window, p, secondsAhead):
        self.radius = 10
        self.window = window
        self.p = p
        self.secondsAhead = secondsAhead
        self.alive = True
        self.y = self.p.y + self.p.getYDisplacement(secondsAhead)
        self.x = self.p.x + self.p.getXDisplacement(secondsAhead)
        self.bounceNumber = 0
        self.totalTime = 0
        self.ySpeedAtStart = 0
        self.xSpeedAtStart = 0
        self.timeToZero = 0
        self.lastTimeToZero = 0
        if self.p.yForce < 0:
            while self.y < self.p.radius and self.bounceNumber < 10:
                if self.bounceNumber == 0:
                    self.x = self.p.x
                    #finds the velocity of the player just before they hit the ground
                    ySpeed = abs(self.p.getYVel())
                    yDisplacement = abs(self.p.radius - self.p.y)
                    self.ySpeedAtStart = math.sqrt(ySpeed ** 2 + abs(self.p.yForce) * 2 * yDisplacement)
                    self.xSpeedAtStart = self.p.getXVel()

                    #finds the time it will take fore the player to hit the ground
                    if self.p.getYVel() < 0:
                        self.timeToZero = abs((ySpeed - self.ySpeedAtStart) / abs(self.p.yForce))
                    else:
                        self.timeToZero = 2 * abs(self.ySpeedAtStart) / abs(self.p.yForce) - abs((ySpeed - self.ySpeedAtStart) / abs(self.p.yForce))
                else:
                    self.timeToZero = 2 * self.ySpeedAtStart / abs(self.p.yForce)
                self.bounceNumber += 1
                self.totalTime += self.timeToZero


                #updates the x position according to the last timeToZero calculated, placing the start of the bounce at the correct position
                self.x += self.xSpeedAtStart * self.timeToZero + .5 * self.p.xForce * self.timeToZero ** 2

                #updates the x speed so that it is correct for after the bounce
                self.xSpeedAtStart += self.p.xForce * self.timeToZero
                self.xSpeedAtStart *= (1.0 - .3 * self.p.friction)


                #calculates the y position assuming there are no more bounces, if there are, the y will be negative, and the loop will continue
                leftOverTime = self.secondsAhead - self.totalTime
                self.ySpeedAtStart *= (1.0 - .3 * self.p.friction)
                self.y = self.ySpeedAtStart * leftOverTime + .5 * self.p.yForce * leftOverTime ** 2 + self.p.radius
            #since x position is one bounce behind, a final adjustment must be made
            self.leftOverTime = self.secondsAhead - self.totalTime
            self.x += self.xSpeedAtStart * self.leftOverTime + .5 * self.p.xForce * self.leftOverTime ** 2
        if self.y < p.radius:
            self.y = p.radius