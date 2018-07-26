__author__ = 'psheppard16'
import math
from PIL import Image
from GameObjects.mobile import Mobile
class BlackHole(Mobile):
    def __init__(self, window, x, y):
        super().__init__(window, x, y, 0, 0)
        self.radius = 100 #change to mass
        self.color = "black"
        self.cannotDespawn = .5
        self.imageUpdate = 0
        self.alive = True

    def run(self, blackHoleList, blobList, p, localScale, width, distance, TICK_SPEED):
        self.cannotDespawn -= TICK_SPEED
        if distance(p.x, p.y, self.x, self.y) < p.radius + self.radius: #add only hurt if bigger than virus
            if p.shield > 0:
                p.shield -= 1
            else:
                p.setMass(p.startMass)
                for b in blobList:
                    b.cannotDespawn = 1
                for h in blackHoleList:
                    h.cannotDespawn = 1
            self.alive = False
        if distance(p.x + width * 5 / 4 / localScale, p.y, self.x, self.y) > width * 1.5 / localScale and self.cannotDespawn < 0:
            self.alive = False

    def scaleRotateTranslate(self, image, angle, center = None, new_center = None, scale = None): #nowhere else to put this
        if center is None:
            return image.rotate(angle)
        angle = -angle/180.0*math.pi
        nx,ny = x,y = center
        sx=sy=1.0
        if new_center:
            (nx,ny) = new_center
        if scale:
            (sx,sy) = scale
        cosine = math.cos(angle)
        sine = math.sin(angle)
        a = cosine/sx
        b = sine/sx
        c = x-nx*a-ny*b
        d = -sine/sy
        e = cosine/sy
        f = y-nx*d-ny*e
        return image.transform(image.size, Image.AFFINE, (a,b,c,d,e,f), resample=Image.BICUBIC)