#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // TODO
    int length = strlen(input);
    char letter[length];
    
    long num = 0;
    int i = 0;

    while (letter[i] && (letter[i] >= '0' || letter[i] <= '9'))
    {
        num = num * 10 + (letter[i] - '0');
    }
    return num;
}