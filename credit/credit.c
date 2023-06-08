#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Ask credit card number
    int number = get_number();

    

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