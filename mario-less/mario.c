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

    for (char i = 0; i < size; i++)
    {
        for (char j = 0; j < size; j++)
        {
            if (size - i > j+1)
            {
                printf(".");
            }
            else
            {
                printf("#");
            }
        }
        printf("\n");
    }
}