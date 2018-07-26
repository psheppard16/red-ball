from tkinter import *
import tkinter as tk
from PIL import ImageTk
class Instructions:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.window.width, height =self.window.width)
        self.f.pack_propagate(0)
        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/instructions.png")
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        instructions = """Objective:
The goal of RedBall is to collect as much mass as possible, then buy items with your mass in order to collect even more!
Mechanics:
Watch out for black holes; when you touch them, they take away all your mass!
Speed gates will propel you foward, but if you touch their end caps, they will be destroyed.
Shields will allow you to touch a black hole and not lose any mass in the process.
Fuel cans will give you more fuel (I didn't think it was necessay to say this, but who knows?)
You can collect stars and use them to buy special upgrades in the star shop.
Controls:
Aim you blob with the mouse, and fire your rocket with space bar."""

        self.descriptionL = Label(window.root, text=instructions, justify=CENTER, bg="#%02x%02x%02x" % (121, 202, 249), compound=CENTER, wraplength=self.window.width // 1.25, font="Helvetica 15 bold")
        self.descriptionL.pack(in_=self.f, side=TOP, pady=10)

        self.cancel = Button(self.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=15)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.f.pack(side=LEFT)

    def cancel(self):
        print("button pressed")
        if self.window.saveSelected:
            self.window.rMenu = "charScreen"
        else:
            self.window.rMenu = "mainMenu"

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()
