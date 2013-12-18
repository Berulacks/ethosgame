from abc import ABCMeta, abstractmethod
from pygame import Surface

class State:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.surface = Surface((300,300))

    def getSurface(self):
        return self.surface

    def setSurface(self, surface):
        self.surface = surface

    @abstractmethod
    def update(self, dT):
        pass

