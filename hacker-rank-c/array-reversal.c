#include <stdio.h>

int main() {
    int tam;

    scanf("%d", &tam);

    int array[tam];

    for (int i = 0; i < tam; i++) {
        scanf("%d", &array[i]);
    }
    
    for (int i = tam - 1; i >= 0; i--) {
        printf("%d ", array[i]);
    }

    return 0;
}
