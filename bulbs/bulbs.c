#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string message = get_string("What's your nessage: ");
    int length = strlen(message);

    int binary_number[BITS_IN_BYTE];
    int rem;

    for (int i = 0; i < length; i++)
    {
        // printf("%i\n", message[i]);

        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            rem = message[i] % 2;
            message[i] = (message[i] - rem) / 2;
            binary_number[j] = rem;
            printf("%i", binary_number[j]);
        }
        printf("\n");

        for (int k = 0; k < BITS_IN_BYTE - k - 1; k++)
        {
            printf("%i", rem);
        }
        printf("\n");

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
