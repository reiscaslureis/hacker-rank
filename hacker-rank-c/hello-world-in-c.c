#include <stdio.h>

int main() {
    char x[30];

    gets(x);

    printf("Hello, World!\n");
    printf("%s", x);

    return 0;
}
