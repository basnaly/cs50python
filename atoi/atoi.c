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

    long number = 0;

    int length = strlen(input);

    // Base case
    if (length == 0) return 0;

    // Define last char of the string and transform it to integer
    char last_char = input[length - 1];
    int last_int = last_char - '0';

    // remove last char from string
    input[length - 1] = '\0';

    // 
    number = convert(input) * 10 + last_int;

    return number;
}