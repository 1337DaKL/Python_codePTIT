from math import *
def kiemTraSoNguyenTo(n):
    for i in range(2 , isqrt(n) + 1):
        if n % i == 0: return False
    return n > 1
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraSoNguyenTo(int(s[len(s) - 4: len(s)])): print("YES")
        else: print("NO")
# 3
# 12234323130097
# 3443354654654654461123
# 43543543434554659999