#include <stdio.h>

int main() {
    int n, nsum;

    scanf("%d", &n);

    nsum = (n / 10000) + (n % 10000 / 1000) + (n % 1000 / 100) + (n % 100 / 10) + (n % 10 / 1);

    printf("%d", nsum);

    return 0;
}
