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
    for (int j = 0; j < width; j++)
    {
        RGBTRIPLE *pixel = &image[i][j];

        int average = round((float)(pixel->rgbtBlue + pixel->rgbtGreen + pixel->rgbtRed) / 3.0);

        pixel->rgbtBlue = average;
        pixel->rgbtGreen = average;
        pixel->rgbtRed = average;
    }
   }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];

            int sepiaRed = 0;
            int sepiaGreen = 0;
            int sepiaBlue = 0;

            sepiaRed = round(.393 * pixel->rgbtRed + .769 * pixel->rgbtGreen + .189 * pixel->rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }

            sepiaGreen = round(.349 * pixel->rgbtRed + .686 * pixel->rgbtGreen + .168 * pixel->rgbtBlue);
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            sepiaBlue = round(.272 * pixel->rgbtRed + .534 * pixel->rgbtGreen + .131 * pixel->rgbtBlue);
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            pixel->rgbtBlue = sepiaBlue;
            pixel->rgbtGreen = sepiaGreen;
            pixel->rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];

            RGBTRIPLE right = image[i][j];
            RGBTRIPLE left = image[i][width - j - 1];

            image[i][width - j - 1] = right;
            image[i][j] = left;
        }
    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE *pixel = &image[i][j]

            for (int ii = 0; ii < max(j - 1,))
        }
    }
    return;
}
