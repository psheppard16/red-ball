__author__ = 'psheppard16'
from tkinter import *
import tkinter as tk
from PIL import ImageTk
class CharScreen:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.parent.width, height=self.parent.height)
        self.f.pack_propagate(0)
        self.backgroundNumber = 1
        self.backgroundImage1= ImageTk.PhotoImage(file="Backgrounds/mainMenu1.png")
        self.backgroundImage2= ImageTk.PhotoImage(file="Backgrounds/mainMenu2.png")
        self.backgroundImage3= ImageTk.PhotoImage(file="Backgrounds/mainMenu3.png")
        self.backgroundImage4= ImageTk.PhotoImage(file="Backgrounds/mainMenu4.png")
        self.backgroundImage5= ImageTk.PhotoImage(file="Backgrounds/mainMenu5.png")
        self.backgroundImage6= ImageTk.PhotoImage(file="Backgrounds/mainMenu6.png")
        self.backgroundImage7= ImageTk.PhotoImage(file="Backgrounds/mainMenu7.png")
        self.backgroundImage8= ImageTk.PhotoImage(file="Backgrounds/mainMenu8.png")
        self.backgroundLabel1 = Label(self.root, image=self.backgroundImage1)
        self.backgroundLabel2 = Label(self.root, image=self.backgroundImage2)
        self.backgroundLabel3 = Label(self.root, image=self.backgroundImage3)
        self.backgroundLabel4 = Label(self.root, image=self.backgroundImage4)
        self.backgroundLabel5 = Label(self.root, image=self.backgroundImage5)
        self.backgroundLabel6 = Label(self.root, image=self.backgroundImage6)
        self.backgroundLabel7 = Label(self.root, image=self.backgroundImage7)
        self.backgroundLabel8 = Label(self.root, image=self.backgroundImage8)
        self.launchB = Button(self.root, text="Launch!", command=self.launch, bg="#%02x%02x%02x" % (50, 255, 50), font="Helvetica 15 bold", padx=10, pady=10)
        self.launchB.pack(in_=self.f, pady=15)
        self.shopB = Button(self.root, text="Shop", command=self.shop, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.shopB.pack(in_=self.f, pady=15)
        self.achievementB = Button(self.window.root, text="Star Shop", command=self.achievement, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.achievementB.pack(in_=self.f, pady=15)
        self.instructionsB = Button(self.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)
        self.optionsB = Button(self.root, text="Options", command=self.options, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.optionsB.pack(in_=self.f, pady=15)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def achievement(self):
        self.window.rMenu = "starShop"

    def setUp(self):
        if self.backgroundNumber == 1:
            self.backgroundLabel1.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 2:
            self.backgroundLabel2.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 3:
            self.backgroundLabel3.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 4:
            self.backgroundLabel4.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 5:
            self.backgroundLabel5.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 6:
            self.backgroundLabel6.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 7:
            self.backgroundLabel7.place(x=0, y=0, relwidth=1, relheight=1)
        elif self.backgroundNumber == 8:
            self.backgroundLabel8.place(x=0, y=0, relwidth=1, relheight=1)
        self.f.pack(side=LEFT)
        if self.backgroundNumber < 8:
            self.backgroundNumber += 1
        else:
            self.backgroundNumber = 1

    def options(self):
        self.window.rMenu = "options"

    def instructions(self):
        self.window.rMenu = "instructions"

    def launch(self):
        self.window.rMenu = "gameEngine"

    def shop(self):
        self.window.rMenu = "shop"

    def hide(self):
        self.backgroundLabel1.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel2.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel3.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel4.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel5.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel6.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel7.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.backgroundLabel8.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()