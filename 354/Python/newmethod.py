#
#Only works if side length is 1

import math
import matplotlib.pyplot as plt

SQRTOF3 = math.sqrt(3)
HSQRTOF3 = SQRTOF3 / 2
Length = math.sqrt(21)
#Length = 111111111
#Length = 3

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

def DistanceFormula(Point1, Point2):
    return round(math.sqrt((Point2[0]- Point1[0])**2 + (Point2[1]- Point1[1])**2), 3)

#RectPoint = [X, Y]
def RectToHex(RectPoint):
    return [RectPoint[0] * SQRTOF3, (RectPoint[1] * SQRTOF3) + (RectPoint[0] * HSQRTOF3)]

def main():
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(Length * -1.2, Length * 1.2)
    plt.ylim(Length * -1.2, Length * 1.2)
    plt.grid(True)
    plt.plot(0,0,marker='o')
    #plt.plot([0,0], [0, Length],marker='o',markerfacecolor='blue', linestyle='dashed')
    I = 0
    NumOfPoints = 0
    while True:
        if SQRTOF3 * I >= Length:
            NumOfPoints = I - 1
            break
        I += 1
        Test = HexagonPoints(0, 0, I)
        for i in Test:
            plt.plot(i[0], i[1], marker='h', color='g')
    print 'Hexagon \'Size\':', I
    print 'Points On One Side:', NumOfPoints
    Count = 0
    for i in range(0, I):
        print [i, I - i]
        Point = RectToHex([i, I - i])
        plt.plot([Point[0]], [Point[1]], marker='h', color='r')
        print RectToHex([i, I - i])
        print DistanceFormula([0.000, 0.000], RectToHex([i, I - i]))
        if DistanceFormula([0.000, 0.000], RectToHex([i, I - i])) == round(Length, 3):
            Count += 6
    print Count
    plt.show()

if __name__ == '__main__':
    main()
