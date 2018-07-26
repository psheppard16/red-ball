__author__ = 'python'
from tkinter import Button, TOP, CENTER
from PIL import Image
import PIL
from tkinter import Label
import math
class ShopButton(Button):
    def __init__(self, window, level, buttonGrid, sideBar, save, buttonList, barImageList, backgroundImage, row, column, description, *args, **kwargs):
        super(ShopButton, self).__init__(*args, **kwargs)
        self.bind("<Enter>", self.mouseEnter)
        self.bind("<Leave>", self.mouseLeave)
        self.sideBar = sideBar
        self.backgroundImage = backgroundImage
        self.description = description
        self.buttonGrid = buttonGrid
        self.save = save
        self.window = window
        self.config(command=self.buy)
        self.cost = 0
        self.level = level
        buttonList.append(self)
        self.config(cursor="@Images/Shop/cursor.cur")

        self.itemFrame = Label(buttonGrid, bg="#%02x%02x%02x" % (121, 202, 249))
        self.itemFrame.grid(padx= 50, pady=15, row=row, column=column)

        self.barImageList = barImageList
        self.barLabel = Label(self.itemFrame, image=self.barImageList[0])
        self.pack(side=TOP, in_=self.itemFrame)
        self.barLabel.pack(side=TOP, in_=self.itemFrame)
        self.descriptionL = Label(window.root, text=self.description, justify=CENTER, bg="#%02x%02x%02x" % (121, 202, 249), compound=CENTER, wraplength=self.window.width // 7, font="Helvetica 15 bold")

        self.costL = Label(window.root, text="Costs: " + str(self.cost))

    def mouseEnter(self, event):
        self.descriptionL.pack(in_=self.sideBar, side=TOP, pady=10)
        self.costL.pack(in_=self.sideBar, side=TOP, pady=10)

    def mouseLeave(self, event):
        self.descriptionL.pack_forget()
        self.costL.pack_forget()

    def buy(self):
        if self.window.cMenu == "shop":
            if self.save.mass >= self.cost and self.level < 5:
                self.save.mass -= self.cost
                self.level += 1
        if self.window.cMenu == "starShop":
            if self.save.stars >= self.cost and self.level < 5:
                self.save.stars -= self.cost
                self.level += 5

    def run(self):
        if self.window.cMenu == "shop":
            if self.level == 0:
                self.cost = 500
            else:
                self.cost = 500 * (self.level * 4) ** 2
        elif self.window.cMenu == "starShop":
            self.cost = 5
        self.barLabel.config(image=self.barImageList[self.level])
        self.costL.config(text="Costs: " + str(self.cost), font="Helvetica 15 bold", bg="#%02x%02x%02x" % (121, 202, 249))

    def scale(self, image, scale):
        newWidth = image.size[0] * scale
        wPercent = (newWidth/float(image.size[0]))
        hSize = int((float(image.size[1])*float(wPercent)))
        scaledImage = image.resize((int(newWidth), int(hSize)), PIL.Image.ANTIALIAS)
        return scaledImage
