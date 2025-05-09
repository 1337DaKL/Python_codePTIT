class Rectangle:
    def __init__(self, chieu_dai, chieu_rong, mau_sac):
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        self.mau_sac = mau_sac

    def perimeter(self):
        return (self.chieu_dai + self.chieu_rong) * 2

    def area(self):
        return self.chieu_dai * self.chieu_rong

    def color(self):
        return str(self.mau_sac).title()


if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
