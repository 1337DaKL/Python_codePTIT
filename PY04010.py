class ThiSinh:
    def __init__(self, ten , ngay_sinh , diem1 ,diem2 , diem3 ):
        self.ten = ten 
        self.ngay_sinh = ngay_sinh
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tong_diem = diem1 + diem2 + diem3
    def __str__(self):
        return "{} {} {:.1f}".format(str(self.ten).title() , self.ngay_sinh , self.tong_diem)
if __name__ == "__main__":
    thi_sinh = ThiSinh(input() , input() , float(input()) , float(input()) , float(input()))
    print(thi_sinh)