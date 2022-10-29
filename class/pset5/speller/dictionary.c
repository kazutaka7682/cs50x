// Implements a dictionary's functionality


#include <strings.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>


#include "dictionary.h"
//int strcasecmp(const char *s1, const char *s2);

unsigned int counter;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    node *cursor = table[hash(word)];
    //node *cursor = malloc(sizeof(node));

    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        else
        {
            cursor = cursor->next;
        }
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO
    //unsigned int i = 0;
    //for (; *word != '\0'; i++)
    //{
        //i = i * 137 + *word;
    //}

    //return i % 1987;

    int num = word[0];
    int word_number = 0;

    if (isupper(word[0]))
    {
        word_number = num - 65;
    }
    else
    {
        word_number = num - 97;
    }

    return word_number;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *d = fopen(dictionary, "r");
    if (d == NULL)
    {
        printf("Could not open file.\n");
        return false;
    }

    char buffer[LENGTH + 1];
    while (fscanf(d, "%s", buffer) != EOF)
    {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            unload();
            printf("Could not malloc.\n");
            return false;
        }
        strcpy(n->word, buffer);

        int num = hash(n->word);

        if (table[num] == NULL)
        {
            table[num] = n;
            n->next = NULL;
        }
        else
        {
            n->next = table[num];
            table[num] = n;
        }

        //n->next = table[hash(buffer)];
        //table[hash(buffer)] = n;
        counter++;
    }

    fclose(d);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    //int counter = 0;
    //for (int i = 0; i < N; i++)
    //{
        //while (table[i]->next != NULL)
        //{
            //table[i]->next = table[i];
            //counter++;
        //}
    //}
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    //if (*table == NULL)
    //{
        //return false;
    //}

    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *temp = cursor;
            cursor = cursor->next;
            free(temp);
        }

        //free(table[i]);
    }
    return true;
}
