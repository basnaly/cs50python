#include "helpers.h"
#include <math.h>
#include <stdlib.h>
#include <stdio.h>

int max(int i, int j)
{
    if (i < j)
    {
        return j;
    }
    return i;
}

int min(int i, int j)
{
    if (i < j)
    {
        return i;
    }
    return j;
}

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
   for (int i = 0; i < height; i++)
   {
    for (int j = 0; j < width; i++)
    {
        RGBTRIPLE *pixel = &image[i][j];
        int gray = round((float)(pixel->rgbtBlue + pixel->rgbtGreen + pixel->rgbtRed) / 3.0);
    }
   }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    return;
}
