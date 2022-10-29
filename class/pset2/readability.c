#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    
    // printf("%d letter(s)\n", count_letters(text));
    
    // printf("%d word(s)\n", count_words(text));
    
    // printf("%d sentence(s)\n", count_sentences(text));
    
    
    float L = ((float)count_letters(text) * 100.0) / (float)count_words(text);
    float S = ((float)count_sentences(text) * 100.0) / (float)count_words(text);
    float index = 0.0588 * L - 0.296 * S - 15.8;
    int grade = round(index);
    
    if (grade >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (grade < 1)
    {
        printf("Before Grade 1\n");
    }
    else 
    {
        printf("Grade %d\n", grade);
    }
    
}

int count_letters(string text)
{
    int counter1 = 0;
    
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] >= 65 && text[i] <=90)
        {
            counter1++;
        }
        else if (text[i] >= 97 && text[i] <= 122)
        {
            counter1++;
        }
        else 
        {
            ;
        }
    }
    
    return counter1;
}

int count_words(string text)
{
    int counter2 = 1;
    
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 32)
        {
            counter2++;
        }
    }
    
    return counter2;
}

int count_sentences(string text)
{
    int counter3 = 0;
    
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        if (text[i] == 33 || text[i] == 46 || text[i] == 63)
        {
            counter3++;
        }
    }
    
    return counter3;
}

