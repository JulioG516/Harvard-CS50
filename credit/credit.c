#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //initiate the variable ccNumber that will store the user input
    long ccNumber;
    do
    {
        ccNumber = get_long("Card Number: ");
    }
    while (ccNumber <= 0);

    //initiate variables to be used in the iteration loops
    int sum = 0;
    //Declare ccTest to be used in iteration to no use ccNumber and do bugs
    long ccTest = ccNumber;
    int count = 0;
    long divisor = 10;
    string cardName;

//pick the digits and do the sum
    while (ccTest > 0)
    {
        int lastDigit = ccTest % 10;
        sum = sum + lastDigit;
        ccTest = ccTest / 100;
    }

    //Gets the second-to-last digit

    ccTest = ccNumber / 10;
    while (ccTest > 0)
    {
        int lastDigit = ccTest % 10;
        int x2 = lastDigit * 2;
        sum = sum + (x2 % 10) + (x2 / 10);
        ccTest = ccTest / 100;
    }
    // length of the number / digit count
    ccTest = ccNumber;
    while (ccTest != 0)
    {
        ccTest = ccTest / 10;
        count++;
    }

    // divisor
    for (int i = 0; i < count - 2; i++)
    {
        divisor = divisor * 10;
    }

    int OneDigit = ccNumber / divisor;
    int TwoDigit = ccNumber / (divisor / 10);

    // if to check the conditions
    if (sum % 10 == 0)
    {
        if (OneDigit == 4 && (count == 13 || count == 16))
        {
            printf("Your Card Number: %lu\n", ccNumber);
            printf("VISA\n");
        }
        else if ((TwoDigit == 34 || TwoDigit == 37) && count == 15)
        {
            printf("Your Card Number: %lu\n", ccNumber);
            printf("AMEX\n");
        }
        else if ((50 < TwoDigit && TwoDigit < 56) && count == 16)
        {
            printf("Your Card Number: %lu\n", ccNumber);
            printf("MASTERCARD\n");
        }
        else
        {
            printf("Please insert a valid Card Number");
            printf("INVALID\n");
        }
    }
    // Invalidates by the length
    else
    {
        printf("Please insert a valid Card Number\n");
        printf("INVALID\n");
    }
}

//