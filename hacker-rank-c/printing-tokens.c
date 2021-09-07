#include <stdio.h>

int main() {
    char str[1000];
    
    gets(str);

    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == ' ') {
            printf("\n");
        } else {
            printf("%c", str[i]);
        }
    }

    return 0;
}
