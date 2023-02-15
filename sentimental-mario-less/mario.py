from cs50 import get_int
while True:  # As python dont have do while we use the solution passed on lecture
    n = get_int("Height: ")
    if n >= 1 and n <= 8:  # check if the number is valid in range of 1 and 8
        break

for i in range(n):
    for l in range(n - 1 - i):
        print(" ", end='')

    for l in range(i + 1):
        print("#", end='')
    print("")