#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;

int calcArea(int a, int b, int c, int n) {
    float area, p;

    p = (a + b + c) / 2.0;
    area = (p * (p - a) * (p - b) * (p - c));

    return area;
}

void sort_by_area(triangle *tr, int n) {
    for (int i = 0; i < n; i++) {
        for (int i = 0; i < n - 1; i++) {
            if (calcArea(tr[i].a, tr[i].b, tr[i].c, n) > calcArea(tr[i + 1].a, tr[i + 1].b, tr[i + 1].c, n)) {
                triangle aux;
                aux.a = tr[i].a;
                aux.b = tr[i].b;
                aux.c = tr[i].c;
                tr[i].a = tr[i + 1].a;
                tr[i].b = tr[i + 1].b;
                tr[i].c = tr[i + 1].c;
                tr[i + 1].a = aux.a;
                tr[i + 1].b = aux.b;
                tr[i + 1].c = aux.c;
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}