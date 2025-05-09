from math import *
def kiemTraNguenTo(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
def uuTheNguyenTo(s):
    if kiemTraNguenTo(len(s)) == False: return False
    count = 0
    for i in range(len(s)):
        if s[i] in "2357":
            count += 1
    if count < len(s) - count: return False
    return True
if __name__ == "__main__":
    test = int(input())
    for i in range(test):
        s = input()
        if uuTheNguyenTo(s): print("YES")
        else: print("NO")
# 3
# 1234567
# 22334455667
# 23400300489898989