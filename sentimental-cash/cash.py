from cs50 import get_float


def main():
    cents = get_cents()  # getting how many cents, by using our function
    coins = 0  # keeping track of number of coins

    # Calculate number of quarters
    while cents >= 25:
        cents = cents - 25
        coins = coins + 1  # we cant get coins++ like in C

    # Calculate number of dimes
    while cents >= 10:
        cents = cents - 10
        coins = coins + 1

    # Calculate number of nickels
    while cents >= 5:
        cents = cents - 5
        coins = coins + 1

    # Calculate number of pennies
    while cents >= 1:
        cents = cents - 1
        coins = coins + 1

    print(f"Total coins: {coins}")  # using string interpolation


# So i tried doing multiple functions like the cash in C language, but that was the only function i can abstract
# doing the division like in C does not work here like to obtain quarters cents / 25, you can't get here
# but i think  that option  was more easier than C version, i just needed to think a little more
def get_cents():
    while True:
        cents = get_float("Change owed ")
        if cents > 0:
            break
    cents = round(cents * 100)
    return cents

main()