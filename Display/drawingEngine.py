import math
from PIL import Image, ImageTk
import PIL
import tkinter as tk
try:
    import pygame
except:
    from tkinter import Canvas
import random
import os
import platform
from decimal import *
class DrawingEngine:
    def __init__(self, window):
        self.window = window
        self.f = tk.Frame(self.window.root, width = self.window.width, height = self.window.height)
        self.f.pack_propagate(0)
        self.blinkTime = 0
        os.environ['SDL_WINDOWID'] = str(self.f.winfo_id())
        if platform.system() == "Windows":
            os.environ['SDL_VIDEODRIVER'] = 'windib'
            self.usePygame = True
            self.display = pygame.display.set_mode((self.window.width, self.window.height))
            self.display.fill((255,255,255))
            pygame.display.init()
        else:
            self.usePygame = False
            self.canvas = Canvas(self.window.root, bg="white", width=self.window.width, height = self.window.height)
            self.canvas.pack(in_=self.f)
        self.rawEfficiencyBar = self.convertToDisplayFormat(Image.open("Images/efficiencyBar.png"))
        self.rawIndicator = self.convertToDisplayFormat(Image.open("Images/indicator.png"))
        self.rawMassBar = self.convertToDisplayFormat(Image.open("Images/massBar.png"))
        self.rocketFlameImage = self.convertToDisplayFormat(Image.open("Images/rocketFlame.png"))
        self.shieldCounter = self.convertToDisplayFormat(self.scale(Image.open("Images/shield.png"), .15))
        self.bgImageList = [None for x in range(1000)] #these list lengths must match the number of preloaded images there are
        self.bhImageList = [None for x in range(1000)]
        self.sgImageList = [None for x in range(1000)]
        self.bhwImageList = [None for x in range(250)]
        self.sgwImageList = [None for x in range(250)]
        self.smImageList = [None for x in range(1000)]
        self.emImageList = [None for x in range(1000)]
        self.deImageList = [None for x in range(1000)]
        self.heImageList = [None for x in range(1000)]
        self.neImageList = [None for x in range(1000)]
        self.fcImageList = [None for x in range(1000)]
        self.shImageList = [None for x in range(1000)]
        self.tkImageList = [] #images must maintain a reference in order to appear on the canvas
        self.face = "normal"
        self.faceTimer = 50

    def render(self, scale, debugScale, blobList, blackHoleList, predictionList, speedGateList, starList, fuelCanList, sheildList, spawnGrid, requestedScale):
        p = self.window.gameEngine.character
        self.window.frameRate.startTimer("clear")
        if self.usePygame:
            self.display.fill((121, 202, 249))
        else:
            self.canvas.delete("all")
            self.canvas.create_rectangle(0, 0, self.window.width, self.window.height, fill = "#%02x%02x%02x" % (121, 202, 249))
            self.tkImageList.clear()
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showBackground")
        self.showBackground(scale)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("debugg")
        if self.window.save.debugMode:
            self.showDebugElements(p, scale, debugScale, spawnGrid)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showStar")
        self.showStars(starList)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showFuelCan")
        self.showFuelCans(fuelCanList)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showSheild")
        self.showSheilds(sheildList)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showVirus")
        self.showBlackHole(blackHoleList, scale, p)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showPredictions")
        if self.window.save.starPredictionLevel == 5:
           self.showPredictions(p, scale, predictionList)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showBlobs")
        self.showBlobs(blobList, scale)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showPlayer")
        self.showPlayer(p, scale)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showFace")
        self.showFace(p, scale, blobList, requestedScale)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showSpeedGate")
        self.showSpeedGates(p, scale, speedGateList)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("showGUI")
        self.showGUI(p)
        self.window.frameRate.timeChange()

        self.window.frameRate.startTimer("update")
        if self.usePygame:
            pygame.display.update()
            self.window.root.update() #must update while in canvas in pygame but not in tkinter
        else:
            self.canvas.update()
        self.window.frameRate.timeChange()

    def showRectangle(self, x1, y1, x2, y2, color):
        if self.usePygame:
            pygame.draw.rect(self.display, color, ((x1, y1), (x2, y2)))
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=tk_rgb, width=0)

    def showLine(self, position1, position2, color, width):
        if self.usePygame:
            pygame.draw.line(self.display, color, position1, position2, width)
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_line(position1[0], position1[1], position2[0], position2[1],
                                    fill=tk_rgb, width=width)

    def showImage(self, image, position, anchorCenter = False):
        if self.usePygame:
            if anchorCenter:
                imageW = image.get_width()
                imageH = image.get_height()
            else:
                imageW = 0
                imageH = 0
            self.display.blit(image, (int(position[0] - imageW / 2), int(position[1] - imageH / 2)))
        else:
            image = ImageTk.PhotoImage(image)
            self.tkImageList.append(image)
            if not anchorCenter:
                imageW = image.width()
                imageH = image.height()
            else:
                imageW = 0
                imageH = 0
            self.canvas.create_image((position[0] + imageW / 2, position[1] + imageH / 2), image=image)

    def showPolygon(self, pointList, color, position=(0, 0)):
        points = []
        for index in range(len(pointList)):
            points.append((pointList[index][0] + position[0], pointList[index][1] + position[1]))
        if self.usePygame:
            pygame.draw.polygon(self.display, color, points)
            pygame.draw.polygon(self.display, (0, 0, 0), points, 2)
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_polygon(points, outline='black', fill=tk_rgb, width=2)

    def showCircle(self, radius, position, color):
        if self.usePygame:
            pygame.draw.circle(self.display, color, (int(position[0]), int(position[1])), int(radius))
            pygame.draw.circle(self.display, (0, 0, 0), (int(position[0]), int(position[1])), int(radius), 2)
        else:
            tk_rgb = "#%02x%02x%02x" % color
            self.canvas.create_oval(position[0] - radius, position[1] - radius,
                                    position[0] + radius, position[1] + radius, fill=tk_rgb)

    def showBackground(self, scale):
        p = self.window.gameEngine.character
        x1 = 0
        y1 = 0
        x2 = self.window.width
        y2 = self.window.height
        self.showRectangle(x1, self.getScreenY(y1), x2, y2, (127, 172, 113))
        if self.window.save.showBackground:
            imageWidth = 1920
            imageHeight = 1080
            groundLocation = imageHeight * .77
            #get images
            if p.y <  (imageHeight + self.window.height / 2) / scale:
                nearestScale = self.getNearestScale(scale, self.window.savedG.lowestScale, self.window.savedG.highestScale, self.window.savedG.roundString)
                path = "ModifiedImages/Ground/" + str(nearestScale) + ".png"
                backGroundImage = self.getListImage(path, nearestScale, self.bgImageList)

                #position and display images
                referencePoint = p.x // imageWidth
                numberOfBackgrounds = int(self.window.width // (imageWidth * scale / 2) + 1)
                for location in range(-numberOfBackgrounds, numberOfBackgrounds):
                    self.showImage(backGroundImage, (self.getScreenX(location * imageWidth + referencePoint * imageWidth),  self.getScreenY(groundLocation)))

    def getListImage(self, path, nearestScale, imageList):
        if self.usePygame:
            index = int(nearestScale * len(imageList)) - 1
            if imageList[index] == None:
                image = self.convertToDisplayFormat(Image.open(path))
                imageList[index] = image
                for i in range(len(imageList)): #remove images that havent been used lately
                    if i < index - 50 or i > index + 50:
                        imageList[i] = None
            else:
                image = imageList[index]
        else:
            image = self.convertToDisplayFormat(Image.open(path))
        return image


    def getNearestScale(self, scale, low, high, roundString):
        #find the image that is nearest to the scale
        if scale >= low:
            if scale <= high:
                nearestScale = Decimal(scale).quantize(Decimal(roundString), rounding=ROUND_HALF_UP)
            else:
                nearestScale = Decimal(high).quantize(Decimal(roundString), rounding=ROUND_HALF_UP)
                print("no image preloaded")
        else:
            nearestScale = Decimal(low).quantize(Decimal(roundString), rounding=ROUND_HALF_UP)
            print("no image preloaded")
        return nearestScale

    def showSpeedGates(self, p, scale, speedGateList):
        #get images
        if len(speedGateList) > 0:
            nearestScale = self.getNearestScale(scale, self.window.savedSG.lowestScale, self.window.savedSG.highestScale, self.window.savedSG.roundString)
            path = "ModifiedImages/SpeedGate/" + str(nearestScale) + ".png"
            speedGateImage = self.getListImage(path, nearestScale, self.sgImageList)

            for s in speedGateList:
                rotatedSpeedGateImage = self.rotate(speedGateImage, s.angle)
                x = int((self.getScreenX(s.x)))
                y = int((self.getScreenY(s.y)))
                self.showImage(rotatedSpeedGateImage, (x, y), True)
                #x = int((self.getScreenX(s.cap1X)))
                #y = int((self.getScreenY(s.cap1Y)))
                #self.showCircle(s.capRadius * scale, (x, y), (0, 0, 255))
                #x = int((self.getScreenX(s.cap2X)))
                #y = int((self.getScreenY(s.cap2Y)))
                #self.showCircle(s.capRadius * scale, (x, y), (0, 0, 255))
                #x = int((self.getScreenX(s.sweepX)))
                #y = int((self.getScreenY(s.sweepY)))
                #self.showCircle(s.sweepRadius * scale, (x, y), (0, 0, 0))

    def showGUI(self, p):
        #self.canvas.create_text(250, self.window.height - 75, fill="darkblue", font="Times 50 bold",
        #                text="Mass")
        self.showImage(self.rawMassBar, (10, self.window.height - 60))
        xLoc = 495 * (p.mass - p.startMass) / (p.maxMass - p.startMass)
        self.showImage(self.rawIndicator, (xLoc, self.window.height - 85))

        #self.canvas.create_text(self.window.width - 250, self.window.height - 75, fill="darkblue", font="Times 50 bold",
        #                text="Fuel")
        self.showImage(self.rawEfficiencyBar, (self.window.width - 10 - 500, self.window.height - 60))
        xLoc = self.window.width - 520 + 495 * (p.maxFuel - p.fuel) / p.maxFuel
        self.showImage(self.rawIndicator, (xLoc, self.window.height - 85))

        if self.usePygame:
            width = self.shieldCounter.get_width()
            height = self.shieldCounter.get_height()
        else:

            width = self.shieldCounter.size[0]
            height = self.shieldCounter.size[1]
        step = width + 15
        for location in range(15, step * p.shield + 15, step):
            self.showImage(self.shieldCounter, (location, self.window.height - 60 - height - 15))

    def showFace(self, p, scale, blobList, requestedScale):
        mouseX = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
        mouseY = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
        xC = mouseX - p.screenX * scale
        yC = mouseY - p.screenY * scale
        h = math.sqrt(xC ** 2 + yC ** 2)
        if h == 0:
            h = .00001
        closeToBlob = False
        for b in blobList:
            if self.window.distance(p.x + xC / h * p.radius * 2, p.y + yC / h * p.radius * 2, b.x, b.y) < p.radius * 4:
                closeToBlob = True
        if random.randint(0, 200) < 1 and self.blinkTime < -30:
            self.blinkTime = 15
            self.face = "blink"
            self.faceTimer = 0
        self.blinkTime -= 1
        self.faceTimer -= 1
        faceScale = requestedScale ** .005 / 2
        mouthAngle = math.degrees(math.atan2(xC, yC)) - 90
        eyeAngle = math.degrees(math.atan2(xC, yC))
        if self.faceTimer < 0 or self.blinkTime == 0:
            oldFace = self.face
            if p.y < p.radius * 1.2 or self.blinkTime > 0:
                self.face = "onGround"
            elif closeToBlob:
                self.face = "closeToBlob"
            elif p.rocket and p.fuel >=0:
                self.face = "rocket"
            else:
                self.face = "normal"
            if oldFace != self.face:
                self.faceTimer = 100
        if self.face == "onGround":
            eyeScale = self.getNearestScale(.5 * faceScale, self.window.savedHE.lowestScale, self.window.savedHE.highestScale, self.window.savedHE.roundString)
            path = "ModifiedImages/HurtEyes/" + str(eyeScale) + ".png"
            eyesImage = self.rotate(self.getListImage(path, eyeScale, self.heImageList), eyeAngle)

            mouthScale = self.getNearestScale(.33 * faceScale, self.window.savedSM.lowestScale, self.window.savedSM.highestScale, self.window.savedSM.roundString)
            path = "ModifiedImages/SmileMouth/" + str(mouthScale) + ".png"
            mouthImage = self.rotate(self.getListImage(path, mouthScale, self.smImageList), mouthAngle + 180)
        elif  self.face == "closeToBlob":
            eyeScale = self.getNearestScale(.5 * faceScale, self.window.savedDE.lowestScale, self.window.savedDE.highestScale, self.window.savedDE.roundString)
            path = "ModifiedImages/DeterminedEyes/" + str(eyeScale) + ".png"
            eyesImage = self.rotate(self.getListImage(path, eyeScale, self.deImageList), eyeAngle)

            mouthScale = self.getNearestScale(.33 * faceScale, self.window.savedEM.lowestScale, self.window.savedEM.highestScale, self.window.savedEM.roundString)
            path = "ModifiedImages/EatingMouth/" + str(mouthScale) + ".png"
            mouthImage = self.rotate(self.getListImage(path, mouthScale, self.emImageList), mouthAngle)
        elif  self.face == "rocket":
            eyeScale = self.getNearestScale(.5 * faceScale, self.window.savedNE.lowestScale, self.window.savedNE.highestScale, self.window.savedNE.roundString)
            path = "ModifiedImages/NormalEyes/" + str(eyeScale) + ".png"
            eyesImage = self.rotate(self.getListImage(path, eyeScale, self.neImageList), eyeAngle)

            mouthScale = self.getNearestScale(.33 * faceScale, self.window.savedEM.lowestScale, self.window.savedEM.highestScale, self.window.savedEM.roundString)
            path = "ModifiedImages/EatingMouth/" + str(mouthScale) + ".png"
            mouthImage = self.rotate(self.getListImage(path, mouthScale, self.emImageList), mouthAngle)
        else:
            eyeScale = self.getNearestScale(.5 * faceScale, self.window.savedNE.lowestScale, self.window.savedNE.highestScale, self.window.savedNE.roundString)
            path = "ModifiedImages/NormalEyes/" + str(eyeScale) + ".png"
            eyesImage = self.rotate(self.getListImage(path, eyeScale, self.neImageList), eyeAngle)

            mouthScale = self.getNearestScale(.33 * faceScale, self.window.savedSM.lowestScale, self.window.savedSM.highestScale, self.window.savedSM.roundString)
            path = "ModifiedImages/SmileMouth/" + str(mouthScale) + ".png"
            mouthImage = self.rotate(self.getListImage(path, mouthScale, self.smImageList), mouthAngle)
        angleSeperation = math.pi / 5

        x = int((p.screenX + p.radius * math.sin(math.atan2(xC, yC) + angleSeperation) * .5) * scale)
        y = int((p.screenY + p.radius * math.cos(math.atan2(xC, yC) + angleSeperation) * .5) * scale)
        self.showImage(eyesImage, (x, y), True)

        x = int((p.screenX + p.radius * math.sin(math.atan2(xC, yC) - angleSeperation) * .5) * scale)
        y = int((p.screenY + p.radius * math.cos(math.atan2(xC, yC) - angleSeperation) * .5) * scale)
        self.showImage(mouthImage, (x, y), True)

    def showPredictions(self, p, scale, predictionList):
        red = True
        for z in range(len(predictionList) - 1):
            x1 = (self.getScreenX(predictionList[z].x))
            y1 = (self.getScreenY(predictionList[z].y))
            x2 = (self.getScreenX(predictionList[z + 1].x))
            y2 = (self.getScreenY(predictionList[z + 1].y))
            if red:
                self.showLine((x1, y1), (x2, y2), (255, 0, 0), 4)
                red = False
            else:
                self.showLine((x1, y1), (x2, y2), (0, 0, 0), 4)
                red = True

    def showGround(self, p, scale):
        x1 = 0
        y1 = int((p.y + p.screenY) * scale)
        x2 = self.window.width
        y2 = int((p.y + p.screenY) * scale)
        self.showLine((x1, y1), (x2, y2), (0, 255,0), 2)


    def showPlayer(self, p, scale):
        if p.rocket and p.fuel >= 0:
            mouseX = self.window.root.winfo_pointerx() - self.window.root.winfo_rootx()
            mouseY = self.window.root.winfo_pointery() - self.window.root.winfo_rooty()
            xC = mouseX - p.screenX * scale
            yC = mouseY - p.screenY * scale
            if not self.window.save.invertedControls:
                xC *= -1
                yC *= -1
            h = math.sqrt(xC ** 2 + yC ** 2)
            if h == 0:
                h = .00001
            flameAngle = math.degrees(math.atan2(xC, yC)) + 45
            rotatedFlame = self.rotate(self.rocketFlameImage, flameAngle)
            x = int((p.screenX + p.radius * math.sin(math.atan2(-xC, -yC) + math.pi)) * scale)
            y = int((p.screenY + p.radius * math.cos(math.atan2(-xC, -yC) + math.pi)) * scale)
            self.showImage(rotatedFlame, (x, y), True)

        if self.window.save.outlineMode == "off":
            self.showCircle(p.radius * scale, (p.screenX * scale, p.screenY * scale), (255, 0, 0))
        else:
            playerOutline = []
            for t in p.outlineList:
                playerOutline.append(((p.screenX + t.x) * scale, (p.screenY - t.y) * scale))
            self.showPolygon(playerOutline, (255, 0, 0))

    def showBlobs(self, blobList, scale):
        for b in blobList:
            x = int((self.getScreenX(b.x)))
            y = int((self.getScreenY(b.y)))
            try:
                self.showCircle(b.radius * scale, (x, y), b.color)
            except:
                pass

    def showStars(self, starList):
        for s in starList:
            x = int((self.getScreenX(s.x)))
            y = int((self.getScreenY(s.y)))
            self.showPolygon(s.pointList, (255, 255, 255), (x, y))

    def showFuelCans(self, fuelCanList):
        fuelCanImage = None
        if len(fuelCanList) > 0:
            nearestScale = self.getNearestScale(self.window.gameEngine.scaleEngine.getScale(), self.window.savedBH.lowestScale, self.window.savedBH.highestScale, self.window.savedBH.roundString)
            path = "ModifiedImages/GasCan/" + str(nearestScale) + ".png"
            fuelCanImage = self.getListImage(path, nearestScale, self.fcImageList)
        for f in fuelCanList:
            x = int((self.getScreenX(f.x)))
            y = int((self.getScreenY(f.y)))
            try:
                self.showImage(fuelCanImage, (x, y), True)
            except:
                pass

    def showSheilds(self, sheildList):
        sheildImage = None
        if len(sheildList) > 0:
            nearestScale = self.getNearestScale(self.window.gameEngine.scaleEngine.getScale() / 2, self.window.savedSH.lowestScale, self.window.savedSH.highestScale, self.window.savedSH.roundString)
            path = "ModifiedImages/Shield/" + str(nearestScale) + ".png"
            sheildImage = self.getListImage(path, nearestScale, self.shImageList)
        for sh in sheildList:
            x = int((self.getScreenX(sh.x)))
            y = int((self.getScreenY(sh.y)))
            try:
                self.showImage(sheildImage, (x, y), True)
            except:
                pass

    def showBlackHole(self, blackHoleList, scale, p):
        if len(blackHoleList) > 0:
            nearestScale = self.getNearestScale(scale, self.window.savedBH.lowestScale, self.window.savedBH.highestScale, self.window.savedBH.roundString)
            path = "ModifiedImages/BlackHole/" + str(nearestScale) + ".png"
            blackHoleImage = self.rotate(self.getListImage(path, nearestScale, self.bhImageList), p.angle)

            warningImage = None
            if self.window.save.starBlackHoleLevel == 5:
                warningScale = self.window.gameEngine.scaleEngine.requestedScale ** .005 / 2
                nearestScale = self.getNearestScale(warningScale, self.window.savedBHW.lowestScale, self.window.savedBHW.highestScale, self.window.savedBHW.roundString)
                path = "ModifiedImages/BlackHoleWarning/" + str(nearestScale) + ".png"
                warningImage = self.getListImage(path, nearestScale, self.bhwImageList)
            for b in blackHoleList:
                x = int((self.getScreenX(b.x)))
                y = int((self.getScreenY(b.y)))
                self.showImage(blackHoleImage, (x, y), True)

                xC = b.x - p.x
                yC = b.y - p.y
                h = math.sqrt(xC ** 2 + yC ** 2)
                if h == 0:
                    h = .00001
                newXC = p.radius * 1.75 * xC / h
                newYC = p.radius * 1.75 * yC / h
                angleToBlackHole = math.degrees(math.atan2(yC, xC)) + 90
                if self.window.save.starBlackHoleLevel == 5:
                    if angleToBlackHole - 90 > p.getAngle() - 30 and angleToBlackHole - 90 < p.getAngle() + 30:
                        rotatedWarningImage = self.rotate(warningImage, angleToBlackHole)
                        x = int((p.screenX + newXC + yC / h * 10) * scale)
                        y = int((p.screenY - newYC - xC / h * 10) * scale)
                        self.showImage(rotatedWarningImage, (x, y), True)

    def showDebugElements(self, p, scale, debugScale, spawnGrid):
        radius = self.window.width * 1.5 * scale / debugScale
        xLoc = int((p.screenX  + self.window.width * 5 / 4 / debugScale) * scale)
        yLoc = int((p.screenY) * scale)
        self.showCircle(radius, (xLoc, yLoc), (0, 255, 0))

        spawnSweep = self.window.gameEngine.spawnSweep
        xLoc2 = self.getScreenX(spawnSweep.x)
        yLoc2 = self.getScreenY(spawnSweep.y)
        self.showCircle(spawnSweep.radius * scale, (xLoc2, yLoc2), (0, 255, 255))

        screenX1 = int(p.screenX * scale - self.window.width / 5 * scale / debugScale)
        screenY1 = int(p.screenY * scale - self.window.height / 2 * scale / debugScale)
        xSize = int(self.window.width * scale / debugScale)
        ySize = int(self.window.height * scale / debugScale)
        self.showRectangle(screenX1, screenY1, screenX1 + xSize, screenY1 + ySize, (0, 0, 255))

        p = self.window.gameEngine.character
        lowestX = math.floor(p.x / 1000) - int(1 / math.sqrt(debugScale) * 5)
        if lowestX < 0:
            lowestX = 0
        largestX = lowestX + int(1 / math.sqrt(debugScale) * 5) * 2
        lowestY = math.floor(p.y / 1000) - int(1 / math.sqrt(debugScale) * 5)
        if lowestY < 0:
            lowestY = 0
        largestY = lowestY + int(1 / math.sqrt(debugScale) * 5) * 2
        for i in range(lowestX, largestX):
            for j in range(lowestY, largestY):
                try:
                    hasSpawned = spawnGrid[(i, j)]
                except:
                    hasSpawned = False
                if not hasSpawned:
                    x = int((self.getScreenX(i * 1000 + 500)))
                    y = int((self.getScreenY(j * 1000 + 500)))
                    self.showCircle(3, (x, y), (0, 0, 0))

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)
        if self.usePygame:
            self .diplay = pygame.display.set_mode((self.window.width, self.window.height))
        else:
            self.canvas.config(width=self.window.width, height=self.window.height)

    def scale(self, image, scale):
        newWidth = image.size[0] * scale
        wPercent = (newWidth/float(image.size[0]))
        hSize = int((float(image.size[1])*float(wPercent)))
        scaledImage = image.resize((int(newWidth), int(hSize)), PIL.Image.ANTIALIAS)
        return scaledImage

    def rotate(self, image, angle):
        if self.usePygame:
            return pygame.transform.rotate(image, angle)
        else:
            return self.rotatePIL(image, angle)

    def rotatePIL(self, image, angle):
        startSize = image.size
        imageString = image.convert('RGBA')
        rotatedImage = imageString.rotate(angle, expand=0).resize(startSize)
        finalImage = Image.new("RGBA", startSize, (255, 255, 255, 0))
        finalImage.paste(rotatedImage, (0, 0), rotatedImage)
        return finalImage

    def convertToDisplayFormat(self, image):
        if self.usePygame:
            imageBytes = image.convert('RGBA').tobytes("raw", 'RGBA')
            convertedImage = pygame.image.fromstring(imageBytes, image.size, 'RGBA')
        else:
            convertedImage = image
        return convertedImage

    def manipulateImage(self, image, scale, angle):
        scaledImage = self.scale(image, scale)
        rotatedImage = self.rotatePIL(scaledImage, angle)
        finalImage = self.convertToDisplayFormat(rotatedImage)
        return finalImage

    def getScreenX(self, x):
        return (-self.window.gameEngine.character.x + self.window.gameEngine.character.screenX + x) * self.window.gameEngine.scaleEngine.getScale()

    def getScreenY(self, y):
        return (self.window.gameEngine.character.y + self.window.gameEngine.character.screenY - y) * self.window.gameEngine.scaleEngine.getScale()

    def hide(self):
        self.f.pack_forget()