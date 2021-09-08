#include <iostream>

using namespace std;

void update(int *a,int *b) {
    int aux = *a;
    *a = *a + *b;
    *b = abs(aux - *b);
}

int main() {
    int a, b;
    int *aP = &a, *bP = &b;
    
    cin >> a;
    cin >> b;

    update(aP, bP);

    cout << *aP << endl;
    cout << *bP << endl;

    return 0;
}