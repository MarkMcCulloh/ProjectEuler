import random, sys, pygame, math
from pygame.gfxdraw import *
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

WHITE    = (255, 255, 255)
DARKGRAY = ( 70,  70,  70)
BLACK    = (  0,   0,   0)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)

def HexagonPoints(Centerx, Centery, SideLength):
    PointList = []
    SideLength *= 3 ** .5
    HalfSideLength = SideLength * .5
    PointList.append((Centerx, Centery + SideLength))
    PointList.append((Centerx + SideLength, Centery + HalfSideLength))
    PointList.append((Centerx + SideLength, Centery - HalfSideLength))
    PointList.append((Centerx, Centery - SideLength))
    PointList.append((Centerx - SideLength, Centery - HalfSideLength))
    PointList.append((Centerx - SideLength, Centery + HalfSideLength))
    return PointList

def CheckForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        pygame.quit() # terminate if any QUIT events are present
        sys.exit()
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            pygame.quit() # terminate if the KEYUP event was for the Esc key
            sys.exit()
        pygame.event.post(event) # put the other KEYUP event objects back

def NormalPlot(Window, x, y, Color):
    pygame.gfxdraw.pixel(Window, 500 + x, 500 + y, Color)

def HexPlot(Window, x, y, Color):
    pygame.gfxdraw.pixel(Window, 500 + x + .5, 500 + y, Color)

def main():
    pygame.init()
    global FPSCLOCK, WINDOW
    FPSCLOCK = pygame.time.Clock()
    WINDOW = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('Hexagon Utility')
    WINDOW.fill(BLACK)
    pygame.gfxdraw.pixel(WINDOW, 500 + 0, 500 + 0, WHITE)
    NormalPlot(WINDOW, 0, 0, WHITE)
    NormalPlot(WINDOW, 1, 0, WHITE)
    NormalPlot(WINDOW, 2, 0, WHITE)
    #HexPlot(WINDOW, 0, 0, WHITE)
    while True:
        CheckForQuit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()
