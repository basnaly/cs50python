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
    else if()

    // Open a new jpeg file

    // Write 512 bytes until a new jpeg is found

    // Stop at end of the file
}