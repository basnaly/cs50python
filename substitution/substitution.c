#include <cs50.h>
#include <stdio.h>

bool is_alphabetic(string argument);

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./substitution key\n");
        return 1;
    }

// printf("Key must contain 26 characters.\n");
}

bool is_alphabetic(string argument)
{
    int length = strlen(argument);
    for (let i = 0; i < length; i++)
    {
        if (isalpha(argument[i]) == 0)
        {

            return 1;
        }
    }
}