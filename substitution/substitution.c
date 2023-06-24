#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool is_alphabetic(string argument);
bool is_length_key_valid(string argument);
bool is_valid_key(string argument);

int change(char plaintext);

int main(int argc, string argv[])
{
    // Check a CLA
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./substitution key\n");
        return 1;
    }

    // Check if the CLA is alphabetic
    else if ((is_alphabetic(argv[1]) == false))
    {
        printf("Key must only contain alphabetic characters.\n");
        return 1;
    }

    // Check if the CLA' s length valid
    else if ((is_length_key_valid(argv[1]) == false))
    {
        printf("Key must only contain 26 characters.\n");
        return 1;
    }

    // Check if the CLA has only uniqe characters
    else if (is_valid_key(argv[1]) == false)
    {
        printf("Key must not contain repeated characters.\n");
        return 1;
    }

    // Transfer the key (CLA) to lowercase
    string key = argv[1];
    int key_length = strlen(key);
    for (int i = 0; i < key_length; i++)
    {
        key[i] = tolower(key[i]);
    }
    printf("key: %s\n", key);

    // Ask user to type text
    string plain_text = get_string("plaintext: ");
    int text_length = strlen(plain_text);

    for (int i = 0; i < text_length; i++)
    {
        int is
    }


    printf("ciphertext: %s\n", plain_text);

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

// Check if letter of plain_text uppercase or lowercase and return the changed
// letter in according case
int change(char letter)
{
    char cipher_index = letter;

    if (isupper(letter))
    {
        cipher_index = (int)(cipher_index - 65);
    }
    else if (islower(letter))
    {
        cipher_index = (int)(cipher_index - 97);
    }
    return cipher_index;
}