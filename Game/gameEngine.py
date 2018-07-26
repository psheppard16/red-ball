from GameObjects.character import *
from GameObjects.blob import *
from GameObjects.blackHole import *
from GameObjects.speedGate import *
from GameObjects.star import Star
from GameObjects.fuelCan import FuelCan
from GameObjects.shield import Shield
from Display.prediction import *
from Display.scaling import Scale
from Game.spawnSweep import SpawnSweep
class GameEngine:
    def __init__(self, window):
        self.window = window
        self.scaleEngine = Scale(self.window.save.debugMode)
        self.blobList = []
        self.blackHoleList = []
        self.predictionList = []
        self.speedGateList = []
        self.fuelCanList = []
        self.launchPadList = []
        self.shieldList = []
        self.starList = []
        self.predictionUpdate = 0
        self.lowestX = 0
        self.largestX = 0
        self.lowestY = 0
        self.largestY = 0
        self.character = Character(self.window)
        self.spawnSweep = SpawnSweep(self.window)
        if self.character.getXSpeed() > 0:
            self.predictionsSecAhead = self.window.width * self.scaleEngine.getScale() / self.character.getXSpeed()
        else:
            self.predictionsSecAhead = 10
        self.lastPredictionTime = -1 * self.predictionsSecAhead
        self.spawnGrid = {}

    def runGame(self):
        self.window.frameRate.startTimer("setScale")
        self.setScale()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("spawnElements")
        self.runSpawnSweep()
        self.spawnElements()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runBlob")
        self.runBlobs()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runGates")
        self.runGates()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runBlackHoles")
        self.runBlackHoles()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runFuelCans")
        self.runFuelCans()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runLaunchPads")
        self.runLaunchPads()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runShields")
        self.runShields()
        self.window.frameRate.timeChange()
        self.window.frameRate.startTimer("runStars")
        self.runStars()
        self.window.frameRate.timeChange()
        if self.window.frameRate.loadTime < 0:
            if self.window.save.starPredictionLevel == 5:
                self.window.frameRate.startTimer("runPredictions")
                self.runPredictions()
                self.window.frameRate.timeChange()
            self.window.frameRate.startTimer("runPlayer")
            self.runPlayer()
            self.window.frameRate.timeChange()
        self.window.save.mass = self.character.requestedMass - self.character.startMass
        self.window.frameRate.getLongestTask()

    def setScale(self):
        self.scaleEngine.setScale(self.window.height, self.character.radius, self.window.save.smoothScale, self.window.save.debugMode)

    def runPredictions(self):
        self.predictionsSecAhead = self.window.width / self.window.gameEngine.scaleEngine.scale / abs(self.character.getXSpeed()) * 2
        if self.predictionsSecAhead > 10:
            self.predictionsSecAhead = 10
        if self.character.y > self.character.radius:
            self.predictionList.clear()
            for b in range(0, int(self.predictionsSecAhead / self.window.save.predictionQuality), 1):
                self.predictionList.append(Prediction(self.window, self.character, b * self.window.save.predictionQuality))
            lastBounce = 0
            for b in range(len(self.predictionList)):
                if self.predictionList[b].bounceNumber > lastBounce:
                    self.predictionList.insert(b, Prediction(self.window, self.character, self.predictionList[b].totalTime))
                    lastBounce += 1

    def runBlobs(self):
        for b in self.blobList:
            b.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for b in self.blobList:
            if not b.alive:
                self.blobList.remove(b)
                del b

    def runFuelCans(self):
        for f in self.fuelCanList:
            f.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for f in self.fuelCanList:
            if not f.alive:
                self.fuelCanList.remove(f)
                del f

    def runBlackHoles(self):
        for h in self.blackHoleList:
            h.run(self.blackHoleList, self.blobList, self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for h in self.blackHoleList:
            if not h.alive:
                self.blackHoleList.remove(h)
                del h

    def runLaunchPads(self):
        for l in self.launchPadList:
            l.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for l in self.launchPadList:
            if not l.alive:
                self.launchPadList.remove(l)
                del l

    def runShields(self):
        for sh in self.shieldList:
            sh.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for sh in self.shieldList:
            if not sh.alive:
                self.shieldList.remove(sh)
                del sh

    def runStars(self):
        for s in self.starList:
            s.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for s in self.starList:
            if not s.alive:
                self.starList.remove(s)
                del s

    def runGates(self):
        for g in self.speedGateList:
            g.run(self.character, self.window.gameEngine.scaleEngine.getScale(), self.window.width, self.distance, self.window.frameRate.TICK_SPEED)
        for g in self.speedGateList:
            if not g.alive:
                self.speedGateList.remove(g)
                del g

    def runSpawnSweep(self):
        self.spawnSweep.run()

    def runPlayer(self):
        self.character.run()

    def spawnElements(self):
        #checks to see whether player is within 10000 pixels of each grid
        p = self.character
        scale = self.window.gameEngine.scaleEngine.getScale()
        self.lowestX = math.floor(p.x / 1000) - int(1 / math.sqrt(scale) * 5) #only checks in small area around player
        if self.lowestX < 0:
            self.lowestX = 0
        self.largestX = self.lowestX + int(1 / math.sqrt(scale) * 5) * 2
        self.lowestY = math.floor(p.y / 1000) - int(1 / math.sqrt(scale) * 5) #not finished -doesnt work corectly on large scales
        if self.lowestY < 0:
            self.lowestY = 0
        self.largestY = self.lowestY + int(1 / math.sqrt(scale) * 5) * 2
        for i in range(self.lowestX, self.largestX):
            for j in range(self.lowestY, self.largestY):
                if self.distance(self.spawnSweep.x, self.spawnSweep.y, i * 1000 + 500, j * 1000 + 500) < self.spawnSweep.radius:
                    try:
                        hasSpawned = self.spawnGrid[(i, j)]
                    except:
                        hasSpawned = False
                        self.spawnGrid[(i, j)] = False
                    if not hasSpawned:
                        #sets spawnGrid of i, j to true, indicating it has spawned
                        self.spawnGrid[(i, j)] = True
                        #spawns blobs in that area
                        lowestX = i * 1000
                        largestX = lowestX + 1000
                        lowestY = j * 1000
                        largestY = lowestY + 1000
                        #spawn number based off of distance from 0,0
                        for l in range(0, 2):
                            x = random.randint(lowestX, largestX)
                            y = random.randint(lowestY, largestY)
                            self.blobList.append(Blob(self.window, x, y, 0, 0, 50 * (1 + 2 *random.random() * ((i ** .3 + 1) * (j ** .3 + 1)))))

                        multiplier = 1
                        for o in range(0, int(100 / (i ** .2 + j ** .2 + 20))): #larger second term lowers chance of virus(so higher i, j raises)
                            multiplier *= random.randint(0, 1)
                        for t in range(0, random.randint(1, 3) * multiplier): #1-3 possilbe number of viruses
                            if random.randint(0, 10) > 9:
                                x = random.randint(lowestX, largestX)
                                y = random.randint(lowestY, largestY)
                                self.blackHoleList.append(BlackHole(self.window, x, y))

                        multiplier = 1
                        for o in range(0, int(100 / (i ** .2 + j ** .2 + 40))): #larger second term lowers chance of speedgates(so higher i, j raises)
                            multiplier *= random.randint(0, 1)
                        for s in range(0, random.randint(1, 3) * multiplier): #1-3 possilbe number of speedgates
                            if random.randint(0, 10) > 9:
                                x = random.randint(lowestX, largestX)
                                y = random.randint(lowestY, largestY)
                                self.speedGateList.append(SpeedGate(self.window, x, y))

                        multiplier = 1
                        for o in range(0, int(100 / (i ** .2 + j ** .2 + 40))): #larger second term lowers chance of speedgates(so higher i, j raises)
                            multiplier *= random.randint(0, 1)
                        for s in range(0, random.randint(1, 3) * multiplier): #1-3 possilbe number of speedgates
                            if random.randint(0, 10) > 9:
                                x = random.randint(lowestX, largestX)
                                y = random.randint(lowestY, largestY)
                                self.starList.append(Star(self.window, x, y))

                        multiplier = 1
                        for o in range(0, int(100 / (i ** .2 + j ** .2 + 20))): #larger second term lowers chance of speedgates(so higher i, j raises)
                            multiplier *= random.randint(0, 1)
                        for s in range(0, random.randint(1, 3) * multiplier): #1-3 possilbe number of speedgates
                            if random.randint(0, 10) > 9:
                                x = random.randint(lowestX, largestX)
                                y = random.randint(lowestY, largestY)
                                self.fuelCanList.append(FuelCan(self.window, x, y))

                        multiplier = 1
                        for o in range(0, int(100 / (i ** .2 + j ** .2 + 40))): #larger second term lowers chance of speedgates(so higher i, j raises)
                            multiplier *= random.randint(0, 1)
                        for s in range(0, random.randint(1, 3) * multiplier): #1-3 possilbe number of speedgates
                            if random.randint(0, 10) > 9:
                                x = random.randint(lowestX, largestX)
                                y = random.randint(lowestY, largestY)
                                self.shieldList.append(Shield(self.window, x, y))

    def endGame(self):
        p = self.character
        for b in self.blobList:
            del b
        for v in self.blackHoleList:
            del v
        for z in self.predictionList:
            del z
        self.window.save.stars += p.stars
        self.window.frameRate.loadTime = 2

    def kp(self, event):
        p = self.character
        if event.char == " ":
            p.rocket = True

    def kr(self, event):
        p = self.character
        if event.char == " ":
            p.rocket = False

    def distance(self, x1, y1, x2, y2):
        xD = x1 - x2
        yD = y1 - y2
        return math.sqrt(xD ** 2 + yD ** 2)







