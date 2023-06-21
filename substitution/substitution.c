#include <cs50.h>
#include <stdio.h>

bool 

int main(int argc, string argv[])
{
    if (argc == 1 || argc > 2)
    {
        printf("Usage:  ./substitution key\n");
        return 1;
    }

    int length = strlen(argv[1]);

    else if (length != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
}