def tinhTich(s):
    tich = 1
    check = True
    for i in range(0 , len(s), 2 ):
        if s[i] != '0':
            check = False
            tich *= int(s[i])
    if check : return 0
    return tich
def tinhTong(s):
    tong = 0
    for i in range(1 , len(s) , 2):
        tong += int(s[i])
    return tong
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        print(tinhTich(s), tinhTong(s), sep=" " )
# 3
# 12345678
# 20000
# 22334455667788