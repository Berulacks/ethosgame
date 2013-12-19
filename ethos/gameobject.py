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
	self.MAX_HILL_HEIGHT = 300
	self.vy = 0.0
	

    def update(self, dT):

        self.rect.x += self.vx * dT
        self.rect.y += self.vy * dT

    #This function takes a list of points we're
    #colliding with. If the points are
    #lower than the center, the object 
    def processPointCollision(self, points):
	
        print "Processing collisions"
	#mod = self.vx / -self.vx
        xExtreme = (0,0)
        yExtreme = (0,0)
	    
        for point in points:
            if(point[0] > xExtreme[0]):
                xExtreme = point
            if(point[1] > xExtreme[1]):
                yExtreme = point
	
        print "We be at (" + str(self.rect.x) + ", " + str(self.rect.y) + ")"
        print "xExtreme is (" + str(xExtreme[0]) + ", " + str(xExtreme[1]) + ")"

        base = self.rect.y + self.rect.width/2 + 5

        if yExtreme[1] < base:
            self.vy = abs(self.vy) * 0.2

        if xExtreme[1] > self.rect.x + self.rect.width:
            print "Diff is " + str(base - xExtreme[1])
            if base - xExtreme[1] <= self.MAX_HILL_HEIGHT:
                #print "Incrementing vy by " + str(xExtreme[1] - self.rect.y)
                self.vy = abs(base - xExtreme[1])




		#if(point.y < self.rect.y and self.vy < 0):
		#	self.vy = abs(self.vy) * 0.2

