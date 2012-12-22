#Problem 354
#Numbers are rounded to 3 places (0.000) for comparison

import math, matplotlib.pyplot as pyplot

SQRTOF3 = math.sqrt(3)
HSQRTOF3 = SQRTOF3 / 2

#Test Cases
#Length = 1 * math.sqrt(3) #Should be 6#
#Length = math.sqrt(21) #Should be 12#
#Length = 3 #Should be 6#
#Length = 111111111 #Should be 54#
Length = 111*math.sqrt(3)

#List of Points [X, Y] that correspond to the six corners of the hexagon
def HexagonPoints(Centerx, Centery, SideLength):
    PointList = []
    A = SideLength
    SideLength *= 3 ** .5
    HalfSideLength = SideLength * .5
    PointList.append((Centerx, Centery + SideLength))
    PointList.append((Centerx + (1.5 * A), Centery + HalfSideLength))
    PointList.append((Centerx + (1.5 * A), Centery - HalfSideLength))
    PointList.append((Centerx, Centery - SideLength))
    PointList.append((Centerx - (1.5 * A), Centery - HalfSideLength))
    PointList.append((Centerx - (1.5 * A), Centery + HalfSideLength))
    return PointList

#([X, Y], [X, Y])
def DistanceFormula(Point1, Point2):
    return round(math.sqrt((Point2[0]- Point1[0])**2 + (Point2[1]- Point1[1])**2), 3)

#RectPoint = [X, Y]
def RectToHex(RectPoint):
    return [RectPoint[0] * 1.5, (RectPoint[1] * SQRTOF3) + (RectPoint[0] * HSQRTOF3)]

#Initial Stuff for the graph, plots a center and circle
def SetUpPyplot():
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    pyplot.xlim(Length * -1.2, Length * 1.2)
    pyplot.ylim(Length * -1.2, Length * 1.2)
    pyplot.grid(True)
    pyplot.plot(0,0,marker='+',  color='g')
    Circle = pyplot.Circle((0,0),radius=Length)
    Circle.fill = False
    ax = pyplot.gca()
    ax.add_patch(Circle)

def main():
    SetUpPyplot()
    I = 0
    NumOfPoints = 0
    while True:
        if SQRTOF3 * I >= Length:
            NumOfPoints = I - 1
            break
        I += 1
    print 'Hexagon \'Size\':', I
    print 'Points On One Side:', NumOfPoints

    Test = HexagonPoints(0, 0, I-1)
    Testx = []
    Testy = []
    for i in Test:
        Testx.append(i[0])
        Testy.append(i[1])
    Testx.append(Testx[0])
    Testy.append(Testy[0])
    pyplot.plot(Testx, Testy, marker='.', color='r', linestyle='dashed', label='Minimum Hexagon Level')

    Count = 0
    Even = False
    while True:
        #if I * SQRTOF3 == Length:
            #Count = 6
            #break
        LocalCount = 0
        if (I % 2 == 0): Even = True
        Done = False
        #print I
        for i in range(0, I):
            if Done: break
            #if not Even:
                #if i + 2 % 2 != 0 and i != 0: continue
            #if Even:
                #if i + 2 % 2 == 0 and i != 0: continue
            Point = RectToHex([i, I - i])
            print Point[0], Point[1]
            #if Point[1] > Length: continue
            pyplot.plot(Point[0], Point[1], marker='H', color='y')
            #print DistanceFormula([0.000, 0.000], [Point[0], Point[1]])
            if DistanceFormula([0.000, 0.000], [Point[0], Point[1]]) == round(Length, 3):
                pyplot.plot(Point[0], Point[1], marker='H', color='r')
                LocalCount += 1
                if not Even:
                    Count += 12
                    Point = RectToHex([I-i, i])
                    pyplot.plot(Point[0], Point[1], marker='H', color='r')
                else:
                    Count += 6
                    if I/2 > i:
                        Point = RectToHex([I-i, i])
                        pyplot.plot(Point[0], Point[1], marker='H', color='r')
                        Count += 6
                Done = True
            if DistanceFormula([0.000, 0.000], [Point[0], Point[1]]) < Length:
                break
        I += 1
        if I*1.5 > Length: break
    Lastx = [Testx[0], Testx[1]]
    Lasty = [Testy[0], Testy[1]]
    Test = HexagonPoints(0, 0, I-1)
    Testx = []
    Testy = []
    for i in Test:
        Testx.append(i[0])
        Testy.append(i[1])
    Testx.append(Testx[0])
    Testy.append(Testy[0])
    #pyplot.plot([Lastx[0], Testx[0]], [Lasty[0], Testy[0]], marker='.', color='g', linestyle='dashed')
    pyplot.plot(Testx, Testy, marker='.', color='b', linestyle='dashed', label='Maximum Hexagon Level')
    print Count
    pyplot.legend()
    pyplot.show()

if __name__ == '__main__':
    main()
