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
        string output = "";
        if (i % 3 == 0) output += "Foo";
        if (i % 5 == 0) output += "Bar";
        if (i % 3 != 0 && i % 5 != 0) output += to_string(i);
        cout << output << endl;
    }
}