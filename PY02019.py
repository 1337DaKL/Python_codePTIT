from math import *
n = int(input())
arr = list(map(int , input().split()))
arr.sort()
for i in range(len(arr)):
    for j in range(i + 1 , len(arr)):
        if gcd(arr[i] , arr[j])  == 1 :
            print(arr[i] , arr[j] , sep = " " , end = "\n")