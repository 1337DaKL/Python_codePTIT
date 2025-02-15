from math import *
test = int(input())
for _ in range(test):
    s = input()
    if gcd(int(s) , int(s[::-1])) == 1:
        print("YES")
    else :
        print("NO")