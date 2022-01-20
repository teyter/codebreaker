#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int power(int base, unsigned int exp) {
    int i, result = 1;
    for (i = 0; i < exp; i++)
        result *= base;
    return result;
 }

void bruteforce(int k, const char* a) {
    int base = strlen(a);
    int sic = power(base,k);
    for (int i = 0; i < sic; i++) {
        int exp = k-1;
        for (int j = 0; j < k; j++) {
            int bit = (int)(i/power(base,exp)) % base;
            printf("%c", a[bit]);
            exp--;
        }
        printf("\n");
    }
}

int main() {
    int k = 5;
    //char* a = "ACGT";
    char* a = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    bruteforce(k,a);
}
