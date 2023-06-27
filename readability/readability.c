#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int count_letters(string text);

int count_words(string text);

int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // printf("%i letters\n", letters);
    // printf("%i words\n", words);
    // printf("%i sentences\n", sentences);

    // Calculate the average number of letters per 100 words in the text
    float L = (float)letters / (float)words * 100;

    // Calculate the average number of sentences per 100 words in the text.
    float S = (float)sentences / (float)words * 100;

    //  Calculate the index using the Coleman-Liau formula:
    int index = round((0.0588 * L) - (0.296 * S) - 15.8);

    if (index > 16)
    {
        printf("Grade 16+\n");
    }

    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else
    {
        printf("Grade %i\n", index);
    }
}

// Calculate letters by counting alphabetic characters in the text
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

// Calculate words by counting number of spaces in the text
int count_words(string text)
{
    int total_words = 1;
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        if (isspace(text[i]))
        {
            total_words = total_words + 1;
        }
    }
    return total_words;
}

// Calculate sentences by counting '.', '!' and '?' in the text
int count_sentences(string text)
{
    int total_sentences = 0;
    int length = strlen(text);

    for (int i = 0; i < length; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            total_sentences = total_sentences + 1;
        }
    }
    return total_sentences;
}