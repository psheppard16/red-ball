__author__ = 'python'
from decimal import *
from PIL import Image
import PIL
import os.path
class ImageSaving:
    def __init__(self, rawImage, folderName, lowestScale, highestScale, step, round, roundString):
        self.rawImage = rawImage
        self.folderName = folderName
        self.lowestScale = lowestScale
        self.highestScale = highestScale
        self.step = step
        self.round = round
        self.roundString = roundString
        self.saveImages()

    def saveImages(self):
        self.scaleImages(int(self.lowestScale / self.step), int(self.highestScale / self.step))

    def scaleImages(self, lowest, highest):
        for scale in range(lowest, highest + 1):
            if round(scale * self.step + self.lowestScale, self.round) > 0:
                name = str(Decimal(scale * self.step).quantize(Decimal(self.roundString), rounding=ROUND_HALF_UP))
                basePath = os.path.dirname(os.path.dirname(__file__))
                path = basePath + "/ModifiedImages/" + self.folderName + "/" + name + ".png"
                if not os.path.isfile(path):
                    print(path)
                    image = self.scaleImage(self.rawImage, round(scale * self.step + self.lowestScale, self.round))
                    image.save(path, "PNG")

    def scaleImage(self, image, scale):
        newWidth = image.size[0] * scale
        wPercent = (newWidth/float(image.size[0]))
        hSize = int((float(image.size[1])*float(wPercent)))
        scaledImage = image.resize((int(newWidth), int(hSize)), PIL.Image.ANTIALIAS)
        return scaledImage