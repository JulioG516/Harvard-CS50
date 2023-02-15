// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
#include <stdlib.h>
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
unsigned int hashValue;
unsigned int wordCounter;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    hashValue = hash(word);
    node *cursor = table[hashValue];

    while (cursor != 0)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    unsigned long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]) - 'a';
    }

    // Here i tried to use the provided hash function passing all chars to lower than removing the number using - 'a' and using a module
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *file = fopen(dictionary, "r");

    if (file == NULL)
    {
        printf("Cannot be opened");
        return false;
    }
    char word[LENGTH + 1];

    //scan directory until end of file
    while (fscanf(file, "%s", word) != EOF)
    {
        //Allocating memory for new node
        node *n = malloc(sizeof(node));

        //Check malloc
        if (n == NULL)
        {
            return false;
        }
        // copy word to our node
        strcpy(n->word, word);
        hashValue = hash(word);
        n->next = table[hashValue];
        table[hashValue] = n;
        wordCounter++;
    }
    fclose(file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (wordCounter > 0)
    {
        return wordCounter;
    }
    else
    {
        return 0;
    }

}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];

        while (cursor != NULL)
        {
            //creating our temporary variable to free up space
            node *tmp = cursor;
            //We set the cursor to the next position, so we can free space
            cursor = cursor->next;
            free(tmp);
        }
        if (cursor == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}
