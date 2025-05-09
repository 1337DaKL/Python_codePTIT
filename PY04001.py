from math import *
class Point:
    def __init__ (self , tu , mau):
        self.tu = tu
        self.mau = mau
    def distance(self , a):
        return "{:.4f}".format(sqrt((self.tu - a.tu) ** 2  + (self.mau - a.mau) ** 2))
def Decimal(x):
    return float(x)
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1