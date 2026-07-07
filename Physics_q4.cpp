#include <iostream>
using namespace std;


/*

A stone is dropped from the top of a tall building. It starts falling from rest, and gravity accelerates it downward at 9.8 m/s². Your task is to write a C++ program that asks the user for the time (in seconds) for which the stone has been falling. The program should calculate how far the stone has fallen and what its final velocity is after that time. Display both values rounded to two decimal places. Assume there is no air resistance and that the stone has not yet reached the ground.

*/


double distance(double t){

    double gravity = 9.8;
    double u = 0;

    double distance = u * t + (gravity * t * t) /2;


    return distance;


}

double velocity(double t){
    double gravity = 9.8;
    double u = 0;

    double velocity = u + gravity * t;

    return velocity;

}


int main(){
    double a = distance(5);
    double b = velocity(5);
    cout << "Distance: " << a << "m" << endl;
    cout << "Velocity: " << b << "m/s" << endl;
    return 0;
}
