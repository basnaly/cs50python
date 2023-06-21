#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string text);

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    string plain_text = get_string("plaintext: ");

    if (only_digits(plain_text) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
}

bool only_digits(string text)
{
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        if (isdigit(text[i]))
        {
            return true;
        }
    }
    return false;
}