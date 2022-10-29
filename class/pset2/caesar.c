#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("missing command-line argument\n");
        return 1;
    }
    
    for (int i = 0, m = strlen(argv[1]); i < m; i++)
    {
        if (argv[1][i] < 48 || argv[1][i] > 57)
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    
    string plain = get_string("plaintext: ");
    
    int number = atoi(argv[1]);
    
    for (int j = 0, n = strlen(plain); j < n; j++)
    {
        if ((plain[j] >= 65 && plain[j] <= 90))
        {
            int change = (plain[j] + number) % 65;
            if (change < 26)
            {
                plain[j] = change + 65;
            }
            else 
            {
                plain[j] = (change % 26) + 65;
            }
            // printf("result: %d\n", plain[j]);
        }
        else if ((plain[j] >= 97 && plain[j] <= 122))
        {
            int change = (plain[j] + number) % 97;
            if (change < 26)
            {
                plain[j] = change + 97;
            }
            else 
            {
                plain[j] = (change % 26) + 97;
            }
        }
        else 
        {
            ;
        }
        
    }
    
    printf("ciphertext: %s\n", plain);
    
    return 0;
    
}
