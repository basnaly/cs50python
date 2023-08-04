// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 'Z' - 'A' + ('Z' - 'A') * 26 + ('Z' - 'A') * 52 + 1;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word to obtain a hash value
    unsigned int index = hash(word);

    // Access linked list at that index in the hash table;
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
        {
            // Return true if the word is in the dictionary, false otherwise
            if (strcasecmp(cursor->word, *word) == 0)
            return true;
        }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function

    int length = strlen(word);

    int sum = 0;

    if (length >= 1 && isalpha(word[0]))
    {
        sum += toupper(word[0]) - 'A';
    }
    if (length >= 2 && isalpha(word[1]))
    {
        sum += (toupper(word[0]) - 'A') * 26;
    }
    if (length >= 3 && isalpha(word[1]))
    {
        sum += (toupper(word[0]) - 'A') * 52;
    }
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary file
        // Use fopen
        FILE *dict_file = fopen(dictionary, "r");

        // Remember to check if return value is null
        if (dict_file == NULL)
        {
            return NULL;
        }

    // Read string from file one at a time

        char dict_word[LENGTH + 1];

        // fscanf(file, "%s", word)
        while(fscanf(dict_file, "%s", dict_word) == 1)
        {

            // Create a new node for each word
                // use malloc
            node *new_node = malloc(sizeof(node))

                // remember to check if return value is NULL
            if (new_node = NULL)
            {
                return NULL;
            }
                // Copy word into node using strcpy
            strcpy(new_node->word, dict_word);
            new_node->next = NULL;

            // Hash word to obtain a hash value
                // Use the hash function
                // function takes a string and return the index
            unsigned int index = hash(new_node->word);

            // Insert node into hash table at that location
                // Recall that hash table is an array of linked lists
                // Be shure to set pointers in the correct order
                if (table[index] == NULL)
                {
                    table[index] = new_node;
                }
                else
                {
                    new_node->next = table[index]
                    table[index] = new_node;
                }
        }

        // fscan will return EOF once it reaches end of file
        if (feof(dict_file))
        {
            fclose(dict_file);
            return true;
        }

    return false;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO

    int total_words = 0;

    for (int index = 0; index < N; index++)
    {
        for (node *ptr = table[index]; ptr != NULL; ptr = ptr->next)
        {
            total_words += 1;
        }
    }
    return total_words;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (node *cursor = table[index]; cursor != NULL; cursor = cursor->next)
        {
            temp = 
            // Return true if the word is in the dictionary, false otherwise
            if (strcasecmp(cursor->word, *word) == 0)
            return true;
        }
    return false;
}
