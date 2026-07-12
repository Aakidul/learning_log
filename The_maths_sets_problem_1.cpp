#include <iostream>

using namespace std;


/*
This is question from sets chapter in mathematics


If n(A) = 15,
n(A union B) = 29,
n(A intersection B) = 7,
then n(B) = ?

*/


int problem(int a, int UnionAB, int IntersectionAB){

    // Using The Standard Formula
    // n(A union B) = n(A) + n(B) - n(A intersection B)
    // To find B


//    int UnionAB = (a + b) - IntersectionAB;

    int b = UnionAB - ( a - IntersectionAB);
    return b;


}


int main(){
    int a = problem(15, 29, 7);
    cout << "Ans: " << a << endl;
    return 0;
}
