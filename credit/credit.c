#include <cs50.h>
#include <stdbool.h>
#include <stdio.h>

long get_number();
int calc_sum(long number);
bool is_valid(int sum);
bool is_american(long number);
bool is_master(long number);
bool is_visa(long number);
string card_type(long number, int sum);

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Calculate sum of the credit card number digits
    int calculate_sum = calc_sum(number);
    printf("Sum: %i\n", calculate_sum);
    printf("Your card is: %s\n", card_type(number, calculate_sum));
}

long get_number(void)
{
    long number;

    do
    {
        number = get_long("Enter your credit card number: ");
    }
    while (number < 0);
    return number;
}

int calc_sum(long number)
{
    int sum_odd = 0;
    int sum_even = 0;
    for (int i = 0; number > 0; i++)
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        if (i % 2 == 0)
        {
            sum_even = sum_even + rem;
        }
        else
        {
            int double_rem = rem * 2;
            if (double_rem > 9)
            {
                double_rem = 1 + double_rem - 10;
            }
            sum_odd = sum_odd + double_rem;
        }
    }
    return sum_even + sum_odd;
}

bool is_valid(calculate_sum)
{
    if (calculate_sum % 10 == 0)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool is_american(long number)
{
    int start1 = 34;
    int start2 = 37;
    int digits = 15;

    if ((number / 10 ^ (digits - 2)) == 34 || (number / 10 ^ (digits - 2)) == 37)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool is_master(long number)
{
    int start1 = 51;
    int start2 = 52;
    int start3 = 53;
    int start4 = 54;
    int start5 = 55;
    int digits = 16;

    if ((number / 10 ^ (digits - 2)) == 51 || (number / 10 ^ (digits - 2)) == 52 || (number / 10 ^ (digits - 2)) == 53 ||
        (number / 10 ^ (digits - 2)) == 54 || (number / 10 ^ (digits - 2)) == 55)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool is_visa(long number)
{
    int start = 4;
    int digits1 = 13;
    int digits2 = 16;

    for (int i = 0; i <= 16; i++) {
        int rem = number % 10;
        number = (number - rem) / 10;
        printf("Ren)
        if (rem == 4 && (i == digits1 || i == digits2))
        {
            return true;
        }
    }
    return false;

}

string card_type(long number, int sum)
{
    if (is_american(number) && is_valid(sum))
    {
        return "AMERICAN EXPRESS";
    }
    else if (is_master(number) && is_valid(sum))
    {
        return "MASTER CARD";
    }
    else if (is_visa(number) && is_valid(sum))
    {
        return "VISA";
    }
    else
    {
        return "INVALID";
    }
}