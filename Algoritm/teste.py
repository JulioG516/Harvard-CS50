a = 6
b = 10
f = False

x = a
if b > x:
    x = b

if f == False:
    while f:
        if x % a == 0 and x % b == 0:
            f == True
    else:
        x = x + 1
print(x)