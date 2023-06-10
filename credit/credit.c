#include <cs50.h>
#include <stdio.h>

long get_number();
int calc_sum(number);
string check_type(number);

int main(void)
{
    // Get a credit card number
    long number = get_number();

    // Calculate sum of credit card numver digits
    int sum = calc_sum(number);

    // Check type card
    string = check_type(number);
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

int calc_sum(long number)
{
    int sum = 0;
    for (int i = 0; number <= 0; i++)
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        if (i % 2 == 0)
        {
            sum = sum + rem;
        }
        else
        {
            int doubled = rem * 2;
            if (doubled > 9)
            {
                doubled = 1 + (doubled - 10);
            }
            sum = sum + doubled;
        }
    }
    return sum;
}

string check_type(number)
{
    
}