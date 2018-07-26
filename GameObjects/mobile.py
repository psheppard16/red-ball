__author__ = 'psheppard16'
import math
class Mobile:
    def __init__(self, window, x, y, xVel, yVel):
        self.window = window
        self.xVel = xVel
        self.yVel = yVel
        self.x = x
        self.y = y
        self.xForce = 0
        self.yForce = 0
        self.shiftedX = 0
        self.shiftedY = 0 #shifted x and y are for predicting trajectory correcly by accounting for reocket movement

    def move(self): #move must be called before forces and shifts are applied to an object
        self.x += self.getXDisplacement(self.window.frameRate.TICK_SPEED)
        self.y += self.getYDisplacement(self.window.frameRate.TICK_SPEED)
        self.xVel += self.xForce * self.window.frameRate.TICK_SPEED
        self.yVel += self.yForce * self.window.frameRate.TICK_SPEED
        self.shiftedX = 0
        self.shiftedY = 0
        self.xForce = 0
        self.yForce = 0

    def accelerate(self, xForce, yForce): #forces in change in velocity per second
        self.xForce += xForce
        self.yForce += yForce

    def setSpeed(self, xVel, yVel):
        self.yVel = yVel
        self.xVel = xVel

    def setPosition(self, xPos, yPos):
        self.x = xPos
        self.y = yPos

    def changePosition(self, xChange, yChange):
        self.shiftedX += xChange
        self.shiftedY += yChange

    def getXSpeed(self):
        return self.xVel + self.shiftedX

    def getYSpeed(self):
        return self.yVel + self.shiftedY

    def getXVel(self):
        return self.xVel

    def getYVel(self):
        return self.yVel

    def getSpeed(self):
        return math.sqrt(self.yVel ** 2 + self.xVel ** 2)

    def getXDisplacement(self, seconds):
        return self.getXSpeed() * seconds + math.copysign(.5 * self.xForce * seconds ** 2, self.xForce)

    def getYDisplacement(self, seconds):
        return self.getYSpeed() * seconds + math.copysign(.5 * self.yForce * seconds ** 2, self.yForce)

    def getAngle(self):
        return math.degrees(math.atan2(self.getYSpeed(), self.getXSpeed()))