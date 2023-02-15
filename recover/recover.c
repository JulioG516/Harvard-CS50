#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    const int BLOCK_SIZE = 512; //Declare our const to use instead of using 512 all the time
    //Check if is 1 command line argument
    if (argc == 2)
    {

    }
    else
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }

    FILE *card = fopen(argv[1], "r");

    if (card == NULL)
    {
        printf("cannot be opened.\n");
        return 1;
    }

    BYTE buffer[BLOCK_SIZE];
    int imgCounter = 0;
    FILE *output = NULL;
    char filename[8];

    while (fread(buffer, sizeof(BYTE), BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        //Check if is a valid JPG by checking the headers for a JPG      Bitwise Arithmetic
        if (buffer[0] == 0xff & buffer[1] == 0xd8 & buffer[2] == 0xff & (buffer[3] & 0xf0) == 0xe0)
        {
            //Check's if is the first JPG
            if (imgCounter == 0)
            {
                sprintf(filename, "%03i.jpg", imgCounter);

                output = fopen(filename, "w");

                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
                //Increase the img counter
                imgCounter++;
            }

            //If is not the first image
            else if (imgCounter > 0)
            {
                //If its not the first image, we close the previously
                fclose(output);
                //Do the same thing
                sprintf(filename, "%03i.jpg", imgCounter);

                output = fopen(filename, "w");

                fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);

                imgCounter++;
            }
        }
        //Keep writing the multiple block
        else if (imgCounter > 0)
        {
            fwrite(buffer, sizeof(BYTE), BLOCK_SIZE, output);
        }
    }
    fclose(output);
    fclose(card);
}