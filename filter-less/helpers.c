#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average;


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Picking Average of each pixel
            average = round((image[i][j].rgbtBlue + image[i][j].rgbtGreen +  image[i][j].rgbtRed) / 3.0);



            // Setting average to RGB to set a gray pattern
            image[i][j].rgbtBlue = average;
            image[i][j].rgbtGreen = average;
            image[i][j].rgbtRed = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Using the sepia formula on each pixel
            int sepiaRed = round(.393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue);
            int sepiaGreen = round(.349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue);
            int sepiaBlue = round(.272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue);

            // Ensure that sepia dont pass 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }



            //Setting Sepia to our pixels
            image[i][j].rgbtBlue = sepiaBlue;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtRed = sepiaRed;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{


    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            //Creating our temporary variable
            RGBTRIPLE tmp = image[i][j];

            image[i][j] = image[i][width - 1 - j];

            //using our tmp variable
            image[i][width - 1 - j] = tmp;

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];



    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float counter = 0.00;
            int totalBlue, totalGreen, totalRed;
            totalBlue = totalGreen = totalRed = 0;


            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    //Variables to check the neighbours pixel
                    int nbhdX = i + x;
                    int nbhdY = j + y;
                    //Check if the next pixel is valid
                    if (nbhdX < 0 || nbhdX > (height - 1) || nbhdY < 0 || nbhdY > (width - 1))
                    {
                        continue;
                    }

                    //Picks up the total of each colors to obtain the average
                    totalRed += image[nbhdX][nbhdY].rgbtRed;
                    totalBlue += image[nbhdX][nbhdY].rgbtBlue;
                    totalGreen += image[nbhdX][nbhdY].rgbtGreen;

                    counter++;
                }
                //Copy original image to our temporary variable, with the blur already
                copy[i][j].rgbtRed = round(totalRed / counter);
                copy[i][j].rgbtBlue = round(totalBlue / counter);
                copy[i][j].rgbtGreen = round(totalGreen / counter);
            }
        }
    }
    // Passing our temporary blurred to our original
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtRed = copy[i][j].rgbtRed;
            image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
            image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
        }
    }
    return;
}
