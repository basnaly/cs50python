#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);

int main(int argc, string argv[])
{

    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    string argument = argv[1];
    int length = strlen(argument);

    for (int i = 0; i < length; i++)
    {
        if (!isdigit(argument[i]))
        {
            printf("Usage:  ./caesar key\n");
            return 1;
        }
    }

    // int k;
    // k = atoi(argv[1]);
    string plain = get_string("Plaintext: ");

    only_digits(argv[1]);

        // return 0;
}

bool only_digits(string s)
{
    if (!isdigit(s))
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }
    else
    {
        return 0;
    }
}