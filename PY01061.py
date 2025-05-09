from math import *
def kiemTraSoNguyenTo(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def kiemTraSoDauCuoi(s):
    if kiemTraSoNguyenTo(int(s[0 : 3])) and kiemTraSoNguyenTo(int(s[len(s) - 3: len(s)])): return True
    return False
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraSoDauCuoi(s) : print("YES")
        else: print("NO")
# 3
# 12743
# 7337
# 12345678901234