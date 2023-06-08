#include <cs50.h>
#include <stdio.h>

long get_number();
int calc_sum(long number);
bool is_valid();
bool american(long number);
bool master(long number);
bool visa(long number);
bool card_type(is_american(), is_master(), is_visa())

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Calculate sum of the credit card number digits
    int calcilate_sum = calc_sum(number);
    printf("Sum: %i\n", calcilate_sum);

    // Check if a credit card number is valid
    bool is_valid = calcilate_sum % 10 == 0;

    // Check if a credit card number is American express
    bool american = is_american();

    // Check if a credit card number is MasterCard
    bool master = is_master();

    // Check if a credit card number is Visa
    bool visa = is_visa();

    bool card_type = is_type(is_american(), is_master(), is_visa())

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

bool american(long number)
{
    int start1 = 34;
    int start2 = 37;
    int digits = 15;

    if ((number / 10 ^ (digits - 2)) == 34 || (number / 10 ^ (digits - 2)) == 37)
    {
        printf("AMERICAN EXPRESS ");
    }
    else
    {
        printf("false ");
    }
    return
}