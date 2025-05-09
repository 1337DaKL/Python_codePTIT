from math import *
def tongUocSo(n):
    tong = 0
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                tong += i
                n //= i
    if n > 1 : tong += n
    return tong
if __name__ == "__main__":
    test = int(input())
    tong = 0
    for _ in range(test):
        n = int(input())
        tong += tongUocSo(n)
    print(tong)
# 5
# 7
# 9
# 10
# 13
# 100