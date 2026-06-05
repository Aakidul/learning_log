#include <iostream>                         using namespace std;
                                            
int ask_user_for_age(){
    cout << "Enter Age: " << endl;
    int age;
    cin >> age;
    return age;

}
                                            
int main(){
    int age = ask_user_for_age();
    cout << "Your age is: " << age << endl;
    if (age >= 18){
       cout << "And you are adult" << endl;
            }
    else if(age < 18){
        cout << "And you are minor";
               }
    else{
        cout << "Invalid Input";
}
}
