#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    // Initialize the variable score
    int score = 0;
    //Picks the length of string with strlen
    for (int i = 0, length = strlen(word); i < length; i++)
    {
        //check if is upper then do  -65 to go to the index value in the array points like A - 65 = 0 which in our array [0] is A

        if (isupper(word[i]))
        {
            score += POINTS[word[i] - 65];
        }
        //check if is lower then do  -97 to go to the index value in the array points
        else if (islower(word[i]))
        {
            score += POINTS[word[i] - 97];
        }
    }
    return score;
}


