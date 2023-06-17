// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>

string replace(string letter)

int main(int argc, string argv[])
{
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
}

string replace(string letter)
{
    string letter;
    switch(letter)
    {
        case "a":
            printf(6);
            break;

        case "e":
            printf(3);
            break;

        case "i":
            printf(1);
            break;

        case "o":
            printf(0);
            break;

        default:
            printf();
            break;
    }
}
