#include <iostream>

using namespace std;

void fooBarV2(int num);

int main() {    
    fooBarV2(15);
    fooBarV2(42);
    fooBarV2(100);
}

void fooBarV2(int num) {
    cout << "Foo Bar Game of " << num << endl;
    for (int i = 1; i <= num; i++) {
        if (i % 3 == 0) cout << "Foo";
        if (i % 5 == 0) cout << "Bar";
        if (i % 3 != 0 && i % 5 != 0) cout << i;
        cout << endl;
    }
}
