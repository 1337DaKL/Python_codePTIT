from math import *
class Point:
    def __init__ (self , x , y):
        self.x = x
        self.y = y
    def tinh_canh(self , a):
        return sqrt((a.x - self.x)** 2 + (a.y - self.y) ** 2)
class Triangle:
    def __init__(self , point_1 , point_2 , point_3 , point_4 , point_5  , point_6):
        self.diem_a = Point(point_1 , point_2)
        self.diem_b = Point(point_3 , point_4)
        self.diem_c = Point(point_5 , point_6)
    def kiem_tra(self):
        canh_a = self.diem_a.tinh_canh(self.diem_b)
        canh_b = self.diem_b.tinh_canh(self.diem_c)
        canh_c = self.diem_a.tinh_canh(self.diem_c)
        if canh_a < (canh_b + canh_c) and canh_b < (canh_a + canh_c) and canh_c < (canh_a + canh_b):
            return True
        return False
    def tinh_dien_tich(self):
        canh_a = self.diem_a.tinh_canh(self.diem_b)
        canh_b = self.diem_b.tinh_canh(self.diem_c)
        canh_c = self.diem_a.tinh_canh(self.diem_c)
        return (1 / 4)* (sqrt((canh_a + canh_b + canh_c )*(-canh_c + canh_a + canh_b) * (-canh_a + canh_b + canh_c) * (-canh_b + canh_a + canh_c)))
    def __str__(self):
        return "{:.2f}".format(self.tinh_dien_tich())
if __name__ == "__main__":
    a = []
    t = int(input())
    for _ in range(t):
        a.extend(x for x in list(map(float , input().split())))
    i = 0
    for _ in range(t):
        tam_giac = Triangle(a[i + 0] , a[i + 1] , a[i + 2] , a[i + 3] , a[i + 4] , a[i + 5])
        i += 6
        if tam_giac.kiem_tra():
            print(tam_giac)
        else:
            print("INVALID")