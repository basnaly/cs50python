#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Calculate sum of the credit card number digits
    int calcilate_sum = calc_sum(long number);

}

long get_number(void)
{
    long number;

    do
    {
        number = get_long("Enter your credit card number: ");
    }
    while (size < 0);
    return number;
}

int calcilate_sum(long number)
{
    int sum;
    for (int i = 0; i < number.length; i++)
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        if (i % 2 == 0)
        {
            sum = sum + rem;
        }
        else
        {
            sum = sum + rem * 2;
            if (sum > 9)
            {
                for (int j = 0; j < sum.length; i++)
                {
                    int rem1 = sum % 10;
                    int sum1 = (sum - rem1) / 10;
                    sum1 = sum1 + rem1
                }
            }
        }
    }
}