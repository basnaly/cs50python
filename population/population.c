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
    while start < 9

    printf("Start size: %i\n", start);

    // TODO: Prompt for end size
    int end;

    do
    {
        end = get_int("End size: ");
    }
    while (end < start)

    printf("End size: %i\n", end);

    // TODO: Calculate number of years until we reach threshold
    int years;

    while(start < end)
    {
        years = start + (start / 3) - (start /4);
    }

    // TODO: Print number of years
    printf()
}
