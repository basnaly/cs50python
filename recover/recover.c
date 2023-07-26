#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }

    // Open the memory card
    FILE *card_file = fopen(argv[1], "r");

    if (card_file == NULL)
    {
        printf("Could not open %s file.\n", argv[1]);
        return 1;
    }

    int BLOCK_SIZE = 512;
    BYTE buffer[BLOCK_SIZE];
    FILE *img;
    char img_name[8];
    int count_img = 0;

    // Read the memory card in loop and save the data in buffer
    while (fread(&buffer, sizeof(BYTE), BLOCK_SIZE, card_file) == BLOCK_SIZE)
    {
        // Look for beggining of a jpeg
        if (buffer[0] = 0xff && buffer[1] = 0xd8 && buffer[2] = 0xff && (buffer[3] & 0xf0) = 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }

            // Create the name of the new jpeg file
            sprintf(img_name, "%03i.jpg", count_img);
            count_img += 1;

            // Open the new img file
            img = fopen(img_name, "w");

            // Write the data from buffer to the img file
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, &img);
        }
        else
        {
            // Write the data from buffer to the img file
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, &img);
        }
    }
    fclose(img);
    if (feof)
    {
        fclose(card_file);
    }
}