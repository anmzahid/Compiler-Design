#include <stdio.h>    // Preprocessor directive, no semicolon needed

int main() {
    int x = 10, y = 20;;      // Extra semicolon, comma between vars
    float z = 3.14e-2         // Missing semicolon here
    char c = 'a';             // Correct line

    if ((x != y)) {           // Balanced parentheses
        z += x * y;;          // Extra semicolon here
        printf("Hello\n");    // Missing semicolon here
    }                        

    if (x > 5               // Missing closing parenthesis here
        && y < 15)) {        // Extra closing parenthesis here
        x = x + + y;         // Consecutive operators ++
        y 20;                // Missing operator between y and 20
    }

    return 0;
}


