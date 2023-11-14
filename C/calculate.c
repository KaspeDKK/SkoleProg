#include <stdio.h>

int main() {
    float a, b, result;
    char operator;

    printf("Enter first number: ");
    scanf("%f", &a);

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);

    printf("Enter second number: ");
    scanf("%f", &b);
    
    switch (operator) {
    case '+':
        result = a + b;
        break;
    case '-':
        result = a - b;
        break;
    case '*':
        result = a * b;
        break;
    case '/':
        if(b != 0.0)
            result = a / b;
        else {
            printf("Error! Division by zero.\n");
            return 1;
        }
        break;
    default:
        printf("Error! Operator is not correct.\n");
        return 1;
    }

    printf("Result: %f %c %f = %f\n", a, operator, b, result);
    return 0;
}
