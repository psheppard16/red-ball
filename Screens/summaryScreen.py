from tkinter import *
import tkinter as tk
from PIL import ImageTk
class SummaryScreen:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="green", width=self.window.width, height =self.window.width)
        self.f.pack_propagate(0)
        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/summaryScreen.png")
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        self.distanceTraveled = StringVar()
        self.distanceTraveled.set("Distance traveled: " + str(int(self.window.gameEngine.character.x / 10)))
        self.distanceTraveledLabel = Label(self.root, textvariable=self.distanceTraveled, bg="#%02x%02x%02x" % (0, 165, 0), font="Helvetica 15 bold")
        self.distanceTraveledLabel.pack(in_=self.f, pady=25)
        self.massCollected = StringVar()
        self.massCollected.set("Mass Collected: " + str(int(self.window.gameEngine.character.massCollected)))
        self.massCollectedLabel = Label(self.root, textvariable=self.massCollected, bg="#%02x%02x%02x" % (0, 165, 0), font="Helvetica 15 bold")
        self.massCollectedLabel.pack(in_=self.f, pady=25)
        self.cancel = Button(self.root, text="Continue", command=self.cancel, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=25)
        self.shop = Button(self.root, text="Shop", command=self.shop, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.shop.pack(in_=self.f, pady=25)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.distanceTraveled.set("Distance traveled: " + str(int(self.window.gameEngine.character.x / 10)))
        self.massCollected.set("Mass Collected: " + str(int(self.window.gameEngine.character.massCollected)))
        self.f.pack(side=LEFT)

    def cancel(self):
        self.window.rMenu = "charScreen"

    def shop(self):
        self.window.rMenu = "shop"

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()