import pygame
from ethos.gameobject import GameObject
from pygame import sprite, Surface, mask, draw, image, rect

class DrawnObject(GameObject):

    def __init__(self, pts):
        #print "Creating drawn object"
        self.pts = pts

        surface = Surface((1280,720))
        self.dSprite = sprite.Sprite()

	#self.dSprite.image = image.load('test.png')

        #self.dSprite.rect = draw.lines(surface, (255,0,255), False, pts, 3)
        #self.dSprite.mask = mask.from_surface(surface) 
