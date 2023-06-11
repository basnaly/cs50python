#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

long get_number(void);
int calc_sum(long number);
bool is_valid(int sum);
string check_type();

int main(void)
{
    // Ask for a credit card number
    long number = get_number();

    // Calc the sum of the credit card number's digits
    int sum = calc_sum(number);

    // Check if the credit card number is valid
    bool is_valid(sum);

    // Check the type of the credit card
    string type = check_type()

}

long get number()
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
    for (int i = 0; i < number; i++)
    {
        rem = number % 10;
        number = (number - rem) / 10;
        if (i % 2 == 0)
        {
            sum = sum + rem;
        }
        else
        {
            doubled = rem * 2;
            if (doubled > 9)
            {
                doubled = 1 + (doubled - 10);
            }
            sum = sum + doubled;
        }
    }
    return sum;
}

bool is_valid(sum)
{
    if (sum % 10 == 0)
    {
        return true;
    }
    return false;
}