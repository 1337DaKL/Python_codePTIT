from math import *
def kiem_tra_so_nguyen_to(n):
    for i in range(2 , isqrt(n) + 1 , 1):
        if n % i == 0: return False
    return n > 1
def pefect_prime(s):
    tong = 0
    for i in range(len(s)):
        if s[i] not in "2357": return False
        tong += int(s[i])
    return kiem_tra_so_nguyen_to(int(s)) and kiem_tra_so_nguyen_to(tong) and kiem_tra_so_nguyen_to(int(s[::-1]))

if __name__ == "__main__":
    for _ in range(int(input())):
        s = input().strip()
        if pefect_prime(s): print("Yes")
        else : print("No")
