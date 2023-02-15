#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int divisor;   // Quantidade a ser passada de moedas, quantidada que deve
    int dividendo; // Numero da moeda  Moedas

    int cents = 95;
    int dividido = cents / 25; // Divisor é a moeda em si
    int resto = cents % 25;
    printf("%i \n",dividido);
    printf("%i \n",resto);

}