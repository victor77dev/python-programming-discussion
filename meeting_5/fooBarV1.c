#include <stdio.h>
#include <string.h>

void fooBarV1(int num);

int main() {    
    fooBarV1(15);
    fooBarV1(42);
    fooBarV1(100);
}

void fooBarV1(int num) {
    int i;
    printf("Foo Bar Game of %d\n", num);
    for (i = 1; i <= num; i++) {
        char output[1024] = "";
        if (i % 3 == 0) strcat(output, "Foo");
        if (i % 5 == 0) strcat(output, "Bar");
        if (i % 3 != 0 && i % 5 != 0) sprintf(output, "%d", i);
        printf("%s\n", output);
    }
}
