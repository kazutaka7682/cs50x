#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>


int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    string word = get_string("name: ");
    int alphabet = 65;
    int total = 0;
    for (int i = 0, n = strlen(word); i < n; i++)
    {
        if (islower(word[i]))
        {
            word[i] = toupper(word[i]);
        }
        
        for (int j = 0; j < 27; j++)
        {
            while (word[i] == alphabet)
            {
                total += POINTS[j];
            }
            alphabet++;
        }
    }
    
    printf("total: %d\n", total);
    
    return total;
}