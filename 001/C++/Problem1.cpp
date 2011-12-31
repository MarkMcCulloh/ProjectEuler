#include <iostream>

using namespace std;

int main()
{
    //Problem 1
    int End = 0;
    int Result = 0;
    cout << "The sum of all the multiples of 3 or 5 below ";
    cin >> End;
    for(int i = 0; i < End; i++)
        if(i % 3 == 0 || i % 5 == 0)Result += i;
    cout << Result;
}
