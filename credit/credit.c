#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Get a credit card number
    long number = get_number();

    // Calculate sum of credit card numver digits
    int sum = calc_sum();
}

long get_number()
{
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);
    return number;
}

int sum = calc_sum(long number)
{
    
}