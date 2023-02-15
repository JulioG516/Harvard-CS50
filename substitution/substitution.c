#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>



int main(int argc, string argv[])
{
    char * keyT = "JTREKYAVOGDXPSNCUIZLFBMWHQ";

    string  plaintext = get_string("Plaintext:");

    string  dec ="Hi";


    printf("%c", keyT[0]);


        for (int i = 0, length = strlen(plaintext); i < length; i++)
    {
        //check if is upper then do  -65 to go to the index value in the array points like A - 65 = 0 which in our array [0] is A

        if (isupper(plaintext[i]))
        {
            dec += keyT[plaintext[i] - 65];
         //   dec += keyT[i];
        }
        //check if is lower then do  -97 to go to the index value in the array points
        else if (islower(plaintext[i]))
        {
            dec += keyT[plaintext[i] - 97];

        }
    }
        printf("Answer: %s", dec);



}