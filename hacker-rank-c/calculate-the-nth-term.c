#include <stdio.h>

int main() {
    int n;

    scanf("%d", &n);

    int array[n];

    for (int i = 0; i <= 2; i++) {
        scanf("%d", &array[i]);
    }

    for (int i = 3; i < n; i++) {
        array[i] = array[i - 1] + array[i - 2] + array[i - 3];
    }
    
    printf("%d", array[n - 1]);

    return 0;
}