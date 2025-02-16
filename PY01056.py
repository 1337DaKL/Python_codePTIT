from math import *
def kiemTraSoNguyenTo(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def tinhTong(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong
def chanLeNguyenTo(s):
    for i in range(len(s)):
        if i % 2 != int(s[i]) % 2: return False
    if kiemTraSoNguyenTo(tinhTong(s)) : return True
    return False
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if chanLeNguyenTo(s): print("YES")
        else: print("NO")
# 2
# 2345678521
# 1212121212121212121212121