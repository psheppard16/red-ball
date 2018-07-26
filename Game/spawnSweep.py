__author__ = 'psheppard16'
import math
class SpawnSweep:
    def __init__(self, window):
        self.window = window
        self.spawnSweep = 1.0
        self.radius = 1
        self.x = 0
        self.y = 0

    def run(self):
        if self.spawnSweep <= 0:
            self.spawnSweep = 1.0
        else:
            self.spawnSweep -= self.window.frameRate.TICK_SPEED * 5 #moves spawn zone back and forth, should be relocated
        scale = self.window.gameEngine.scaleEngine.scale
        player = self.window.gameEngine.character
        h = math.sqrt(player.getXSpeed() ** 2 + player.getYSpeed() ** 2)
        if h == 0:
            h = .001
        xComp = player.getXSpeed() / h
        yComp = player.getYSpeed() / h
        yCenterOfScreen = self.window.width * 2 / 5
        xCenterOfScreen = 0
        self.x = player.x + (yCenterOfScreen + self.window.width / 2 * xComp * self.spawnSweep) / scale
        self.y = player.y + (xCenterOfScreen + self.window.width / 2 * yComp * self.spawnSweep) / scale
        self.radius = self.window.width / 2 / scale + 500


