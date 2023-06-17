// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string letter);

int main(int argc, string argv[])
{
    string word = argv[1];
    if (argc == 0 || argc > 1)
    {
        printf("Error");
        return 1;
    }
    else
    {
        printf("%s\n", argv[1]);
        return 0;
    }
    string replaced = replace(word);
    printf("%s\n", replaced);
}

string replace(string word)
{
    int length = strlen(word);
    for (int i = 0; i < length; i++)

    switch(word[i])
    {
        case 'a':
            word[i] = '6';
            break;

        case 'e':
            printf("3");
            break;

        case 'i':
            printf("1");
            break;

        case 'o':
            printf("0");
            break;

        default:
            printf("%c", word[i]);
            break;
    }
    return word;
}
