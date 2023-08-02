// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = ('Z' - 'A') + ('Z' - 'A') * 26 + ('Z' - 'A') * 52 + 1;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash word to obtain a hash value

    // Access linked list at that index in the hash table

    // Traverse linked list, looking for the word using strcasecmp()

        // Start with cursor set to first item in linked list

        // Keep moving cursor until you get to NULL, checking each node for the word.

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';

    int sum = 0;

    int word_length = strlen(word);

    if (word_length >= 1)
    {
        sum = toupper(word[0]) - 'A';
    }
    if (word_length >= 2)
    {
        sum = sum + (toupper(word[1]) - 'A') * 26;
    }
    if (word_length >= 3)
    {
        sum = sum + (toupper(word[2]) - 'A') * 52;
    }
    printf("%i\n", sum);
    return sum;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO

    // Open dictionary file
    // use fopen to save the dictionary in memory
    FILE *dict_file = fopen(dictionary, "r");
    // remember to check if return value is NULL
    if (dict_file == NULL)
    {
        return NULL;
    }

    // Read strings from file one at a time
    // fscanf(file, "%s", word)
    char word[LENGTH + 1];

    while (fscanf(dict_file, "%s", word) == 1)
    {
        // Create a new node for each word
        // use malloc
        node *new_node = malloc(sizeof(node));

        // remember to check if return value is NULL
        if (new_node == NULL)
        {
            return NULL;
        }

        // copy word into node using strcpy
        strcpy(new_node->word, word);
        new_node->next = NULL;

        // Hash word to obtain a hash value
            // use the hash function
            // Function takes a string and returns an index
            unsigned int index = hash(word);

        // Insert node into hash table at that location
        if (table[index] == NULL)
        {
            table[index] = new_node;
        }
            // recall that hash table is an array of linked lists
        else
        {
            // Be sure to set pointers in the correct order
            // put new node in the start of linked list
            // node *linked_list = table[index];
            new_node->next = table[index];
            table[index] = new_node;


        }
    }

    // fscanf will return EOF once it reaches end of the file
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
        node *linked_list = table[index];

        for (node *ptr = linked_list; ptr != NULL; ptr = ptr->next)
            {
                total_words += 1;
            }
    }

    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}

// int main()
// {
//     char *word = "a";
//     hash(word);
// }
