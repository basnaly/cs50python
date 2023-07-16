#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    RGBTRIPLE (&pixel) = image[height][width];

    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (((*pixel[i][j]).rgbtBlue == 0) && ((*pixel[i][j]).rgbtGreen == 0) && ((*pixel[i][j]).rgbtRed == 00))
            {
                (*pixel[i][j]).rgbtBlue = 200;
                (*pixel[i][j]).rgbtGreen = 120;
                (*pixel[i][j]).rgbtRed = 250;
            }

        }
    }
    return 0;
}
