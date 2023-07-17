// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file

    // Create an array of bytes to store the data from the WAV file of the input file.
    unit8_t header[HEADER_SIZE];

    // Create a buffer to store audio samples from the WAV file
    unit16_t buffer;

    // Read the header from the input file
    fread(&header, sizeof(unit8_t) * HEADER_SIZE, 1, input)

    // Write the header to the output file
    fwrite(&header, sizeof(unit8_t) * HEADER_SIZE, 1, output)

    // TODO: Read samples from input file and write updated data to output file

    // Read the rest of the data from the input file
    fread(&buffer, sizeof(unit16_t) * HEADER_SIZE, 1, input)

    // Close files
    fclose(input);
    fclose(output);
}
