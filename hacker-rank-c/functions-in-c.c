#include <stdio.h>

int greatest_func(int a, int b, int c, int d) {
    int greatest;

    greatest = a;

    if (greatest < b) {
        greatest = b;
    }
    
    if (greatest < c) {
        greatest = c;
    }

    if (greatest < d) {
        greatest = d;
    }

    return greatest;

}

int main() {
    int greatest, a, b, c, d;

    scanf("%d %d %d %d", &a, &b, &c, &d);

    greatest = greatest_func(a, b, c, d);

    printf("%d", greatest);

    return 0;
}
