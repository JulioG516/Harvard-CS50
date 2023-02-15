#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

bool only_digits(string text);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    // If the command line is more or less then one gets the correctly usage message

    if (argc == 2)
    {

    }
    else
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //Test if the command line is numbers

    bool test = only_digits(argv[1]);

    if (test != 1)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //pass the command line string to int
    int key = atoi(argv[1]);

    //Pick user input
    string plaintext = get_string("Plaintext: ");

    char rotation;

    printf("ciphertext: ");
    for (int i = 0; i < strlen(plaintext); i++)
    {
        char cipher = rotate(plaintext[i], key);
        printf("%c", cipher);

    }
    printf("\n");

}


bool only_digits(string text)
{
    //check  if received text who is argv[1] is a positive digit
    for (int i = 0; i < strlen(text); i++)
    {
        if (isdigit(text[i]) == false)
        {
            return false;
        }
    }
    return true;
}

char rotate(char c, int n)
{
    if (c >= 'A' && c <= 'Z')
    {
        char cp = c - 'A'; // - 65
        cp += n;
        cp = cp % 26;
        c = cp + 'A';
    }
    else if (c >= 'a' && c <= 'z')
    {
        char cp = c - 'a'; // - 97
        cp += n;
        cp = cp % 26;
        c = cp + 'a';
    }
    return c;
}