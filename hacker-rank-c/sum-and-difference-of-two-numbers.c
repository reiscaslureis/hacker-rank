#include <stdio.h>

int main() {
    int ix, iy, isum, idff;
    float fx, fy, fsum,fdiff;

    scanf("%d %d %f %f", &ix, &iy, &fx, &fy);

    isum = ix + iy;
    idff = ix - iy;

    fsum = fx + fy;
    fdiff = fx - fy;

    printf("%d %d\n", isum, idff);
    printf("%.1f %.1f", fsum, fdiff);

    return 0;
}