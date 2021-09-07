#include <stdio.h>

int main() {
    int tam, sum;

    scanf("%d", &tam);

    int array[tam];

    for (int i = 0; i < tam; i++) {
        scanf("%d", &array[i]);
    }

    sum = 0;

    for (int i = 0; i < tam; i++) {
        sum = sum + array[i];
    }

    printf("%d", sum);

    return 0;
}