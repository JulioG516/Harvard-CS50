#include <cs50.h>
#include <stdio.h>

int main(void)
{
  int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 0 || n > 8);

    for(int i = 0; i < n; ++i)
    {
        // left part
        for(int l = 0; l < n-1-i; ++l)
        {
            printf(" ");
        }

        for(int l = 0; l < i + 1; ++l)
        {
            printf("#");
        }

        // space between pyramid
        printf("  ");


         // right part
        for(int r = 0; r < i + 1; ++r)
            printf("#");
        for(int r = 0; r < n-1-i; ++r)
            printf(" ");

        printf("\n");

    }


}

