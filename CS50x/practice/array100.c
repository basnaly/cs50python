// Create an array of 100 ints and the first element put 0

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int length = 100;
    int array[length];

    for (int i = 0; i < length; i++)
    {
        array[i] = i + 1;
        printf("%i ", array[i]);
    }
    printf("\n");
    return 0;
}


// What it will return?

// void set_array(int array[4]);
// void set_int(int x);

// int main(void)
// {
//     int a = 10;
//     int b[4] = {0, 1, 2, 3};
//     set_int(a);
//     set_array(b);
//     printf("%d %d\n", a, b[0]);
// }

// void set_array(int array[4])
// {
//     array[0] = 22;
// }

// void set_int(int x)
// {
//     x = 22;
// }
