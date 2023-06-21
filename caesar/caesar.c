#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string argument);

char rotate(char letter, int key);

int main(int argc, string argv[])
{
    // If no agruments or there are more than 2
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./caesar key\n");
        return 1;
    }

    // If arguments not digits
    if (only_digits(argv[1]) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    // Transform the key fron string to integer
    int key = atoi(argv[1]);

    // Ask fot user type text
    string plain_text = get_string("plaintext: ");
    int length = strlen(plain_text);

    // Create new variable with the same length
    string cipher_text = plain_text;

    for (int i = 0; i < length; i++)
    {
        // Change each letter of the text in for loop;
        cipher_text[i] = rotate(cipher_text[i], key);
    }
    printf("ciphertext: %s\n", cipher_text);
    return 0;
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

char rotate(char letter, int key)
{
    char cipher_letter = letter;
    if (isupper(cipher_letter) != 0)
    {
        // If the letter has uppercase rotate it according ASCII on key positions
        cipher_letter = ((int)((cipher_letter) - 65 + key) % 26) + 65;
    }

    else if (islower(cipher_letter) != 0)
    {
        // If the letter has lowercase rotate it according ASCII on key positions
        cipher_letter = ((int)((cipher_letter) - 97 + key) % 26) + 97;
    }
    return cipher_letter;
}
