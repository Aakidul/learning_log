#include <iostream>

using namespace std;                                                                                                  int main(){
    cout << "Enter Day Number: " << endl;
    int day;
    cin >> day;


    //Checking your luck days.

    switch(day){
        case 1:
            cout << "Monday is lucky";                                 break;                                         
        case 2:
            cout << "Tuesday is Great";
            break;
                                                                   case 3:                                                        cout << "Wednesday is Bad";
            break;
                                                                   case 4:
            cout << "Thursday is Average";
            break;

        case 5:
            cout << "Friday is Lower average but not bad";
            break;

        case 6:
            cout << "Saturday is Sunny day";
            break;

        case 7:
            cout << "Sunday is Funday";
            break;

       default:
           cout << "Invalid";
           break;
}

    return 0;
}
