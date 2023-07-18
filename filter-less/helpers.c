#include "helpers.h"
#include<math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];
            int average_pixel = round((pixel->rgbtBlue + pixel->rgbtGreen + pixel->rgbtRed) / 3);

            pixel->rgbtBlue = average_pixel;
            pixel->rgbtGreen = average_pixel;
            pixel->rgbtRed = average_pixel;
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
