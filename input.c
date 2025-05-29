#include <stdio.h>
int main() {
    int x = 10, y = 20;
    float z = 3.14e-2;
    char c = 'a';
    if (x != y) {
        z += x * y;
        printf("Hello\n");
    }
    // This is a comment
    /*
      Multi-line
      comment
    */
    return 0;
}
