#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;

    do
    {
        size = get_int("Height: ");
    }
    while (size < 1 || size > 8);

    printf("Height: %i\n", size);

    for (char i = 0; i < size; i++) {

        for (char j = 0; j < size; j++)
        {
            if (size - i < j + 2)
            {
                printf("#");
            }
            else if (size - i > j + 3)
            {
                printf("..");
            }
            else
            {
                printf(".");
            }

        }

        printf("\n");
    }
}