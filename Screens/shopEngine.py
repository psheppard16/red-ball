from tkinter import Frame, Label, Button, TOP, RIGHT, LEFT, CENTER, BOTTOM
from PIL import Image, ImageTk
import PIL
from Screens.shopButton import ShopButton
class ShopEngine:
    def __init__(self, window):
        self.window = window
        self.normalShop = True
        self.f = Frame(self.window.root, bg="blue", width=self.window.width, height =self.window.height)
        self.f.pack_propagate(0)

        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/shop.png")
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

        self.moneyL = Label(self.window.root, text="Mass: " + str(self.save.mass), bg="#%02x%02x%02x" % (121, 202, 249), font="Helvetica 15 bold", width=self.window.width // 5)
        self.moneyL.pack(side=TOP, in_=self.sideBar, pady=25)

        self.achievementB = Button(self.window.root, text="Star Shop", command=self.achievement, bg="#%02x%02x%02x" % (255, 165, 0), width=self.window.width // 5, font="Helvetica 15 bold")
        self.achievementB.pack(side=BOTTOM, in_=self.sideBar, pady=25)

        self.accept = Button(self.window.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 0, 0), width=self.window.width // 5, font="Helvetica 15 bold")
        self.accept.pack(side=BOTTOM, in_=self.sideBar)

        self.shieldButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/shieldButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.shieldLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 0, 0,
                   """Shield Capacity:
Increases the amount of sheilds you are able to hold""",
                   self.window.root, image=self.shieldButtonImage)
        self.airResistButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/airResistButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.airResistLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 1, 0,
                   """Aerodynamics:
Reduces air resistance, allowing you to fly farther and faster""",
                   self.window.root, image=self.airResistButtonImage)
        self.antiGravButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/antiGravButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.antiGravLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 2, 0,
                   """Anit-gravity:
Reduces the effect of gravity, causing increased time between bounces""",
                   self.window.root, image=self.antiGravButtonImage)
        self.frictionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/frictionButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.frictionLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 0, 1,
                   """Oil:
Reduces the friction between you and the ground, allowing you to bounce farther""",
                   self.window.root, image=self.frictionButtonImage)
        self.launchSpeedButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/launchSpeedButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.launchLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 1, 1,
                   """Launch Speed:
Increases the speed at which you launch, greatly increasing your trip length""",
                   self.window.root, image=self.launchSpeedButtonImage)
        self.maxMassButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxMassButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.maxMassLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 2, 1,
                   """Maximum Size:
Increases the size that you start your launch with, causing increased visibility and accelerated growth""",
                   self.window.root, image=self.maxMassButtonImage)
        self.growthRateButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/growthRateButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.growthRateLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 0, 2,
                   """Growth rate:
Increases the rate at which you grow, allowing you to make more money faster""",
                   self.window.root, image=self.growthRateButtonImage)
        self.maxFuelButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxFuelButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.maxFuelLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 1, 2,
                   """Max Fuel:
Increases the amount of fuel you start with, and the maximum amount you can hold""",
                   self.window.root, image=self.maxFuelButtonImage)
        self.propulsionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/propulsionButton.png"), buttonScale))
        ShopButton(self.window, self.window.save.propulsionLevel, self.buttonGrid, self.sideBar, self.save, self.buttonList, self.barImageList, self.backgroundImage, 2, 2,
                   """Rocket speed:
Increases the propulsion from your rocket, allowing you to maneuver more easily and go farther""",
                   self.window.root, image=self.propulsionButtonImage)


    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

        self.shopScale = self.window.width / 1280
        self.save = self.window.save
        barScale = self.shopScale / 5

        self.sideBar.config(width=self.window.width // 5, heigh=self.window.height)
        self.buttonGrid.config(width=self.window.width // 5 * 3, height=self.window.height)
        buttonScale = self.shopScale / 2

        self.barImageList.clear()
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar1.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar2.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar3.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar4.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar5.png", barScale))
        self.barImageList.append(self.openTkImage("Images/Shop/levelBar6.png", barScale))

        try:
            self.buttonGrid.config(width=self.window.width // 5 * 3, height=self.window.height)
            self.shieldButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/shieldButton.png"), buttonScale))
            self.buttonList[0].config(image=self.shieldButtonImage)
            self.airResistButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/airResistButton.png"), buttonScale))
            self.buttonList[1].config(image=self.airResistButtonImage)
            self.antiGravButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/antiGravButton.png"), buttonScale))
            self.buttonList[2].config(image=self.antiGravButtonImage)
            self.frictionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/frictionButton.png"), buttonScale))
            self.buttonList[3].config(image=self.frictionButtonImage)
            self.launchSpeedButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/launchSpeedButton.png"), buttonScale))
            self.buttonList[4].config(image=self.launchSpeedButtonImage)
            self.maxMassButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxMassButton.png"), buttonScale))
            self.buttonList[5].config(image=self.maxMassButtonImage)
            self.growthRateButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/growthRateButton.png"), buttonScale))
            self.buttonList[6].config(image=self.growthRateButtonImage)
            self.maxFuelButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/maxFuelButton.png"), buttonScale))
            self.buttonList[7].config(image=self.maxFuelButtonImage)
            self.propulsionButtonImage = ImageTk.PhotoImage(self.scale(Image.open("Images/Shop/propulsionButton.png"), buttonScale))
            self.buttonList[8].config(image=self.propulsionButtonImage)
        except:
            pass

    def accept(self):
        self.window.rMenu = "charScreen"

    def achievement(self):
        self.window.rMenu = "starShop"

    def run(self):
        self.moneyL.config(text="Mass: " + str(int(self.save.mass)))
        self.save = self.window.save
        for button in self.buttonList:
            button.save = self.window.save
            button.run()

        self.window.save.shieldLevel = self.buttonList[0].level
        self.window.save.airResistLevel = self.buttonList[1].level
        self.window.save.antiGravLevel = self.buttonList[2].level
        self.window.save.frictionLevel = self.buttonList[3].level
        self.window.save.launchLevel = self.buttonList[4].level
        self.window.save.maxMassLevel = self.buttonList[5].level
        self.window.save.growthRateLevel = self.buttonList[6].level
        self.window.save.maxFuelLevel = self.buttonList[7].level
        self.window.save.propulsionLevel = self.buttonList[8].level

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
        self.shopScale = self.window.width / 1280
        self.buttonList[0].level = self.window.save.shieldLevel
        self.buttonList[1].level = self.window.save.airResistLevel
        self.buttonList[2].level = self.window.save.antiGravLevel
        self.buttonList[3].level = self.window.save.frictionLevel
        self.buttonList[4].level = self.window.save.launchLevel
        self.buttonList[5].level = self.window.save.maxMassLevel
        self.buttonList[6].level = self.window.save.growthRateLevel
        self.buttonList[7].level = self.window.save.maxFuelLevel
        self.buttonList[8].level = self.window.save.propulsionLevel

        self.f.pack()

    def openTkImage(self, path, scale):
        return ImageTk.PhotoImage(self.scale(Image.open(path), scale).convert("RGB"))
