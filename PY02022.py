from math import *
def kiem_tra_so_nguyen_so(n):
    for i in range(2 , isqrt(n) + 1 , 1):
        if n % i == 0: 
            return False
    return n > 1
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int , input().split()))
    dict_prime = {}
    for it in arr:
        if kiem_tra_so_nguyen_so(it):
            if it in dict_prime:
                dict_prime[it] += 1
            else:
                dict_prime[it] = 1
    for key, value in dict_prime.items():
        print(key , value)