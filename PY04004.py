from math import *
class PhanSo:
    def __init__ (self , tu, mau):
        self.tu = tu
        self.mau = mau
    def rut_gon(self):
        uoc_chung_lon_nhat = gcd(self.tu , self.mau)
        self.tu = self.tu // uoc_chung_lon_nhat
        self.mau = self.mau // uoc_chung_lon_nhat
    def tinh_tong(self , phan_so_a):
        tu_tong_phan_so = self.tu * phan_so_a.mau + self.mau * phan_so_a.tu
        mau_tong_phan_so = self.mau * phan_so_a.mau
        tong_phan_so = PhanSo(tu_tong_phan_so , mau_tong_phan_so)
        return tong_phan_so
    def __str__ (self):
        return "{}/{}".format(self.tu , self.mau)

if __name__ == "__main__":
    a , b , c , d = list(map(int , input().split()))
    phan_so_a = PhanSo(a , b)
    phan_so_b = PhanSo(c , d)
    tong_phan_so = phan_so_a.tinh_tong(phan_so_b)
    tong_phan_so.rut_gon()
    print(tong_phan_so)