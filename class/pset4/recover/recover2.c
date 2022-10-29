#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image");
        return 1;
    }
    
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open file.");
        return 1;
    }
    
    const int BYTE_SIZE = 512;
    
    typedef uint8_t BYTE;
    
    BYTE buffer[BYTE_SIZE];
    
    int found = 1;
    int counter = -1;
    
    FILE *recover = NULL;
    
    while (fread(buffer, BYTE_SIZE, 1, card))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            found = 0;
            counter++;
            if (counter == 0)
            {
                char name[7];
                sprintf(name, "00%i.jpg", counter);
                recover = fopen(name, "wb");
                if (recover == NULL)
                {
                    printf("Could not open file.\n");
                    return 1;
                }   
                fwrite(buffer, BYTE_SIZE, 1, recover);
            }
            else 
            {
                fclose(recover);
                char name[7];
                if (counter <= 9)
                {
                    sprintf(name, "00%i.jpg", counter);
                }
                else 
                {
                    sprintf(name, "0%i.jpg", counter);
                }
                recover = fopen(name, "w");
                if (recover == NULL)
                {
                    printf("Could not open file.\n");
                    return 1;
                }   
                fwrite(buffer, BYTE_SIZE, 1, recover);
                counter--;
            }
        }
        else 
        {
            if (found == 0)
            {
                char name[7];
                if (counter <= 9)
                {
                    sprintf(name, "00%i.jpg", counter);
                }
                else 
                {
                    sprintf(name, "0%i.jpg", counter);
                }
                recover = fopen(name, "a");
                if (recover == NULL)
                {
                    printf("Could not open file.\n");
                    return 1;
                }   
                fwrite(buffer, BYTE_SIZE, 1, recover);
            }
        }
    }
    
    fclose(card);
}
