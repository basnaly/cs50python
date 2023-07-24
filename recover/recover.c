#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE \n");
        return 1;
    }

    // Open a memory card
    FILE *file = fopen(argv[1],"r");
    if (file == NULL)
    {
        fclose(file);
        printf("Could not open file %s\n", argv[1]);
        return 1;
    }

    int BLOCK_SIZE = 512;
    BYTE buffer[BLOCK_SIZE];
    int count_image = 0;
    char filename[8];
    FILE *img = NULL;

    while(fread(&buffer, sizeof(BYTE), BLOCK_SIZE, file) == BLOCK_SIZE)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If image exists close it
            if (img != NULL)
            {
                fclose(img);
            }
            // Make a new jpeg file
            sprintf(filename, "%03i.jpg", count_image);

            count_image += 1;

            // Open the jpeg file
            img = fopen(filename, "w");

            // Write the buffer to the img file
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
        else if (img != NULL)
        {
            // Write the buffer to the img file
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
    }
    fclose(img);
    if (feof(file))
        {
            fclose(file);
        }
}