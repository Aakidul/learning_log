#include <iostream>
using namespace std;

// using the namespace, for value of pi
namespace pi{
    const double pi_val = 3.14159;
}


// area of circle is pi*r^2

int get_radius(){
    int r;
    cout << "Enter radius: ";
    cin >> r;
    return r;
}


int main(){
    using namespace pi;
    int r = get_radius();
    double area = pi_val * (r * r);
    cout << area << endl;

    return 0;
}
