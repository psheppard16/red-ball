from Screens.screen import Screen
from tkinter import *
class Instructions(Screen):
    def __init__(self, window):
        super().__init__(window, "instructions", backgroundPath="Backgrounds/instructions.png")
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

        self.cancel = Button(self.window.root, text="Cancel", command=self.cancel, bg="#%02x%02x%02x" % (255, 0, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.cancel.pack(in_=self.f, pady=15)

    def cancel(self):
        if self.window.saveSelected:
            self.window.rMenu = "mainMenu"
        else:
            self.window.rMenu = "startScreen"
