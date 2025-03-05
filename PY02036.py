from math import *
def is_prime(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int , input().split()))
    arr.sort()
    for i in range(len(arr)):
        for j in range(i + 1 , len(arr)):
            if gcd(arr[i] , arr[j]) == 1:
                print(arr[i], arr[j])