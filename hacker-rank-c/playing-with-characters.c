#include <stdio.h>

int main() {
    char ch, s[10], sen[20];

    scanf("%c\n", &ch);
    scanf("%s\n", &s);
    gets(sen);

    printf("%c\n%s\n%s", ch, s, sen);

    return 0;
}