#include <iostream>
#include <vector>

using namespace std;

int main()
{
    //Problem 2
    vector<int> Fibonacci;
    Fibonacci.push_back(1);
    Fibonacci.push_back(2);
    for (int Current_F = 0;Current_F < 4000000;){
    Current_F = Fibonacci[Fibonacci.size() - 1] + Fibonacci[Fibonacci.size() - 2];
    if(Current_F > 4000000)break;
    Fibonacci.push_back(Current_F);
    }

    int EvenSum = 0;

    for (int i=0; i<Fibonacci.size(); i++){
    if(Fibonacci[i] % 2 == 0)EvenSum += Fibonacci[i];
    cout << Fibonacci[i] << endl;
    }

    cout << "\n" << EvenSum;
}
