#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int size;

    size = get_int("Height: ");

    do
    {
        printf("Height, %i\n", size);
    }
    while (size > 1 || size > 8);

    for (int i = 0; i < size; i++)
    {
        for (int j = 0; j < size; j++)
        {
            if (size - i > j + 1)
            {
                printf(" ");
            }
            else
            {
                printf("#");
            }
        }
        printf("  ");
        for (int k = 0; k < size; k++)
        {
            if (i < k)
            {
                printf("  ");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}