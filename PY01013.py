from math import *
def tinhTongChuSo(n) :
    tong = 0
    while n > 0:
        tong = tong + n % 10
        n //= 10
    return tong
def kiemTraSoNguyenTo(n) :
    for i in range(2 , isqrt(n) + 1 , 1) :
        if n % i == 0 : return  False
    return n > 1
if __name__ == "__main__" :
    test = int(input())
    for _ in range(test):
        a , b = map(int , input().split())
        if kiemTraSoNguyenTo(tinhTongChuSo(gcd(a , b))):
            print("YES")
        else : print("NO")