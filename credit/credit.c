#include <cs50.h>
#include <stdio.h>

long get_number(void);
int calculate_sum(long number);

int main(void)
{
    // Ask credit card number
    long number = get_number();

    //
    int sum = calculate_sum(long number);

}