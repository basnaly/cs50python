#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool only_digits(string sla);

char rotate(char letter, int key);

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

    string plain_text = get_string("plaintext: "); // 10milk
    int length = strlen(plain_text);

    string ciphertext = "";

    for(int i = 0; i < length; i++)
    {
        if (!isalpha(plain_text[i]))
        {
             ciphertext = ciphertext + plain_text[i];
        }
        else
        {
            ciphertext = ciphertext + rotate(plain_text[i], k);

            prinf("%")
        }
    }

    string cipher_text = get_string("ciphertext: ");
    printf("%s\n", )

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

char rotate(char letter, int key)
{
    if (isupper(letter))
    {
        char rotated_letter = (char) ((int) letter + key - 65) % 26;
    }
    else if (islower(letter))
    {
        char rotated_letter = (char) ((int) letter + key - 97) % 26;
    }

    return rotated_letter;
}