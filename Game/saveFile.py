__author__ = 'psheppard16'
class SaveFile:
    def __init__(self):
        self.mass = 0
        self.stars = 0

        self.shieldLevel = 0
        self.airResistLevel = 0
        self.antiGravLevel = 0
        self.frictionLevel = 0
        self.launchLevel = 0
        self.maxMassLevel = 0
        self.growthRateLevel = 0
        self.propulsionLevel = 0
        self.maxFuelLevel = 0

        self.starShieldLevel = 0
        self.starSpeedGateLevel = 0
        self.starFuelCanLevel = 0
        self.starMagnetLevel = 0
        self.starPredictionLevel = 0
        self.starBlackHoleLevel = 0

        self.color = "red"
        self.resolution = "1280x720"
        self.smoothFrames = False
        self.debugMode = False
        self.debugScale = .1 #<1
        self.showBackground = False
        self.outlineMode = "simple"
        self.smoothScale = True

        self.starSpawn = 1.0 #>1
        self.speedGateSpawn = 1.0 #>1
        self.shieldSpawn = 1.0 #>1
        self.launchPadSpawn = 1.0 #>1
        self.fuelCanSpawn = 1.0 #>1
        self.predictionQuality = .1 #float above 0
        self.invertedControls = False