#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

// int convert_loop(string input);

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

    //printf("%i\n", convert_loop(input));
}

int convert(string input)
{
    // TODO

    long number = 0;
    int length = strlen(input);

    if (length == 0)
    {
        return 0;
    }

    // Get last char
    char last_char = input[length - 1];

    // Transform the last char to int
    int last_int = last_char - '0';

    // Remove the last char from the string;
    input[length - 1] = '\0';

    // Transform the string to int
    number = convert(input) * 10 + last_int;
    // number (1) = 0 * 10 + 1 => 1
    // number (12) = 1 * 10 + 2 => 12
    // number (123) = 12 * 10 + 3 => 123

    return number;
}

// int convert_loop(string input)
// {
//     long number = 0;
//     int i = 0;

//     while(input[i] && (input[i] >= '0' && input[i] <= '9'))
//     {
//         number = number * 10 + input[i] - '0';
//         i++;
//     }
//     return number;
// }