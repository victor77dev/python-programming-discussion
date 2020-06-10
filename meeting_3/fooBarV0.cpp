#include <iostream>

using namespace std;

void fooBarV0(int num);

int main() {    
    fooBarV0(15);
    fooBarV0(42);
    fooBarV0(100);
}

void fooBarV0(int num) {
    cout << "Foo Bar Game of " << num << endl;
    for (int i = 1; i <= num; i++) {
        if (i % 15 == 0) {
            cout << "FooBar" << endl;
        } else if (i % 3 == 0) {
            cout << "Foo" << endl;
        } else if (i % 5 == 0) {
            cout << "Bar" << endl;
        } else {
            cout << i << endl;
        }
    }
}
