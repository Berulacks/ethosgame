import sys,os
#sys.path.append(os.path.join(os.path.dirname(__file__), '../../..'))
#from ethosgame.ethos.level import Level
from ..level import Level
#from ethosgame.ethos.gameobject import GameObject
from ..gameobject import GameObject
#from ethosgame.ethos.drawnobject import DrawnObject
from ..drawnobject import DrawnObject
import pygame
from pygame.locals import *
from pygame import Color, image, font, sprite

class Level0(Level):

    def __init__(self):
        super(Level0, self).__init__()

        self.activeSprites = sprite.RenderClear()
        self.drawnSprites = []
        self.npc = GameObject(image.load('User.png'), 100,50)
        self.activeSprites.add(self.npc)
        
        self.block1 = GameObject(image.load('platform.png'), 100, 400)
        self.activeSprites.add(self.block1);

        self.mousex = 0
        self.mousey = 0

	#The highest height our npc
	#can climb. If a the dY with a
	#point is higher than this, the
	#npc will just fall to his death
	self.MAX_HILL_HEIGHT = 3

	self.toDrawRectTopLeft = (0,0)
	self.toDrawRectBottomRight = (0,0)

        self.drawing = False

        self.pts = []

        print "Level 0 initialized."

    def update(self, dT):
        #print "Running level0"
        #Character info
        for gobject in self.activeSprites:
            if gobject is not self.npc:
                if not gobject.rect.colliderect(self.npc.rect):
                    #if self.npc.vy < 0.3 and (gobject.rect.y >= self.npc.rect.y + self.npc.rect.height):
                    if self.npc.vy < 0.3:
                        self.npc.vy += 0.1 
                else:
                    self.npc.vy = 0

            gobject.update(dT)

	collidingPoints = []
        for drawnstuff in self.drawnSprites:
	    for point in drawnstuff.pts:
	        x = self.npc.rect.collidepoint(point)
	        if x:
                    collidingPoints.append(point)
        if(len(collidingPoints) > 0):
            self.npc.processPointCollision(collidingPoints)



    def processKeyDown(self,key):
        print "You hit the key " + str(key) + "!"
        if key == pygame.K_RIGHT:
            self.npc.vx = 0.1

    def processMouseMotion(self,pos):
        #print "Your mouse is at " + str(pos[0]) + " " + str(pos[1])
        self.mousex = pos[0]
        self.mousey = pos[1]
        if self.drawing and len(self.pts) < 100:
            self.pts.append( pos )

    def processMouseButtonDown(self, pos):
        print "Ya clicked at " + str(pos[0]) + " " + str(pos[1]) + " ya goof!"
        self.drawing = True
	
	self.toDrawRectTopLeft = (pos[0],pos[1])
        if len(self.pts) > 0:
            self.pts = []


    def processMouseButtonUp(self, pos):
        print "Ya let go"
        if self.drawing is True:
            self.drawing = False
            self.drawnSprites.append ( DrawnObject(self.pts) )
	    self.toDrawRectBottomRight = (pos[0], pos[1])


