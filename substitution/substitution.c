#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool is_alphabetic(string argument);
bool is_length_key_valid(string argument);
bool is_valid_key(string argument);

int change(char plaintext);

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./substitution key\n");
        return 1;
    }
    else if ((is_alphabetic(argv[1]) == false))
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }
    else if ((is_length_key_valid(argv[1]) == false))
    {
        printf("Key must only contain 26 characters.\n");
        return 1;
    }

    else if (is_valid_key(argv[1]) == false)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    string key = argv[1];
    int key_length = strlen(key);
    for (int i = 0; i < key_length; i++)
    {
        key[i] = tolower(key[i]);
    }
    printf("key: %s\n", key);

    string plain_text = get_string("plaintext: ");
    int text_length = strlen(plain_text);

    string cipher_text = plain_text;

    for (int i = 0; i < text_length; i++)
    {
        if (isalpha(plain_text[i]))
        {
            int is_letter_uppercase = isupper(plain_text[i]);

            cipher_text[i] = key[change(plain_text[i])];

            if (isupper(plain_text[i]))
            {
                cipher_text[i] = cipher_text[i] + 32;
            }
            // else if (islower(plain_text[i]))
            // {
            //     cipher_text[i] = cipher_text[i] - 32;
            // }
        }
    }
    printf("ciphertext: %s\n", cipher_text);

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

bool is_length_key_valid(string argument)
{
    int length = strlen(argument);

    if (length != 26)
    {
        return false;
    }
    return true;
}

bool is_valid_key(string argument)
{
    int length = strlen(argument);

    for (int i = 0; i < length; i++)
    {
        char letter = argument[i];
        for (int j = i + 1; j < length; j++)
        {
            if (letter == argument[j])
            {
                return false;
            }
        }
    }
    return true;
}

int change(char letter)
{
    char cipher_letter = letter;

    if (isupper(letter) != 0)
    {
        cipher_letter = (int)(cipher_letter - 65);
    }
    else if (islower(letter) != 0)
    {
        cipher_letter = (int)(cipher_letter - 97);
    }
    return cipher_letter;
}