from math import *
class PhanSo:
    def __init__(self , tu , mau):
        self.tu = tu
        self.mau = mau
    def rut_gon(self):
        uoc_chung_lon_nhat = gcd(self.tu, self.mau)
        self.tu = self.tu // uoc_chung_lon_nhat
        self.mau = self.mau // uoc_chung_lon_nhat
    def __str__(self):
        return "{}/{}".format(self.tu , self.mau)


if __name__ == "__main__":
    tu , mau = list(map(int , input().split()))
    a = PhanSo(tu , mau)
    a.rut_gon()
    print(a)