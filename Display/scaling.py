__author__ = 'psheppard16'
class Scale:
    def __init__(self, debugMode):
        self.debugMode = debugMode
        self.debugScale = .1
        self.scale = 1.0
        self.requestedScale = 1.0

    def setScale(self, windowHeight, radius, smoothScale, debugMode):
        playerRatio = .15 #how much of the screen the player takes up
        self.requestedScale = windowHeight / radius * playerRatio / 2
        if smoothScale:
            self.scale += (self.requestedScale - self.scale) / 6
        else:
            self.scale = self.requestedScale
        if self.scale > 1.0:
            self.scale = 1.0

    def getScale(self):
        if self.debugMode:
            return self.debugScale
        else:
            return self.scale