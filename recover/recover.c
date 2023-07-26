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

    FILE *card_file = fopen(argv[1], "r");

    if (card_file == NULL)
    {
        printf("Could not open %s file.\n", argv[1]);
        return 1;
    }

    BYTE BLOCK_SIZE = 512;
    int buffer = 0;

    while (fread(&buffer, sizeof(BLOCK_SIZE), BYTE, card_file) == BLOCK_SIZE)
    {

    }

}