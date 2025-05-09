from math import *
def demUocSo(n):
    dem = 0
    for i in range(1 , isqrt(n) + 1):
        if n % i == 0  and i * i != n: dem += 2
        elif i * i == n : dem +=1
    return dem
def check(n):
    dem = 0
    for i in range(1 , n):
        if demUocSo(i) == 9: dem += 1
    return dem
if __name__ == "__main__":
    n = int(input())
    print(check(n))
