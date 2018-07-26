__author__ = 'psheppard16'
from tkinter import *
import tkinter as tk
from PIL import ImageTk
class MainMenu:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.parent.width, height=self.parent.height)
        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/mainMenu.png")
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)
        self.f.pack_propagate(0)
        self.startB = Button(self.root, text="Start", command=self.start, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.startB.pack(in_=self.f, pady=15)
        self.instructionsB = Button(self.root, text="Instructions", command=self.instructions, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.instructionsB.pack(in_=self.f, pady=15)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        self.f.pack(side=LEFT)

    def start(self):
        self.window.rMenu = "saveScreen"

    def instructions(self):
        self.window.rMenu = "instructions"

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()
