#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    // Ensure proper usage
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    // Open file (card.raw)
    FILE *file = fopen(argv[1], "r");

    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 1;
    }

    // Look for beginning of jpeg
    buffer[0] == 0xff
    buffer[1] == 0xd8
    buffer[2] == 0xff
    (buffer[3] & 0xf0) == 0xe0

    // Create a new jpeg file
    sprintf(filename, "%03i.jpg", 2)

    // Write 512 bytes until a new jpeg is found

    // Stop at end of the file
}