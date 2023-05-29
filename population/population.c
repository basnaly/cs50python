#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start = get_int("Start size: ");

    

    if (start < 1) {
        printf(%i\n, start)
    }

    printf(%i\n, start);

    // TODO: Prompt for end size
    int end = get_int("End size: ");
    printf( %i\n, end);

    if (end < start) {
        printf(%i\n, end)
    }

    printf( %i\n, start);


    // TODO: Calculate number of years until we reach threshold
    int years = get int(years + years / 12);

    // TODO: Print number of years
    printf("Years: %i\n, years);
}
