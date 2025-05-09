class SoPhuc:
    def __init__(self, thuc , ao):
        self.thuc = thuc
        self.ao = ao
    def nhan(self , so_phuc):
        phan_thuc  = self.thuc * so_phuc.thuc - self.ao * so_phuc.ao
        phan_ao = self.thuc * so_phuc.ao + self.ao * so_phuc.thuc
        return SoPhuc(phan_thuc , phan_ao)
    def cong(self , so_phuc):
        return SoPhuc(self.thuc + so_phuc.thuc , self.ao + so_phuc.ao)
    def __str__(self):
        if self.ao > 0:
            return "{} + {}i".format(self.thuc , self.ao)
        else:
            return "{} - {}i".format(self.thuc , abs(self.ao))
if __name__ == "__main__":
    t = int(input())
    arr = []
    while True:
        try:
            arr.extend(list(map(int , input().split())))
        except:
            break
    i = 0
    for _ in range(t):
        a , b , c , d  =arr[i + 0] , arr[i + 1], arr[i + 2] , arr[i + 3]
        i += 4
        phuc_a = SoPhuc(a , b)
        phuc_b = SoPhuc(c , d)
        print("{}, {}".format(phuc_a.cong(phuc_b).nhan(phuc_a) , phuc_a.cong(phuc_b).nhan(phuc_a.cong(phuc_b))))