from math import *
def kiemTraSoNguyenTo(n) :
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def tongChuSo(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong

if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraSoNguyenTo(tongChuSo(s)): print("YES")
        else: print("NO")