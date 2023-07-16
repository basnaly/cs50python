#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    RGBTRIPLE *pixel = image[0][0];
    for (int i = 0; i < width; i++)
    {
        for (int j = 0; j < height; j++)
        {
            if (((*pixel).rgbtBlue == 0) && ((*pixel).rgbtGreen == 0) && ((*pixel).rgbtRed == 00))
            {
                (*pixel).rgbtBlue = 200;
                (*pixel).rgbtGreen = 120;
                (*pixel).rgbtRed = 250;
            }

        }
    }
    return 0;
}
