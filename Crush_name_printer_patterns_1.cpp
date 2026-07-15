#include <iostream>

using namespace std;

void loop(string name){
for (int y = 0; y < 7; y++){
            cout << name[y] << endl;
        }
}

int main(){
   for(int i = 0; i < 100; i++){
       string name = "Jessica";
       loop(name);
}

    return 0;
}
