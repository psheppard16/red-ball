from tkinter import *
from PIL import ImageTk
class Options:
    def __init__(self, window):
        self.window = window
        self.parent = window
        self.root = window.root
        self.f = Frame(self.root, bg="blue", width=self.window.width, height=self.window.width)
        self.f.pack_propagate(0)

        self.backgroundImage= ImageTk.PhotoImage(file="Backgrounds/options.png")
        self.backgroundLabel = Label(self.root, image=self.backgroundImage)

        self.showBackgroundF = StringVar()
        if self.window.save.showBackground:
            self.showBackgroundF.set("Show backgrounds")
        else:
            self.showBackgroundF.set("Don't show backgrounds")
        self.showBackgroundB = Button(self.root, textvariable=self.showBackgroundF, command=self.showBackground, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.showBackgroundB.pack(in_=self.f, pady=15)

        self.resolutionF = StringVar()
        self.resolutionF.set("Resolution: " + self.window.save.resolution)
        self.resolutionB = Button(self.root, textvariable=self.resolutionF, command=self.resolution, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.resolutionB.pack(in_=self.f, pady=15)

        self.frameF = StringVar()
        if self.window.save.smoothFrames == True:
            self.frameF.set("Smooth framerate transitions on")
        else:
            self.frameF.set("Smooth framerate transitions off")
        self.frameB = Button(self.root, textvariable=self.frameF, command=self.frame, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.frameB.pack(in_=self.f, pady=15)

        self.scaleF = StringVar()
        if self.window.save.smoothScale == True:
            self.scaleF.set("Smooth scaling on")
        else:
            self.scaleF.set("Smooth scaling off")
        self.scaleB = Button(self.root, textvariable=self.scaleF, command=self.scale, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.scaleB.pack(in_=self.f, pady=15)

        self.invertedF = StringVar()
        if self.window.save.invertedControls == True:
            self.invertedF.set("Inverted controls on")
        else:
            self.invertedF.set("Inverted controls off")
        self.invertedB = Button(self.root, textvariable=self.invertedF, command=self.inverted, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.invertedB.pack(in_=self.f, pady=15)

        self.showOutlineF = StringVar()
        if self.window.save.outlineMode == "simple":
            self.showOutlineF.set("Fancy outline: simple")
        elif self.window.save.outlineMode == "off":
            self.showOutlineF.set("Fancy outline: off")
        elif self.window.save.outlineMode == "fancy":
            self.showOutlineF.set("Fancy outline: fancy")
        self.showOutlineB = Button(self.root, textvariable=self.showOutlineF, command=self.showOutline, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.showOutlineB.pack(in_=self.f, pady=15)

        self.accept = Button(self.root, text="Accept", command=self.accept, bg="#%02x%02x%02x" % (255, 165, 0), font="Helvetica 15 bold", padx=10, pady=10)
        self.accept.pack(in_=self.f, pady=15)

    def update(self):
        self.f.config(width=self.window.width, height=self.window.width)

    def setUp(self):
        self.backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
        if self.window.save.outlineMode == "simple":
            self.showOutlineF.set("Fancy outline: simple")
        elif self.window.save.outlineMode == "off":
            self.showOutlineF.set("Fancy outline: off")
        elif self.window.save.outlineMode == "fancy":
            self.showOutlineF.set("Fancy outline: fancy")

        if self.window.save.invertedControls == True:
            self.invertedF.set("Inverted controls on")
        else:
            self.invertedF.set("Inverted controls off")

        if self.window.save.smoothScale == True:
            self.scaleF.set("Smooth scaling on")
        else:
            self.scaleF.set("Smooth scaling off")

        if self.window.save.smoothFrames == True:
            self.frameF.set("Smooth framerate transitions on")
        else:
            self.frameF.set("Smooth framerate transitions off")

        self.resolutionF.set("Resolution: " + self.window.save.resolution)

        if self.window.save.showBackground:
            self.showBackgroundF.set("Show backgrounds")
        else:
            self.showBackgroundF.set("Don't show backgrounds")

        self.f.pack(side=LEFT)

    def accept(self):
        self.window.rMenu = "charScreen"

    def hide(self):
        self.backgroundLabel.place(x=10000, y=10000, relwidth=1, relheight=1)
        self.f.pack_forget()

    def showOutline(self):
        if self.window.save.outlineMode == "off":
            self.window.save.outlineMode = "simple"
            self.showOutlineF.set("Fancy outline: simple")
        elif self.window.save.outlineMode == "simple":
            self.window.save.outlineMode = "fancy"
            self.showOutlineF.set("Fancy outline: fancy")
        elif self.window.save.outlineMode == "fancy":
            self.window.save.outlineMode = "off"
            self.showOutlineF.set("Fancy outline: off")

    def resolution(self):
        if self.window.save.resolution == "1280x720":
            self.window.save.resolution = "1366x768"
            self.resolutionF.set("Resolution: " + "1366x768")
        elif self.window.save.resolution == "1366x768":
            self.window.save.resolution = "1600x900"
            self.resolutionF.set("Resolution: " + "1600x900")
        elif self.window.save.resolution == "1600x900":
            self.window.save.resolution = "1920x1080"
            self.resolutionF.set("Resolution: " + "1920x1080")
        elif self.window.save.resolution == "1920x1080":
            self.window.save.resolution = "2048x1152"
            self.resolutionF.set("Resolution: " + "2048x1152")
        elif self.window.save.resolution == "2048x1152":
            self.window.save.resolution = "2560x1440"
            self.resolutionF.set("Resolution: " + "2560x1440")
        elif self.window.save.resolution == "2560x1440":
            self.window.save.resolution = "1280x720"
            self.resolutionF.set("Resolution: " + "1280x720")

    def showBackground(self):
        if self.window.save.showBackground:
            self.window.save.showBackground = False
            self.showBackgroundF.set("Don't show background")
        else:
            self.window.save.showBackground = True
            self.showBackgroundF.set("Show background")

    def frame(self):
        if self.window.save.smoothFrames:
            self.window.save.smoothFrames = False
            self.frameF.set("Smooth framerate transitions off")
        else:
            self.window.save.smoothFrames = True
            self.frameF.set("Smooth framerate transitions on")

    def scale(self):
        if self.window.save.smoothScale:
            self.window.save.smoothScale = False
            self.scaleF.set("Smooth scaling off")
        else:
            self.window.save.smoothScale = True
            self.scaleF.set("Smooth scaling on")

    def inverted(self):
        if self.window.save.invertedControls:
            self.window.save.invertedControls = False
            self.invertedF.set("Inverted controls off")
        else:
            self.window.save.invertedControls = True
            self.invertedF.set("Inverted controls on")