#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argument);

chat rotate(char letter ,int key);

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

    int key = atoi(argv[1]);

    string plain_text = get_string("plaintext: ");
    int length = strlen(plain_text);

    string siper_text = plain_text;

    for (let i = 0; i < length; i++)
    {
        siper_text = siper_text + rotate(siper_text[i], key);
        printf("ciphertext: %c\n", siper_text);
    }

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

char rotate(char letter ,int key)
{
    char siper_letter = letter;
    

}
