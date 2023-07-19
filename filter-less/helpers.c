#include "helpers.h"
#include<math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
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
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            RGBTRIPLE *pixel = &image[i][j];

            int sepia_red = round(.393 * pixel->rgbtRed + .769 * pixel->rgbtGreen + .189 * pixel->rgbtBlue);
            if (sepia_red > 255)
            {
                sepia_red = 255;
            }

            int sepia_green = round(.349 * pixel->rgbtRed + .686 * pixel->rgbtGreen + .168 * pixel->rgbtBlue);
            if (sepia_green > 255)
            {
                sepia_green = 255;
            }

            int sepia_blue = round(.272 * pixel->rgbtRed + .534 * pixel->rgbtGreen + .131 * pixel->rgbtBlue);
            if (sepia_blue > 255)
            {
                sepia_blue = 255;
            }

            pixel->rgbtBlue = sepia_blue;
            pixel->rgbtGreen = sepia_green;
            pixel->rgbtRed = sepia_red;
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
            RGBTRIPLE right = image[i][j];
            RGBTRIPLE left = image[i][width - 1 - j];

            image[i][width - 1 - j] = right;
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
            RGBTRIPLE *pixel = image[i][j];
            for (int ii = max(0, i - 1); ii <= min(i + 1, height - 1); ii++)
            {
                for (int jj = max(0, j - 1); jj <= min(j + 1, width - 1); jj++)
                {
                    int 
                }
            }
        }
    }
    return;
}
