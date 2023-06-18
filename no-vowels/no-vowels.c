// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string word);

int main(int argc, string argv[])
{
    if (argc < 0 || argc > 2)
    {
        printf("Error \n");
        return 1;
    }
    else
    {
        string word = argv[1];
        string replaced = replace(word);
        printf("%s\n", replaced);
    }
}

string replace(string word)
{
    int length = strlen(word);
    for (int i = 0; i < length; i++)
    {

        switch (i)
        {
            case 'a':
                printf("6");
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
                printf("i");
        }
        word[i];
    }
    return word;
}
