#include <iostream>
#include <cmath>
using namespace std;


double sigmoid(double x){
    return 1.0 / (1.0 + exp(-x));

}


class Neuron{
public:
    double w1 = 0.5;
    double w2 = 0.2;
    double bias = 0.1;



    double forward(double x1, double x2){
        double sum = x1 * w1 + x2 * w2 + bias;
        return sigmoid(sum);


}




};



int main(){
    Neuron n1;
    n1.w1 = 0.6;
    double output = n1.forward(1.0, 3.0);
    cout << output << endl;
    return 0;
}
