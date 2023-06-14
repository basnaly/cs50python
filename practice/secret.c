#include <cs50.h>
#include <stdio.h>
#include <strcmp.h>

bool check_phrase(string);

int main(void)
{
    string phrase = get_string("What's the secret phrase? ");

    bool correct = check_phrase(phrase);

    if (correct == true)
    {
        printf("Come on in!\n");
    }
}

bool check_phrase(string phrase)
{
    string pasword = "Please";
    if (strcmp(phrase, password) == 0)
    {
        return true;
    }
    return false;
}