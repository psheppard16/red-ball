__author__ = 'psheppard16'
try:
    import pygame
except:
    pass
class SoundEngine:
    def __init__(self, window):
        self.window = window
        pygame.mixer.init()
        self.songLength = 114
        self.startTime = -self.songLength
        self.soundStartTime = 0
        self.soundLength = 4
        self.bounceSound = pygame.mixer.Sound('Sounds/bounceSound.wav')
        vol = self.bounceSound.get_volume()
        self.bounceSound.set_volume(min(vol * 5, 1.0))
        self.ejectionSound = pygame.mixer.Sound('Sounds/ejectionSound.wav')
        vol = self.ejectionSound.get_volume()
        self.ejectionSound.set_volume(min(vol * .2, 1.0))

    def runSong(self):
        if self.window.frameRate.getTime() > self.startTime + self.songLength:
            self.startTime = self.window.frameRate.getTime()
            pygame.mixer.music.load("Sounds/Music/mainTheme.mp3")
            vol =  pygame.mixer.music.get_volume()
            pygame.mixer.music.set_volume(min(vol * .25, 1.0))
            pygame.mixer.music.play()

    def playBounceSound(self):
        pygame.mixer.Sound.play(self.bounceSound)

    def playEjectionSound(self):
        pygame.mixer.Sound.play(self.ejectionSound)