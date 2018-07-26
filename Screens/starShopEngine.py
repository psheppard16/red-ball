from tkinter import Frame, Label, Button, TOP, RIGHT, LEFT, CENTER, BOTTOM
from PIL import Image, ImageTk
import PIL
from Screens.shopButton import ShopButton
class StarShopEngine:
    def __init__(self, window):
        self.window = window
        self.normalShop = True
        self.f = Frame(self.window.root, bg="blue", width=self.window.width, height =self.window.height)
        self.f.pack_propagate(0)

        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/starShop.png")
        self.backgroundLabel = Label(self.f, image=self.backgroundImage)

        self.shopScale = self.window.width / 1280
        self.save = self.window.save
        barScale = self.shopScale / 5
        buttonScale = self.shopScale / 2

        self.barImageList = []
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar1.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar2.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar3.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar4.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar5.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar6.png", barScale))

        self.buttonList = []


        self.sideBar = Label(self.window.root, bg="#%02x%02x%02x" % (121, 202, 249), width=self.window.width // 5, height=self.window.height)
        self.sideBar.pack(in_=self.f, side=LEFT, pady=25, padx = 25)

        self.buttonGrid = Label(self.window.root, bg="#%02x%02x%02x" % (121, 202, 249), width=self.window.width // 5 * 3, height =self.window.height)
        self.buttonGrid.pack(in_=self.f, side=TOP)

        self.moneyL = Label(self.window.root, text="Stars: " + str(self.save.stars), bg="#%02x%02x%02x" % (121, 202, 249), font="Helvetica 15 bold", width=self.window.width // 5)
        self.moneyL.pack(side=TOP, in_=self.sideBar, pady=25)

        self.achievementB = Button(self.window.root, text="Shop", command=self.shop, bg="#%02x%02x%02x" % (255, 165, 0), width=self.window.width // 5, font="Helvetica 15 bold")
        self.achievementB.pack(side=BOTTOM, in_=self.sideBar, pady=25)

        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 0, 0), width=self.window.width // 5, font="Helvetica 15 bold")
        self.accept.pack(side=BOTTOM, in_=self.sideBar)


        self.shieldButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxFuelButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starFuelCanLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 0, 0,
                   """Fuel Cans:
Doubles the amount of fuel than fuel cans give you""",
                   self.window.root, image=self.shieldButtonImage)
        self.airResistButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/propulsionButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starSpeedGateLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 1, 0,
                   """Speed Gates:
Doubles the acceleration from speed gates""",
                   self.window.root, image=self.airResistButtonImage)
        self.antiGravButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/shieldButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starShieldLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 2, 0,
                   """Shields:
Reduces the amount of pull from black holes based on your number of shields""",
                   self.window.root, image=self.antiGravButtonImage)
        self.frictionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/magnetButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starMagnetLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 0, 1,
                   """Magnet:
Gives you a magnet that sucks in blobs""",
                   self.window.root, image=self.frictionButtonImage)
        self.launchSpeedButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/predictionButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starPredictionLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 1, 1,
                   """Predictions:
Displays a line that shows the path you will travel along""",
                   self.window.root, image=self.launchSpeedButtonImage)
        self.maxMassButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/blackHoleButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.starBlackHoleLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 2, 1,
                   """Black hole warnings:
Displays arrows that point towards black holes""",
                   self.window.root, image=self.maxMassButtonImage)


    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

        self.shopScale = self.window.width / 1280
        self.save = self.window.save
        barScale = self.shopScale / 5
        buttonScale = self.shopScale / 2

        self.sideBar.config(width=self.window.width // 5, heigh=self.window.height)
        self.buttonGrid.config(width=self.window.width // 5 * 3, height=self.window.height)

        self.barImageList.clear()
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar1.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar2.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar3.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar4.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar5.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar6.png", barScale))

        self.buttonGrid.config(width=self.window.width // 5 * 3, height=self.window.height)
        try:
            self.shieldButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxFuelButton.png"), buttonScale))
            self.buttonList[0].config(image=self.shieldButtonImage)
            self.airResistButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/propulsionButton.png"), buttonScale))
            self.buttonList[1].config(image=self.airResistButtonImage)
            self.antiGravButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/shieldButton.png"), buttonScale))
            self.buttonList[2].config(image=self.antiGravButtonImage)
            self.frictionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/magnetButton.png"), buttonScale))
            self.buttonList[3].config(image=self.frictionButtonImage)
            self.launchSpeedButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/predictionButton.png"), buttonScale))
            self.buttonList[4].config(image=self.launchSpeedButtonImage)
            self.maxMassButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/blackHoleButton.png"), buttonScale))
            self.buttonList[5].config(image=self.maxMassButtonImage)
        except:
            pass

    def accept(self):
        #must add in saving here, buttons dont currently do anything
        self.window.rMenu = "charScreen"

    def shop(self):
        self.window.rMenu = "shop"

    def run(self):
        #must save levels here
        for button in self.buttonList:
            button.run()
        self.save = self.window.save
        self.moneyL.config(text="Stars: " + str(int(self.save.stars)))
        for button in self.buttonList:
            button.save = self.window.save

        self.window.save.starFuelCanLevel = self.buttonList[0].level
        self.window.save.starSpeedGateLevel =self.buttonList[1].level
        self.window.save.starShieldLevel = self.buttonList[2].level
        self.window.save.starMagnetLevel = self.buttonList[3].level
        self.window.save.starPredictionLevel = self.buttonList[4].level
        self.window.save.starBlackHoleLevel = self.buttonList[5].level


    def scale(self, image, scale):
        newWidth = image.size[0] * scale
        wPercent = (newWidth/float(image.size[0]))
        hSize = int((float(image.size[1])*float(wPercent)))
        scaledImage = image.resize((int(newWidth), int(hSize)), PIL.Image.ANTIALIAS)
        return scaledImage

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.sideBar.place(x=10000, y=10000, relwidth=.15, relheight=1)
        self.f.pack_forget()

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.sideBar.place(x=0, y=0, relwidth=.15, relheight=1)
        self.buttonList[0].level = self.window.save.starFuelCanLevel
        self.buttonList[1].level = self.window.save.starSpeedGateLevel
        self.buttonList[2].level = self.window.save.starShieldLevel
        self.buttonList[3].level = self.window.save.starMagnetLevel
        self.buttonList[4].level = self.window.save.starPredictionLevel
        self.buttonList[5].level = self.window.save.starBlackHoleLevel


        self.f.pack()

    def openTkImage(self, path, scale):
        return ImageTk.PhotoImage(self.scale(Image.open(path), scale).convert("RGB"))
