import pygame
from pygame import sprite

class GameObject(sprite.Sprite):

    def __init__(self, imageSurface, x, y):
	sprite.Sprite.__init__(self)
        #print("Heeeere's an object!")
	self.image = imageSurface
	self.rect = self.image.get_rect()
	self.rect.x = x
	self.rect.y = y
	self.vx = 0.0
	self.vy = 0.0
	

    def update(self, dT):

        self.rect.x += self.vx * dT
        self.rect.y += self.vy * dT
