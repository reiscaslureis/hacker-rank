#include <iostream>

using namespace std;

void print_reverse_vet(int n, int vet[]) {
    for (int i = n - 1; i >= 0; i--) {
        cout << vet[i] << ' ';
    }
}

int main() {
    int n;

    cin >> n;

    int vet[n];

    for (int i = 0; i < n; i++) {
        cin >> vet[i];
    }

    print_reverse_vet(n, vet);

    return 0;
}