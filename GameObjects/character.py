__author__ = 'psheppard16'
import platform
from Display.outline import *
from GameObjects.mobile import Mobile
class Character(Mobile):
    def __init__(self, window):
        self.window = window
        self.startMass = 5000
        self.launch = 500 + 250 * window.save.launchLevel
        self.mass = self.startMass + self.window.save.mass
        self.radius = math.sqrt(self.mass / math.pi)
        super().__init__(window, 0, self.radius * 1.25, self.launch, self.launch)

        self.maxShield = self.window.save.shieldLevel
        self.shield = 0
        self.airResist = 1.0 - self.window.save.airResistLevel * .1
        self.antiGrav = 1.0 - self.window.save.antiGravLevel * .1
        self.friction = 1.0 - self.window.save.frictionLevel * .1
        self.growthRate = 1 + .1 * self.window.save.growthRateLevel
        self.propulsion = 1.0 + .1 * self.window.save.propulsionLevel
        if self.window.save.maxMassLevel != 5:
            self.maxMass = self.startMass + 500 * ((self.window.save.maxMassLevel + .5) * 4) ** 2
        else:
            self.maxMass = 10000000000000
        self.maxFuel = 100 * (self.window.save.maxFuelLevel + 1)
        self.fuel = self.maxFuel

        self.stars = 0
        self.outlineMode = window.save.outlineMode
        self.BLOB_MAGNET = 50000
        self.VIRUS_MAGNET = 1000
        self.FUEL_COST = 25
        self.rocket = False
        self.requestedMass = self.mass
        self.massCollected = 0
        self.color = "red"
        self.angle = 0
        self.screenX = window.width / 5
        self.screenY = window.height / 2
        self.GRAVITY = 350
        self.outlineList = []
        self.lostRadius = 0
        self.oldLostRadius = 0
        self.touchingGround = False
        for a in range (361):
            self.outlineList.append(Point(self.radius * 1.25, a, self.window, self.outlineMode))

    def run(self):
        self.move()

        #gravity
        if self.y > self.radius:
            self.accelerate(0, -self.GRAVITY * self.antiGrav)

        #acceleration due to the rocket
        if self.rocket and self.fuel > 0:
            self.fuel -= self.FUEL_COST * self.window.frameRate.TICK_SPEED
            mouseX = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
            mouseY = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
            xC = mouseX - self.screenX * self.window.gameEngine.scaleEngine.getScale()
            yC = self.screenY * self.window.gameEngine.scaleEngine.getScale() - mouseY
            if not self.window.save.invertedControls:
                xC *= -1
                yC *= -1
            h = math.sqrt(xC ** 2 + yC ** 2)
            if h == 0:
                h = .00001
            self.fireRocket(xC, yC, h)

        #the angle for black holes-will likely change
        if self.angle < 360 + 360 * self.window.frameRate.TICK_SPEED:
            self.angle += 360 * self.window.frameRate.TICK_SPEED
        else:
            self.angle = 0

        self.screenX = self.window.width / 5 / self.window.gameEngine.scaleEngine.getScale()
        self.screenY = self.window.height / 2 / self.window.gameEngine.scaleEngine.getScale()

        #updating the outline points
        if self.outlineMode != "off":
            self.oldLostRadius = self.lostRadius
            self.lostRadius = 0
            for o in self.outlineList:
                o.run(self.oldLostRadius)
                self.lostRadius += o.lostRadius

        #air resistance
        xRes = math.pi * self.radius ** 2 * self.getXSpeed() ** 2 * .0000000002 * self.airResist
        yRes = math.pi * self.radius ** 2 * self.getYSpeed() ** 2 * .0000000002 * self.airResist
        self.accelerate(math.copysign(xRes, -self.getXSpeed()), math.copysign(yRes, -self.getYSpeed()))

        #check for collisions with the ground and blobs
        self.collisionCheck()

        #updating values
        self.updateMass()

        #magnet
        if self.window.save.starMagnetLevel == 5:
            for b in self.window.gameEngine.blobList:
                distance = self.window.distance(self.x, self.y, b.x, b.y)
                if distance < self.radius * 20:
                    xC = self.x - b.x
                    yC = self.y - b.y
                    angle = math.atan2(yC, xC)
                    accStrength = self.BLOB_MAGNET / distance ** 2 * self.radius
                    b.accelerate(accStrength * math.cos(angle), accStrength * math.sin(angle))
                    moveStrength = self.BLOB_MAGNET / distance ** 2 * 1000000 * self.window.frameRate.TICK_SPEED
                    b.changePosition(moveStrength * math.cos(angle), moveStrength * math.sin(angle))

        for v in self.window.gameEngine.blackHoleList:
            distance = self.window.distance(self.x, self.y, v.x, v.y)
            if distance < self.radius * 40:
                xC = self.x - v.x
                yC = self.y - v.y
                angle = math.atan2(yC, xC)
                accStrength = self.VIRUS_MAGNET / distance ** 2 * 20000 * (1 - .175 * self.shield * self.window.save.starShieldLevel / 5)
                self.accelerate(accStrength * -math.cos(angle), accStrength * -math.sin(angle))
                moveStrength = self.VIRUS_MAGNET / distance ** 2 * 1000000 * self.window.frameRate.TICK_SPEED * (1 - .175 * self.shield * self.window.save.starShieldLevel / 5)
                self.changePosition(moveStrength * -math.cos(angle), moveStrength * -math.sin(angle))

    def updateMass(self):
        if self.requestedMass - self.mass > 0:
            if self.mass + (self.requestedMass - self.mass) * 2 * self.window.frameRate.TICK_SPEED < self.requestedMass:
                self.mass += (self.requestedMass - self.mass) * 2 * self.window.frameRate.TICK_SPEED
        if self.requestedMass - self.mass < 0:
            if self.mass + (self.requestedMass - self.mass) / 5 > self.requestedMass:
                self.mass += (self.requestedMass - self.mass) / 5
        self.radius = math.sqrt(self.mass / math.pi)

    def addMass(self, mass):
        if mass > 0:
            self.requestedMass += mass * (1 - math.e ** ((self.maxMass - self.requestedMass) / -10000))
            self.massCollected += mass * (1 - math.e ** ((self.maxMass - self.requestedMass) / -10000))
        else:
            print("cannot add negative mass")

    def subtractMass(self, mass):
        if mass < 0:
            if self.requestedMass + mass > 7500:
                self.requestedMass += mass
                self.massCollected += mass
        else:
            print("cannot subtract positive mass")

    def setMass(self, mass):
        self.requestedMass = mass

    def collisionCheck(self):
        if self.y <= self.radius and self.getYSpeed() < 0:
            self.y = self.radius
            self.setSpeed(self.getXSpeed() * (1.0 - .3 * self.friction), abs(self.getYSpeed() * (1.0 - .3 * self.friction)))
        if self.y + self.getYSpeed() * .25 < self.radius * 1.25 and not self.touchingGround and platform.system == "Windows":
            self.touchingGround = True
            self.window.soundEngine.playBounceSound()
        if self.y > self.radius * 1.25 and self.getYSpeed() > 0:
            self.touchingGround = False
        minSpeed = self.GRAVITY * 1.1 * self.window.frameRate.TICK_SPEED
        if self.getXSpeed() < minSpeed and self.getXSpeed() > -minSpeed and self.getYSpeed() < minSpeed and self.getYSpeed() > -minSpeed and self.y < self.radius + minSpeed:
            self.window.rMenu = "summaryScreen"
            self.window.gameEngine.endGame()

    def fireRocket(self, xC, yC, h):
        #self.fuel -= self.FUEL_COST * self.window.frameRate.TICK_SPEED
        if platform.system == "Windows":
            self.window.soundEngine.playEjectionSound()
        xAcc = self.getRocketSpeed() * -xC / h
        yAcc = self.getRocketSpeed() * -yC / h
        self.accelerate(xAcc, yAcc)
        xChange = xAcc * 5
        yChange = yAcc * 5
        self.changePosition(xChange, yChange)

    def getRocketSpeed(self):
        return 50 * self.propulsion

