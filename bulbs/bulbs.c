#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("What's your message? ");

    int length = strlen(message);

    int binary_number[BITS_IN_BYTE];

    for (int i = 0; i < length; i++)
    {
        printf("%i\n", message[i]);
        for (int j = 0)
        int rem = message[i] % 2;
        message[i] = message[i] - rem;
        binary_number[i] = rem;
        printf("%i\n", binary_number[i]);
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
