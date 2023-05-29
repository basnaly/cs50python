#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;

    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);

    printf("Start size: %i\n", start);

    // TODO: Prompt for end size
    int end = get_int("End size: ");
    printf("End size: %i\n", end);

    if (end < start) {
        printf("End size:%i\n", end);
    }

    printf("End size: %i\n", start);


    // TODO: Calculate number of years until we reach threshold
    int years;

    for (int i = start; i < end; i++)
    {
        years = get_int(start = start + (start / 12));
    }

    // TODO: Print number of years
    printf("Years: %i\n", years);
}
