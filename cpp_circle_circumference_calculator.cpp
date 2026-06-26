// CALCULATING CIRCUMFERENCE
#include <iostream>
using namespace std;


int main(){
    const double PI = 3.14159;
    cout << "Enter Radius: ";
    double r;
    cin >> r;
    double circumference = 2 * PI * r;

    cout << "Circumference is: " << circumference << "cm" << endl;


    return 0;

}
