#include <cs50.h>
#include <stdio.h>

long get_number(void);
int calculate_sum(long number);

int main(void)
{
    // Ask for a credit card number
    long number = get_number();

    // Calculate sum of credit card digts
    int sum = calculate_sum(long number);

}

long get_number()
    long number;
    do
    {
        printf("Number: %li\n", number)
    }
    while (number < 0)
