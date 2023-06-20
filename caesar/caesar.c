#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string sla);

char rotate(char word, int key);

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
    int length = strlen(plain_text);

    for(int i = 0; i < length; i++)
    {
        if (!isalpha(plain_text[i]))
        {
            return plain_text[i];
        }
        else if (isupper(plain_text[i]) || islower(plain_text[i]))
        {
            rotate(plain_text[i], k);

            prinf("%")
        }
    }



    return 0;
}

bool only_digits(string sla)
{
    int length = strlen(sla);

    for (int i = 0; i < length; i++)
    {
        if (!isdigit(sla[i]))
        {
            return false;
        }
    }
    return true;
}

char rotate(char word, int key)
{
    word = ((int) word + key) % 26;
}