#include <iostream>

using namespace std;

int main()
{
    //Problem 7 (104,743)
    cout << "Finding the 10,001st prime number....\n";
    int Primes(0), i;
    for(i = 2; Primes < 10001; i++)
    {
        bool Prime = true;
        if(i != 2 || i != 3 || i != 5 || i != 7)
            for(int a = 2; a < (i / 2) + 1; a++)
                if(i % a == 0)
                    {
                        Prime = false;
                        break;
                    }
        if(Prime)Primes++;
    }
    cout << "\nThe 10,001st prime number is " << i - 1 << ".\n";
}
