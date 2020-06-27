#include <iostream>

using namespace std;

void fooBarV1(int num);

int main() {    
    fooBarV1(15);
    fooBarV1(42);
    fooBarV1(100);
}

void fooBarV1(int num) {
    cout << "Foo Bar Game of " << num << endl;
    for (int i = 1; i <= num; i++) {
        string output = "";
        if (i % 3 == 0) output += "Foo";
        if (i % 5 == 0) output += "Bar";
        if (i % 3 != 0 && i % 5 != 0) output += to_string(i);
        cout << output << endl;
    }
}