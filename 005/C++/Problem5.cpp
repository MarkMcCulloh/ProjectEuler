#include <iostream>

using namespace std;

int main()
{
    //Problem 5
    int End = 0;
    long int Result = 0;
    bool Check = false;
    cout << "Number divisible by all the numbers between (and including) 1 and ";
    cin >> End;
    while(true)
    {
        Result++;
        Check = false;
        for(int i = 1; i < End; i++)
        {
            if(Result % i != 0)
            {
                Check = false;
                break;
            }
            else
            {
                Check = true;
            }
        }
        if(Check == true)break;
    }
    cout << "\nThe answer is " << Result;
}
