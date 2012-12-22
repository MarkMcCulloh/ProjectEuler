#include <iostream>
#include <math.h>

using namespace std;

#define SQRT3 1.732050808
#define HSQRT3 0.8660254038

double Round(double a)
{
    a *= 1000;
    a = floor(a + .5);
    return a/1000;
}

double Hex_x(double x)
{
    return(x * 1.5);
}

double Hex_y(double x, double y)
{
    return( (y*SQRT3) + (x*HSQRT3) );
}

double DistanceFormulaC(double x, double y)
{
    return( sqrt((x*x) + (y*y)) );
}

void PrintHelp()
{
    cout << "Hexagon Fun-Time Utility\n";
    cout << "Enter a length (L) to gain the following info:\n";
    cout << "   1. Minimum hexagon level (L / SQRT(3))\n";
    cout << "   2. Maximum hexagon level (L / 1.5)\n";
    cout << "   3. Number of points to be tested\n";
    cout << "L should be a number > 0 that is rounded to 3 decimal places (if needed)\n";
    cout << "Entering any letters will cause a seizure because I am lazy\n";
    cout << "Change the tolerance of the calculations by entering a negative number (default is .000001)\n";
    cout << "     For example: -.00001 changes the tolerance to .00001\n";
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
        if(in < 0)
        {
            Tolerance = in * -1;
            cout << "Tolerance set to " << Tolerance << ".\n";
            continue;
        }
    }
    return in;
}

double PointsToBeTested(int min, int max)
{
    double total = 0;
    while(min <= max)
    {
        total += min;
        min += 1;
    }
    return total;
}

int CountCenters(double Length, int MinLevel, int MaxLevel)
{
    int I = MinLevel;
    int Count = 0;

    while(I <= MaxLevel)
    {
        bool Even = true;
        if(I % 2 == 0)Even = false;
        for(int i = 0; i < int(I/2 + 1); i++)
        {
            a = GetHex_x(i);
            b = GetHex_y(i, I - i);

            double d = Round(DistanceFormulaC(a, b));

            if(d == Length)
            {
                if(Even)Count += 12;
                if(!Even)Count += 6;
                break;
            }
        }
        I++;
    }
    return Count;
}

int main()
{
    cout << "Enter 0 to see the help menu, or just enter a length.\n";
    while(true)
    {
        double input = GetInput();

        int min = int((input / SQRT3) + .5);
        int max = int((input / 1.5) + .5);

        cout << "\n--------------------------------\n";
        cout << "Length: " << Round(input) << "\n";
        cout << "Minimum hexagon level: " << min << "\n";
        cout << "Maximum hexagon level: " << max << "\n";
        cout << "Number of points to be tested: " << PointsToBeTested(min, max) << "\n";

        int Centers = CountCenters(Round(input), min, max);

        cout << "Number of Centers: " << Centers << "\n--------------------------------\n";
    }
    return 0;
}
