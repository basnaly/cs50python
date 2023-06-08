#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask credit card number
    long number = get_number();

    // Check if a credit card number is (syntactically) valid
    bool ifValid = 

}

int get_number(void)
{
    long number;

    do
    {
        number = get_long("Enter your credit card number: ");
    }
    while (size < 0);
}