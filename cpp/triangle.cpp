#include <iostream>
#include <array>

using namespace std;

bool checkNumbers(int a,int b, int c){
    if (a == 0 || b == 0 || c == 0)
    {
        return false;
    }

    if (a + b <= c || b + c <= a || c + a <= b)
    {
        return false;
    }
    return true;
}

int main()
{
    float p, a = 0;
    int tri[3];

    cin >> tri[0];
    cin >> tri[1];
    cin >> tri[2];
    
    if(checkNumbers(tri[0] , tri[1] , tri[2])){
       cout << "tirangle area : " << (tri[0] * tri[1]) / 2 << "\n";
       cout << "tirangle Perimeter : " << (tri[0] + tri[0] + tri[0]) << "\n";
       return 0;
    }
    
    cout << "your triangle parameters in invalid";
    return 0;
}

