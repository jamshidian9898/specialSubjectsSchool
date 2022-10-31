#include <iostream>
#include <math.h>
#include <string>

using namespace std;

int main()
{
    
    int numbers[10];
    int sum = 0;
    int length  = sizeof(numbers)/sizeof(numbers[0]);
    
    string numberStr;
    
    for(int i = 0; i < length; i++){
            cin >> numbers[i];
            if(numbers[i] != 0 && numbers[i] != 1){
                cout << "please only insert binary number.";
                return 0;
            }
    }  
    numberStr = "(";
    for (int j = 1; j <= length;j++){
        sum += numbers[j-1] * pow(2 , (length - j));
        numberStr +=  to_string(numbers[j-1]);
    }
    numberStr += ")";
    cout << " base conversion " << numberStr << ": " << sum;
    return 0;
}
