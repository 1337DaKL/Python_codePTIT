from math import *
n , m = map(int , input().split())
dem = 0
for i in range(int(pow(10 ,  m - 1)) , int(pow(10 , m)) , 1):
    if gcd(i , n) == 1 :
        print(i , end = " ")
        dem += 1
    if dem == 10 :
        dem = 0
        print()