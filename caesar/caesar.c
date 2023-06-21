#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argument);

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    if (only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    int atoi()
    string plain_text = get_string("plaintext: ");

}

bool only_digits(string argument)
{
    int length = strlen(argument);
    for (int i = 0; i < length; i++)
    {
        if (isdigit(argument[i]) == 0)
        {
            return false;
        }
    }
    return true;
}