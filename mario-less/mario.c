#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int size;

    do
    {
        size = get_int("Height: ");
    }
    while (size < 1 || size > 9);

    for (char i = 0; i < size; i++)
    {
        for (char j = 1; j < i; j++) {
            printf("#\n");
        }

    }

}