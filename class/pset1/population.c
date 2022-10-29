#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // TODO: Prompt for start size
    int s;
    
    do 
    {
        s = get_int("Start size : ");
    }
    while (s < 9);
    
    // TODO: Prompt for end size
    int e;
    
    do 
    {
        e = get_int("End size : ");
    }
    while (e < s);

    // TODO: Calculate number of years until we reach threshold
    int count = 0;
    int n = s;
    while (e > n)
    {
        n = n + n/3 - n/4;
        count++;
    }
    

    // TODO: Print number of years
    // printf("total : %d\n", n);
    printf("Years: %i\n", count);
    
    return 0;
}