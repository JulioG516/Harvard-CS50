#include <cs50.h>
#include <stdio.h>


int main(void)
{
    // Get user name and store on a string
    string name = get_string("What's your name ? ");
    // Print out the text Hello and the inputed
    printf("Hello, %s!\n", name);
}

