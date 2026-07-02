#include <iostream>
using namespace std;

// acceleration = (v - u) / t

int main() {

    double u;
    double v;
    double t;
    double a;

    cout << "ENTER INITIAL VELOCITY: ";
    cin >> u;

    cout << "ENTER FINAL VELOCITY: ";
    cin >> v;

    cout << "ENTER TIME TAKEN: ";
    cin >> t;

    a = (v - u) / t;

    cout << "Acceleration = " << a << " m/s^2" << endl;

    return 0;
}
