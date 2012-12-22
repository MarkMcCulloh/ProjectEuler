//Mark McCulloh
//2011-2012

#include <iostream>
#include <vector>
#include <math.h>
#include <iomanip>

using namespace std;

#define SQRT3 1.732050808
#define HSQRT3 0.8660254038

double Tolerance = .000001;

class Point
{
public:
    Point(double, double);
    double x, y;
    double GetHex_x();
    double GetHex_y();
};

Point::Point(double a, double b)
{
    x = a;
    y = b;
}

double Point::GetHex_x()
{
    return x * 1.5;
}

double Point::GetHex_y()
{
    return (y*SQRT3) + (x*HSQRT3);
}

double DistanceFormulaC(double x, double y)
{
    return sqrt(pow(x, 2) + pow(y, 2));
}

void PrintHelp()
{
    cout << "\n----------------------------------------------------------------------------\n\n";
    cout << "Enter a length (L) to gain the following info:\n";
    cout << "   1. Minimum hexagon level (L / SQRT(3))\n";
    cout << "   2. Maximum hexagon level (L / 1.5)\n";
    cout << "   3. Number of points to be tested\n";
    cout << "   4. Approximation of B(L)\n\n";
    cout << "L should be a number > 0 that is rounded to 3 decimal places (if needed)\n";
    cout << "Entering any letters will cause a seizure because I am lazy\n";
    cout << "Change the tolerance of the calculations by entering a negative number \n(default tolerance is .000001)\n";
    cout << "  For example: -.00001 changes the tolerance to .00001";
    cout << "\n\n----------------------------------------------------------------------------\n";
}

double GetInput()
{
    double in = 0;
    while(in <= 0)
    {
        cout << "\n>> ";
        cin >> in;
        if(in == 0)
        {
            PrintHelp();
            continue;
        }
        if(in < 0){
            Tolerance = in * -1;
            cout << "Tolerance set to " << Tolerance << ".\n";
            continue;
        }
    }
    return in;
}

double Round(double a)
{
    a *= 1000;
    a = floor(a + .5);
    return a/1000;
}

int CountCenters(double Length, int MinLevel, int MaxLevel)
{
    int I = MinLevel;
    int Count = 0;
    if(Length < SQRT3 + Tolerance && Length > SQRT3 - Tolerance)return 6;
    if(Length < 3)return 0;

    while(I <= MaxLevel)
    {
        bool Even = true;
        if(I % 2 == 0)Even = false;
        double d = 0;
        double pd = 0;
        for(int i = 0; i < int(I/2 + 1); i++)
        {
            Point test = Point(i, I - i);
            double a, b;
            a = test.GetHex_x();
            b = test.GetHex_y();

            d = Round(DistanceFormulaC(a, b));
            if(d < Length)break;

            if(d < Length + Tolerance && d > Length - Tolerance)
            {
                if(Even)Count += 12;
                if(!Even)Count += 6; //Actually even
                break;
            }
        }
        I++;
    }
    return Count;
}

int sround(double a)
{
    return int(a + .5);
}

int PointsToBeTested(int min, int max){
    int total = 0;
    while(min <= max){
        total += min - 1;
        min += 1;
    }
    return sround(total / 2) + 1;
}

int main()
{
    cout << "Hexagon Utility by Mark McCulloh\n";
    cout << "Enter 0 to see the help menu, or just enter an L for B(L)\n";
    while(true)
    {
        double input = GetInput();
        cout << "\n--------------------------------\n";
        cout << "Length: " << Round(input) << "\n";
        cout << "Minimum hexagon level: " << sround(input / SQRT3) << "\n";
        cout << "Maximum hexagon level: " << sround(input / 1.5)   << "\n";
        if(PointsToBeTested(sround(input / SQRT3), sround(input / 1.5)) < 0)
            cout << "Max points to be tested: Have Fun Waiting (Over 2 billion)\n";
        else
            cout << "Max points to be tested: " << PointsToBeTested(sround(input / SQRT3), sround(input / 1.5)) << "\n";
        cout << "Tolerance: " << Tolerance << "\n\n";

        int Centers = CountCenters(Round(input), sround(input / SQRT3), sround(input / 1.5));

        cout << "Number of Centers: " << Centers << "\n--------------------------------\n";
    }
    return 0;
}
