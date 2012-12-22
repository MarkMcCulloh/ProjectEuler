#
from math import *
import matplotlib.pyplot as pyplot

Precision = 6 #For Rounding
SQRTOF3 = round(sqrt(3), Precision)
HSQRTOF3 = round(SQRTOF3 / 2, Precision)

#List of Points [X, Y] that correspond to the six corners of the hexagon
def HexagonLines(Centerx, Centery, TSideLength):
    PointList = []
    A = TSideLength
    TSideLength *= SQRTOF3
    HalfSideLength = TSideLength * .5
    PointList.append((Centerx, Centery + TSideLength))
    PointList.append((Centerx + (1.5 * A), Centery + HalfSideLength))
    PointList.append((Centerx + (1.5 * A), Centery - HalfSideLength))
    PointList.append((Centerx, Centery - TSideLength))
    PointList.append((Centerx - (1.5 * A), Centery - HalfSideLength))
    PointList.append((Centerx - (1.5 * A), Centery + HalfSideLength))
    xpoints = []
    ypoints = []
    for i in PointList:
        xpoints.append(i[0])
        ypoints.append(i[1])
    xpoints.append(xpoints[0])
    ypoints.append(ypoints[0])
    return xpoints, ypoints

def HexLine(Centerx, Centery, SideLength):
    xpoints = [Centerx, Centerx + (1.5 * SideLength)]
    ypoints = [Centery + (SQRTOF3 * SideLength), Centery + ((SideLength * SQRTOF3) / 2)]
    return xpoints, ypoints

def sHexLine(Startx, Starty, SideLength):
    xpoints = [Startx, Startx + (1.5 * SideLength)]
    ypoints = [Starty, Starty - ((SideLength * SQRTOF3) / 2)]
    return xpoints, ypoints

#([X, Y], [X, Y])
def DistanceFormula(Point1, Point2):
    return round(sqrt((Point2[0]- Point1[0])**2 + (Point2[1]- Point1[1])**2), Precision)

#RectPoint = [X, Y]
def RectToHex(RectPoint):
    return [RectPoint[0] * 1.5, (RectPoint[1] * SQRTOF3) + (RectPoint[0] * HSQRTOF3)]

def CountCenters(HexagonSize):
    Ymax = HexagonSize * CenterD
    Done = False
    while not Done:
        i = Ymax
        Ymax -= CenterD

#Initial Stuff for the graph, plots a center and circle
def SetUpPyplot():
    pyplot.xlabel('x Coords')
    pyplot.ylabel('y Coords')
    pyplot.xlim(-1, Length * 1.2)
    pyplot.ylim(Length / 2, Length * 1.2)
    pyplot.grid(False)
    pyplot.plot(0,0,marker='+', color='g')
    Circle = pyplot.Circle((0,0),radius=Length)
    Circle.fill = False
    ax = pyplot.gca()
    ax.add_patch(Circle)

def main():
    Plot = True
    global CenterD, Length, SideLength, Apothem, CenterWidth
    MinLevel = MaxLevel = 0
    #SideLength = round(eval(raw_input('What is the length of the side of the hexagons?')), 3)
    SideLength = 1
    #Length = round(eval(raw_input('What is the distance you are looking for?')), 3)
    Length = 21
    #Length = SQRTOF3 * 20
    Apothem = round(SideLength / (2*(SQRTOF3/3)), Precision)
    CenterWidth = 1.5                #Make this modular
    CenterD = Apothem * 2
    MinLevel = int(Length/SQRTOF3)   #int(Length / CenterD)
    MaxLevel = int(Length/1.5)       #int(Length / CenterWidth)
    if Plot: SetUpPyplot()
    #
    print 'Regular Hexagon - Side Length:', SideLength
    print 'Regular Hexagon - Apothem:', Apothem
    print 'Regular Hexagon - Distance Between Adjacent Centers:', CenterD
    print 'Regular Hexagon - Width Between Adjacent Centers:', CenterWidth
    print 'Distance You Are Looking For:', Length
    print 'Minimum Hexagon \'Size\':', MinLevel
    print 'Maximum Hexagon \'Size\':', MaxLevel
    #
    if Plot:
        for i in range(MinLevel, MaxLevel + 1):
            xPoints, yPoints = HexagonLines(0, 0, i)
            pyplot.plot(xPoints, yPoints, marker='.', color='r', linestyle='solid', label='Min Hexagon')
    #

    if Plot: pyplot.show()


if __name__ == '__main__':
    main()
