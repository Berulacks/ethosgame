import sys, pygame, ethos
from pygame.locals import *
from pygame import time, display, image, font, cdrom, mixer, draw, event, surface, sprite 
from ethos.gameobject import GameObject
from ethos.levels.level0 import Level0

class EthosMain:

    def __init__(self):

        self.Clock = time.Clock()
        self.aColor = Color(255,255,255)
        self.mouseX, self.mouseY = 0,0
        #fontObj = font.Font('cantarell.ttf', 32)

        
        self.loadLevel()

        print("Initialized")


    def loadLevel(self):

        self.activeState = Level0()

    def run(self):

        window = display.get_surface()

        for evt in event.get():
            if evt.type == pygame.QUIT:
                self.quit()
            elif evt.type == pygame.MOUSEMOTION:
                self.processMouseMotion(evt.pos)

            elif evt.type == pygame.KEYDOWN:
                self.processKeyDown(evt.key)
            
            elif evt.type == pygame.MOUSEBUTTONDOWN:
                self.processMouseButtonDown(evt.pos)

            elif evt.type == pygame.MOUSEBUTTONUP:
                self.processMouseButtonUp(evt.pos)

        window.fill(self.aColor)

        #self.testObj.rect.x = self.mouseX
        #self.testObj.rect.y = self.mouseY
        #self.activeSprites.draw(window)

        self.activeState.update(self.Clock.get_time())
        self.activeState.activeSprites.draw(window)
        #if len(self.activeState.pts) > 1:
        #    draw.lines(window, (255,0,255), False, self.activeState.pts, 3) 

        self.Clock.tick(30)
        display.flip()
        self.run()
    
    def processMouseMotion(self, pos):
        self.mouseX = pos[0]
        self.mouseY = pos[1]
        self.activeState.processMouseMotion(pos)

    def processKeyDown(self, key):
        if key == pygame.K_SPACE:
            display.toggle_fullscreen()
        elif key == pygame.K_ESCAPE:
            self.quit()
        else:
            self.activeState.processKeyDown(key)

    def processMouseButtonDown(self, pos):
        self.activeState.processMouseButtonDown(pos)

    def processMouseButtonUp(self, pos):
        self.activeState.processMouseButtonUp(pos)

    def quit(self):
        pygame.quit()
        sys.exit()

def main():
    pygame.init()
    display.set_mode((1280,720), pygame.RESIZABLE)
    display.set_caption("Ethos")
    display.set_gamma_ramp
    game = EthosMain()
    game.run()

if __name__ == '__main__':
    main()
