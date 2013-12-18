from state import State
from abc import ABCMeta, abstractmethod
from pygame import sprite

class Level(State):


    def __init__(self):
        super(Level, self).__init__()
        print "THIIIS IS A LEVEL"

    @abstractmethod
    def processKeyDown(self,key):
	    pass

    @abstractmethod
    def processMouseMotion(self,pos):
	    pass

    @abstractmethod
    def processMouseButtonDown(self, pos):
	    pass

    @abstractmethod
    def processMouseButtonUp(self, pos):
	    pass

