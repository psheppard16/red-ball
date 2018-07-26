from abc import ABCMeta, abstractmethod
class GameObject(metaclass=ABCMeta):
    def __init__(self, window):
        self.window = window
        self.drawingEngine = window.drawingEngine
        self.alive = True

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def draw(self):
        pass