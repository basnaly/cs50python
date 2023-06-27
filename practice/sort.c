#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int length = 4;
    int temps[] = {97, 82, 85, 90};

    for (int i = 0; i < length; i++)
    {
        int min = temps[i];
        int current = temps[i];
        int index_min = i;

        for (int j = i; j < length; j++)
        {
            if (temps[j] < min)
            {
                min = temps[j];
                index_min = j;
            }
        }

        temps[i] = min;
        index_min = i;
        current = temps[i];
    }
}