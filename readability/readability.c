#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int count_letters(string text);

int main(void)
{
    string text = get_string("Text: ");

    count_letters(text);
    
    printf("%s\n", text);
}

int count_letters(string text)
{
    int total_letters = 0;
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        if (isalpha(text[i]))
        {
            total_letters = total_letters + 1;
        }
    }
    return total_letters;
}