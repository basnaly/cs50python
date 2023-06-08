#include <cs50.h>
#include <stdio.h>

long get_number();
int calc_sum(long number);

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Calculate sum of the credit card number digits
    int calcilate_sum = calc_sum(number);

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
    int sum;
    for (int i = 0; number>= 10; i++)
    {
        int rem = number % 10;
        number = (number - rem) / 10;
        if (i % 2 == 0)
        {
            sum = sum + rem;
        }
        else
        {
            sum = sum + rem * 2; // 14
            if (sum > 9)
            {
                int sum1 = sum; //14
                for (int j = 0; sum1 >= 10; j++)
                {
                    int rem1 = sum % 10; //4
                    sum1 = (sum - rem1) / 10; //1
                    sum = sum1 + rem1; // 5
                }
            }
        }
    }
    return sum;
}