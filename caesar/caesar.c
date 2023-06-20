#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);

char rotate(char letter, int key)

int main(int argc, string argv[])
{

    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    bool is_digit = only_digits(argv[1]);
    if (is_digit == false)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    int k = atoi(argv[1]);

    string plain_text = get_string("plaintext: ");


    return 0;


}

bool only_digits(string s)
{
    int length = strlen(s);

    for (int i = 0; i < length; i++)
    {
        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}