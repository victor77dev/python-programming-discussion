#include <iostream>

using namespace std;

void fooBar(int num);

int main() {    
    fooBar(15);
    fooBar(42);
    fooBar(100);
}

void fooBar(int num) {
    cout << "Foo Bar Game of " << num << endl;
    for (int i = 1; i <= num; i++) {
        if (i % 3 == 0) cout << "Foo";
        if (i % 5 == 0) cout << "Bar";
        if (i % 3 != 0 && i % 5 != 0) cout << i;
        cout << endl;
    }
}