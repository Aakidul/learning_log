#include <iostream>
#include <cmath>
using namespace std;


double sigmoid(double x){
    return 1.0 / (1.0 + exp(-x));

}



int main(){
    double a = sigmoid(5);
    cout << a << "\n";

}
