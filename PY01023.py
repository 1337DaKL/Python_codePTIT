from math import *
test = int(input())
for _ in range(test):
    n = int(input())
    print("1", end="")
    for i in range(2 , isqrt(n) , 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                dem += 1
                n //= i
            print(" * " , end = "")
            print(i , end = "^")
            print(dem , end = "")
    if n > 2:
        print(" * ", end="")
        print(n,end="^1")
    print()