#include <stdio.h>

void fooBarV0(int num);

int main() {    
    fooBarV0(15);
    fooBarV0(42);
    fooBarV0(100);
}

void fooBarV0(int num) {
    int i;
    printf("Foo Bar Game of %d\n", num);
    for (i = 1; i <= num; i++) {
        if (i % 15 == 0) {
            printf("FooBar\n");
        } else if (i % 3 == 0) {
            printf("Foo\n");
        } else if (i % 5 == 0) {
            printf("Bar\n");
        } else {
            printf("%d\n", i);
        }
    }
}

