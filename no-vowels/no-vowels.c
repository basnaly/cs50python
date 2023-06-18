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
        printf("Error"\n);
        return 1;
    }
    else
    {
        string word = argv[1];
        string replaced = replace(word);
        printf(replaced\n);
    }
}

string replace(string word)
{
    
}
