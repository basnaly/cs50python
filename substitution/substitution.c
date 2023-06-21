#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool is_alphabetic(string argument);
bool is_valid_key(string argument);

int main(int argc, string argv[])
{
    if ((argc == 1 || argc > 2) || (is_alphabetic(argv[1]) == false))
    {
        printf("Usage:  ./substitution key\n");
        return 1;
    }
    else if (is_valid_key(argv[1]) == false)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }


    return 0;
}

bool is_alphabetic(string argument)
{
    int length = strlen(argument);
    for (int i = 0; i < length; i++)
    {
        if (isalpha(argument[i]) == 0)
        {
            return false;
        }
    }
    return true;
}

bool is_valid_key(string argument)
{
    int length = strlen(argument);
    for (int i = 0; i < length; i++)
    {
        char letter = argument[i];
        for (int j = j + 1; j < length; j++)
        {
            if (letter[i] == argument[j])
            {
                return false;
            }
        }
    }
    return true;
}