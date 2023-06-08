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
    int sum =
}