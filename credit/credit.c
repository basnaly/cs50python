#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

long get_number(void);
int calculate_sum(long number);
bool is_valid(int sum);
bool is_amex(false);

int main(void)
{
    // Ask for a credit card number
    long number = get_number();

    // Calculate sum of credit card digts
    int sum = calculate_sum(number);
}

long get_number(void)
{
    long number;
    do
    {
        number = get_long("Number: ");
    }
    while (number < 0);
    return number;
}

int calculate_sum(long number)
{
    int sum_even;
    int sum_odd;
    for (int i = 0; number <= 0; i++)
    {
        if (i % 2 == 0)
        {
            sum_even = sum_even + i;
        }
        else
        {
            int double = i * 2;
            if (double > 9)
            {
                double = 1 + (double - 10);
            }
            sum_odd = sum_odd + double;
        }
    }
    return sum_even + sum_odd;
}

bool is_valid(int sum)
{
    if (sum % 10 === 0)
    {
        return true;
    }
    return false;
}

bool is_amex(long number)
{
    
}