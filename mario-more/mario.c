#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;

    //Pick user input between 1 and 8, and mount the pyramid
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    //Loop to add Row and Columns
    for (int i = 0; i < n; ++i)
    {
        // left part
        for (int l = 0; l < n - 1 - i; ++l)
        {
            printf(" ");
        }

        for (int l = 0; l < i + 1; ++l)
        {
            printf("#");
        }

        // two space between pyramid
        printf("  ");


        // right part
        for (int r = 0; r < i + 1; ++r)
        {
            printf("#");
        }
        printf("\n");

    }


}

