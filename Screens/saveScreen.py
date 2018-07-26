from tkinter import *
import tkinter as tk
from PIL import ImageTk
class SaveScreen:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.parent.width, height=self.parent.height)
        self.f.pack_propagate(0)
        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/saveScreen.png")
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        self.save1B = Button(self.root, text="Save file 1", command=self.save1, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save1B.pack(in_=self.f, pady=25)
        self.save2B = Button(self.root, text="save file 2", command=self.save2, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save2B.pack(in_=self.f, pady=25)
        self.save3B = Button(self.root, text="save file 3", command=self.save3, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.save3B.pack(in_=self.f, pady=25)
        self.cancel = Button(self.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=25)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.f.pack(side=LEFT)

    def save1(self):
        self.window.saveSelected = True
        self.window.saveNumber = 1
        self.window.loadChar(1)
        self.window.rMenu = "charScreen"

    def save2(self):
        self.window.saveSelected = True
        self.window.saveNumber = 2
        self.window.loadChar(3)
        self.window.rMenu = "charScreen"

    def save3(self):
        self.window.saveSelected = True
        self.window.saveNumber = 3
        self.window.loadChar(3)
        self.window.rMenu = "charScreen"

    def cancel(self):
        self.window.rMenu = "mainMenu"

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()