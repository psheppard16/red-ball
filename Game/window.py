__author__ = 'psheppard16'
import pickle
from Display.imageSaving import *
from Screens.mainMenu import *
from Screens.options import *
from Display.drawingEngine import *
from Screens.saveScreen import *
from Game.instructions import *
from Screens.charScreen import *
from Game.saveFile import SaveFile
from Screens.summaryScreen import *
from Game.frameRate import *
from Game.gameEngine import *
from Game.soundEngine import *
from Screens.shopEngine import ShopEngine
from Screens.starShopEngine import StarShopEngine
class Window:
    def __init__(self):
        self.width = 1280
        self.height = 720
        self.saveNumber = 0
        self.saveSelected = False
        self.save = SaveFile()
        self.cMenu = "null"
        self.rMenu = "mainMenu"
        self.root = tk.Tk()
        self.root.title("Red Ball")
        self.root.bind_all('<KeyPress>', self.kp)
        self.root.bind_all('<KeyRelease>', self.kr)
        self.root.geometry("1280x720")
        self.root.resizable(False, False)
        self.frameRate = FrameRate(self)
        self.mainMenu = MainMenu(self)
        self.options = Options(self)
        self.saveScreen = SaveScreen(self)
        self.instructions = Instructions(self)
        self.charScreen = CharScreen(self)
        self.gameEngine = GameEngine(self)
        self.summaryScreen = SummaryScreen(self)
        self.shopEngine = ShopEngine(self)
        self.starShopEngine = StarShopEngine(self)
        if platform.system() == "Windows":
            self.soundEngine = SoundEngine(self)
            self.usePygame = True
        else:
            self.usePygame = False
        self.drawingEngine = DrawingEngine(self)
        self.savedBH = None
        self.savedBHW = None
        self.savedDE = None
        self.savedEM = None
        self.savedG = None
        self.savedHE = None
        self.savedNE = None
        self.savedSM = None
        self.savedSG = None
        self.savedSGW = None
        self.savedGC = None
        self.savedSH = None
        #self.saveCharacter(1) # resets the saves
        #self.saveCharacter(2)
        #self.saveCharacter(3)
        self.root.after(1, self.loop)
        self.root.mainloop()

    def loop(self):
        self.savedBH = ImageSaving(Image.open("Images/blackHole.png"), "BlackHole", .01, 1, .001, 3, ".001")
        self.savedBHW = ImageSaving(Image.open("Images/blackHoleWarning.png"), "BlackHoleWarning", .01, 1, .001, 3, ".001")
        self.savedDE = ImageSaving(Image.open("Images/determinedEyes.png"), "DeterminedEyes", .01, 1, .001, 3, ".001")
        self.savedEM = ImageSaving(Image.open("Images/eatingMouth.png"), "EatingMouth", .01, 1, .001, 3, ".001")
        self.savedG = ImageSaving(Image.open("Backgrounds/mainMenu.png"), "Ground", .01, 1, .001, 3, ".001")
        self.savedHE = ImageSaving(Image.open("Images/hurtEyes.png"), "HurtEyes", .01, 1, .001, 3, ".001")
        self.savedNE = ImageSaving(Image.open("Images/normalEyes.png"), "NormalEyes", .01, 1, .001, 3, ".001")
        self.savedSM = ImageSaving(Image.open("Images/smileMouth.png"), "SmileMouth", .01, 1, .001, 3, ".001")
        self.savedSG = ImageSaving(Image.open("Images/speedGate.png"), "SpeedGate", .01, 1, .001, 3, ".001")
        self.savedSGW = ImageSaving(Image.open("Images/speedGateWarning.png"), "SpeedGateWarning", .01, 1, .001, 3, ".001")
        self.savedGC = ImageSaving(Image.open("Images/gasCan.png"), "GasCan", .01, 1, .001, 3, ".001")
        self.savedSH = ImageSaving(Image.open("Images/shield.png"), "Shield", .01, 1, .001, 3, ".001")
        while True:
            self.root.focus_force()
            if self.frameRate.getTime() > self.frameRate.nextTick:
                self.frameRate.tickStartTime = self.frameRate.getTime()
                if self.usePygame:
                    self.soundEngine.runSong()
                if str(self.width) + 'x' + str(self.height) != self.save.resolution:
                    self.root.geometry(self.save.resolution)
                    self.width = self.root.winfo_width()
                    self.height = self.root.winfo_height()
                    self.updateFrameSizes()
                if self.cMenu != self.rMenu:
                    self.clearWindow()
                    if self.rMenu == "options":
                        self.options.setUp()
                    if self.rMenu == "instructions":
                        self.instructions.setUp()
                    if self.rMenu == "mainMenu":
                        self.mainMenu.setUp()
                    if self.rMenu == "gameEngine":
                        self.gameEngine = GameEngine(self)
                        self.drawingEngine.f.pack(side=LEFT)
                        self.lastFrameCalc = int(self.frameRate.getTime())
                    if self.rMenu == "saveScreen":
                        self.saveScreen.setUp()
                    if self.rMenu == "charScreen":
                        self.charScreen.setUp()
                    if self.rMenu == "shop":
                        self.gameEngine = GameEngine(self)
                        self.shopEngine.setUp()
                    if self.rMenu == "starShop":
                        self.gameEngine = GameEngine(self)
                        self.starShopEngine.setUp()
                    if self.rMenu == "summaryScreen":
                        self.summaryScreen.setUp()
                    self.cMenu = self.rMenu
                    self.frameRate.startTimer("saveFile")
                    if self.saveSelected:
                        self.saveCharacter(self.saveNumber)
                    self.frameRate.timeChange()
                if self.cMenu == "gameEngine":
                    self.gameEngine.runGame()
                    self.frameRate.renderedFrame = False
                    if self.frameRate.getTime() <= self.frameRate.nextTick + math.sqrt(self.frameRate.TICK_SPEED): #only renders if not running behind
                        self.frameRate.renderTime = -self.frameRate.getTime() #when a frame is not rendered the variable framerate calculator still has to take into account the time it would have taken
                        self.frameRate.startTimer("display")
                        self.drawingEngine.render(self.gameEngine.scaleEngine.getScale(), self.gameEngine.scaleEngine.scale, self.gameEngine.blobList, self.gameEngine.blackHoleList, self.gameEngine.predictionList, self.gameEngine.speedGateList, self.gameEngine.starList, self.gameEngine.fuelCanList, self.gameEngine.shieldList, self.gameEngine.spawnGrid, self.gameEngine.scaleEngine.requestedScale)
                        self.frameRate.timeChange()
                    self.frameRate.update()
                else:
                    self.root.update()
                if self.cMenu == "shop":
                    self.shopEngine.run()
                if self.cMenu == "starShop":
                    self.starShopEngine.run()

    def kp(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kp(event)

    def kr(self, event):
        if self.cMenu == "gameEngine":
            self.gameEngine.kr(event)

    def screenY(self, x):
        return self.height - x

    def distance(self, x1, y1, x2, y2):
        xD = x1 - x2
        yD = y1 - y2
        return math.sqrt(xD ** 2 + yD ** 2)

    def clearWindow(self):
        self.options.hide()
        self.instructions.hide()
        self.drawingEngine.hide()
        self.mainMenu.hide()
        self.saveScreen.hide()
        self.charScreen.hide()
        self.summaryScreen.hide()
        self.shopEngine.hide()
        self.starShopEngine.hide()

    def updateFrameSizes(self):
        self.options.update()
        self.instructions.update()
        self.mainMenu.update()
        self.drawingEngine.update()
        self.saveScreen.update()
        self.charScreen.update()
        self.summaryScreen.update()
        self.shopEngine.update()
        self.starShopEngine.update()

    def loadChar(self, number):
        try:
            if number == 1:
                with open('SaveFiles/saveFile1', 'rb') as input:
                    self.save = pickle.load(input)
            elif number == 2:
                with open('SaveFiles/saveFile2', 'rb') as input:
                    self.save = pickle.load(input)
            elif number == 3:
                with open('SaveFiles/saveFile3', 'rb') as input:
                    self.save = pickle.load(input)
        except EOFError:
            return {}

    def saveCharacter(self, number):
        if number == 1:
            with open('SaveFiles/saveFile1', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)
        elif number == 2:
            with open('SaveFiles/saveFile2', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)
        elif number == 3:
            with open('SaveFiles/saveFile3', 'wb') as output:
                pickle.dump(self.save, output, pickle.HIGHEST_PROTOCOL)

