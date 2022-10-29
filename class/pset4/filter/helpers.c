#include "helpers.h"
#include <math.h>
#include <string.h>

#include <getopt.h>
#include <stdio.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int average = (int)(round((image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed)/3.0));
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sepia1 = (int)(round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue));
            int sepia2 = (int)(round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue));
            int sepia3 = (int)(round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue));
            
            if (sepia1 > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else 
            {
                image[i][j].rgbtBlue = sepia1;
            }
            
            if (sepia2 > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else 
            {
                image[i][j].rgbtGreen = sepia2;
            }
            
            if (sepia3 > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else 
            {
                image[i][j].rgbtRed = sepia3;
            }
        }
    }
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0, n = width/2; j < n; j++)
        {
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width-(j + 1)];
            image[i][width-(j + 1)] = temp;
        }
    }
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Yuri
    RGBTRIPLE(*ret)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = 0;
            int red = 0;
            int green = 0;
            int null_count = 0;
            
            for (int x = (i - 1); x <= (i + 1); x++)
            {
                for (int y = (j - 1); y <= (j + 1); y++)
                {
                    if (x < 0 || x > (height - 1) || y < 0 || y > (width - 1))
                    {
                        null_count++;
                        //continue;
                    }
                    else
                    {
                        blue += image[x][y].rgbtBlue;
                        red += image[x][y].rgbtRed;
                        green += image[x][y].rgbtGreen;
                    }
                }
            
            }
            //null_count = 0;
            ret[i][j].rgbtBlue = round((double)(blue) / (double)(9 - null_count));
            ret[i][j].rgbtRed = round((double)(red) / (double)(9 - null_count));
            ret[i][j].rgbtGreen= round((double)(green) / (double)(9 - null_count));
        }
    }
    
    for (int s = 0; s < height; s++)
    {
        for (int t = 0; t < width; t++)
        {
            image[s][t] = ret[s][t];
        }
    }
}
