#
from math import *

Precision = 3 #For Rounding

#([X, Y], [X, Y])
def DistanceFormula(Point1, Point2):
    return round(sqrt((Point2[0]- Point1[0])**2 + (Point2[1]- Point1[1])**2), Precision)

#RectPoint = [X, Y]
def RectToHex(RectPoint):
    return [RectPoint[0] * 1.5, (RectPoint[1] * SQRTOF3) + (RectPoint[0] * HSQRTOF3)]

def CountCenters(HexagonSize):
    pass

SideLength = 1
CenterDistance = round(sqrt(3), Precision)
Apothem = round(sqrt(3)/2, Precision)

def main():

if __name__ == '__main__':
    main()
