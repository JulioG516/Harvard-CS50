#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)

{
    string s = get_string("Text: ");

    int letters = count_letters(s);
    int words = count_words(s);
    int sentences = count_sentences(s);
    float index;

//Convert the return to float to help the division
    float st = 100 * (float)sentences / (float)words ; // Gets the average sentences per 100 words
    float l = 100 * (float)letters / (float)words;  //Gets the average letters per 100 words

    index = 0.0588 * l - 0.296 * st - 15.8;

    //Use the math.h method to round the index
    int  indexr = round(index);

    if (indexr >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (indexr < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", indexr);
    }




}
int count_letters(string text)
{
    int countL = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        //Check each character if is  alphabetical
        if (isalpha(text[i]))
        {
            countL++;
        }

        
    }
    return countL;
}
int count_words(string text)
{
    int countW = 1; // Assuming will always have at least one word

    for (int i = 0; i < strlen(text) ; i++)

    {
        // Check if has spaces between the text, and gets word counter by 1
        if (text[i] == ' ')
        {
            countW++;
        }
    }

    return countW;
}
int count_sentences(string text)
{
    int countST = 0;
    for (int i = 0; i < strlen(text) ; i++)

    {
        //If the text has one of these, the sentence counter goes by 1
        if (text[i] == '!' || text[i] == '?' || text[i] == '.')
        {
            countST++;
        }
    }
    return countST;
}