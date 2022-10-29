#include <stdio.h>
#include <cs50.h>
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
    
    int counter = 0;
    
    while (fread(buffer, BYTE_SIZE, 1, card))
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            char name[7];
            sprintf(name, "000.jpg");
            FILE *recover = fopen(name, "w");
            fwrite(buffer, BYTE_SIZE, 1, recover);
        }
        
        fclose(recover);
    }
}

