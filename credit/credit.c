#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

long get_number();
int calc_sum(long number);
bool is_valid();
bool is_american(long number);
bool is_master(long number);
bool is_visa(long number);
string card_type();

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Calculate sum of the credit card number digits
    int calculate_sum = calc_sum(number);
    printf("Sum: %i\n", calculate_sum);
    printf("Your card is: %s\n", card_type());

    // Check if a credit card number is valid
    bool is_valid = false;

    // Check if a credit card number is American express
    bool is_american = false;

    // Check if a credit card number is MasterCard
    bool is_master = false;

    // Check if a credit card number is Visa
    bool is_visa = false;

    bool card_type = false;
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
    int sum = 0;
    for (int i = 0; number > 0; i++)
    {
        int rem = number % 10; // 3, 2
        number = (number - rem) / 10; // 12, 1
        if (i % 2 == 0)
        {
            sum = sum + rem; // 3
        }
        else
        {
            sum = sum + rem * 2; // 14
            // if (sum > 9)
            // {
            //     int sum1 = sum; //14
            //     for (int j = 0; sum1 >= 10; j++)
            //     {
            //         int rem1 = sum1 % 10; //4
            //         sum1 = (sum - rem1) / 10; //1
            //         sum = sum + sum1 + rem1; // 5
            //     }
            // }
        }
    }
    return sum;
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

    if ((number / 10 ^ (digits - 2)) == 51 || (number / 10 ^ (digits - 2)) == 52 || (number / 10 ^ (digits - 2)) == 53 || (number / 10 ^ (digits - 2)) == 54 || (number / 10 ^ (digits - 2)) == 55)
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

    if ((number / 10 ^ (digits1 - 1)) == 44 || (number / 10 ^ (digits2 - 1)) == 4)
    {
        return true;
    }
    else
    {
        return false;
    }
}

string card_type()
{
    if (is_american(true) && is_valid(true))
    {
        return "AMERICAN EXPRESS";
    }
    else if (is_master(true) && is_valid(true))
    {
        return "MASTER CARD";
    }
    else if (is_visa(true) && is_valid(true))
    {
        return "VISA";
    }
    else
    {
        return "INVALID";
    }
}