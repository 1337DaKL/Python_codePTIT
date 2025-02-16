from math import *
def kiemTraSoNguyenTo(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def nguyenToDungViTri(s) :
    for i in range(len(s)):
        if (kiemTraSoNguyenTo(i) and s[i] not in "2357") or (kiemTraSoNguyenTo(i) == False and s[i] in "2357"): return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if nguyenToDungViTri(s) : print("YES")
        else: print("NO")
# 2
# 14239567
# 2314514535353