void func(int *a, int *b) {
    int x = *a, y = *b;

    *a = x + y;
    *b = abs(x - y);
}
          
int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    func(&a, &b);
    
    printf("%d\n", a);
    printf("%d", b);
    return 0;      
} 
