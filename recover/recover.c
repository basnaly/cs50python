#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Should accept one CLA
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *card_file = fopen(argv[1], "r");
    if (card_file == NULL)
    {
        printf("The file %s cannot found", argv[1]);
        return 1;
    }

    int BLOCK_SIZE = 512;
    BYTE buffer[BLOCK_SIZE];
    FILE *img = NULL;
    int count_images = 0;
    char imgname[8];

    while (fread(&buffer, sizeof(BYTE), BLOCK_SIZE, card_file) == BLOCK_SIZE)
    {
        // Check the header of the buffer
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (img != NULL)
            {
                fclose(img);
            }
            // Make new img file
            sprintf(imgname, "%03i.jpg", count_images);
            count_images += 1;

            // Open the new img file
            img = fopen(imgname, "w");

            // Wrire into the new img file
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
        else if (img != NULL)
        {
            fwrite(&buffer, sizeof(BYTE), BLOCK_SIZE, img);
        }
    }
    if (feof(card_file))
    {
        fclose(card_file);
    }
    if (img != NULL)
    {
        fclose(img);
    }
}
