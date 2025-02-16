def tinhTong(s):
    tong = 0
    for i in range(len(s)):
        if i % 2 == 0:
            tong += int(s[i])
    return tong
def tinhTich(s):
    check = True
    for i in range(1 , len(s) , 2):
        if s[i] != '0': check = False
    if check : return 0
    tich = 1
    for i in range(1 , len(s) , 2):
        if s[i] != '0' : tich *= int(s[i])
    return tich
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        print(tinhTong(s), tinhTich(s), sep = " " , end = "\n")
# 3
# 12345678
# 20000
# 22334455667788
