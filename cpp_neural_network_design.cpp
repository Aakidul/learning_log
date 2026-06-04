#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

// SIGMOID FUCNTION
double sigmoid(double x){
    return 1.0 / (1.0 + exp(-x));
}


//CLASS FOR NEURON
class Neuron{
    public:
    vector<double> weights;
    double bias;


//THIS IS THE CONSTRUCTOR FOR NEURON CLASS
    Neuron(vector<double> w, double b){
    weights = w;
    bias = b;

}



//ACTIVATION FUNCTION AKA
   double activation(vector<double> input){
    double sum = 0.0;
    for (int i = 0; i < input.size(); i++){
          sum += input[i] * weights[i];
}
    sum += bias;
    return  sigmoid(sum);

}

};


//MAIN INT FUNCTION FOR CALLING..
int main(){
    Neuron n({1.0, 3.0}, 0.1);
    vector<double> input = {3.0, 1.0};
    cout << n.activation(input) << endl;
    return 0;

}
