#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int BLOCK_SIZE = 512;

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

    if (file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];

    // Repeat until end of card
    // Read 512 bytes into a buffer
    while (fread(&buffer, sizeof(BYTE), BLOCK_SIZE, file) == BLOCK_SIZE)
    {
    // If start of new jpeg

        // If first jpeg...
    // Look for beginning of jpeg and read 512 bytes into a buffer
    if ( buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
    {
        // Make a name for jpeg file
        sprintf(filename, "%03i.jpg", 2);

        // Create a new jpeg file
        FILE *img = fopen(filename, "w");

        // Write  512 bytesof a new jpeg file
        fwrite(buffer, sizeof(BYTE),BLOCK_SIZE, img);
    }

    // Stop at end of the file, fread returns number of items were read

        // Else ...
    // Else
        // If already found jpeg

    // Close any remaining files
    }
}