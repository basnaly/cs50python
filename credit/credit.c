#include <cs50.h>
#include <stdio.h>
#include <stdbool.h>

long get_number(void);
int calc_sum(long number);
bool is_valid(int sum);
string check_type(long number);

int main(void)
{
    // Ask for a credit card number
    long number = get_number();

    // Calc the sum of the credit card number's digits
    int sum = calc_sum(number);

    // Check if the credit card number is valid
    bool is_valid(sum);

    // Check the type of the credit card
    string type = check_type(sum, number);
    printf("Sum: %i\n", sum);
    printf("%s\n", type);

}

long get number(void)
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
        int rem = number % 10;
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

string check_type(int sum, long number)
{
    int amex_digits = 15;
    int master_digits = 16;
    int visa_digits1 = 13;
    int visa_digits2 = 16;

    int amex_start1 = 34;
    int amex_start2 = 37;
    int master_start1 = 51;
    int master_start2 = 52;
    int master_start3 = 53;
    int master_start4 = 54;
    int master_start5 = 55;
    int visa_starts = 4;

    if (is_valid(sum) == false)
    {
        return "INVALID";
    }

    for (int i = 0; i < number; i++)
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        if ((rem == amex_start1 && i = (amex_digits - 1)) || (rem == amex_start2 && i = (amex_digits - 1)))
        {
            return "AMEX";
        }
        else if ((rem == master_start1 && i = (master_digits - 2)) || (rem == master_start2 && i = (master_digits - 2)) || (rem == master_start3 && i = (master_digits - 2)) || (rem == master_start4 && i = (master_digits - 2)) || (rem == master_start5 && i = (master_digits - 2)))
        {
            return "MASTERCARD";
        }
        else if ((rem == visa_start && i = (visa_digits1 - 1)) || (rem == visa_start && i = (visa_digits2 - 1)))
        {
            return "VISA";
        }
    }
    return "INVALID";
}
