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
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
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
        while(fscanf(*dict_file, "%s", dict_word) == 1)
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
            table[index] = new_node;
                // Recall that hash table is an array of linked lists
                // Be shure to set pointers in the correct order
                if (new_node == NULL)
                {
                    
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
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
