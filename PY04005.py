from math import *
class Triangle:
    def __init__(self , canh_a , canh_b , canh_c):
        self.canh_a = canh_a
        self.canh_b = canh_b
        self.canh_c = canh_c
    def kiem_tra_thoa_man(self):
        if self.canh_a >= (self.canh_b + self.canh_c) or self.canh_b >= (self.canh_a + self.canh_c) or self.canh_c >= (self.canh_b + self.canh_a): return False
        return True
    def tinh_chu_vi(self):
        return self.canh_a + self.canh_b + self.canh_c
    def __str__(self):
        return "{:.3f}".format(self.tinh_chu_vi())
def tinh_khoang_cach(a , b , c , d):
    return sqrt((a - c)**2 + (b - d)**2)
if __name__ == "__main__":
    a =[]
    t = int(input())
    for _ in range(t):
        a.extend(x for x in list(map(float , input().split())))
    i = 0
    for _ in range(t):
        canh_a = tinh_khoang_cach(a[i + 0] , a[i + 1] , a[ i + 2] , a[i + 3])
        canh_b = tinh_khoang_cach(a[i + 0] , a[i + 1] , a[i + 4] , a[i + 5])
        canh_c = tinh_khoang_cach(a[i + 2] , a[i + 3] , a[i + 4] , a[i + 5])
        i += 6
        tri_a = Triangle(canh_a , canh_b , canh_c)
        if tri_a.kiem_tra_thoa_man() == False:
            print("INVALID")
        else:
            print(tri_a)