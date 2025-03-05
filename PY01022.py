def tinhTongChuSo(s):
    if len(s) == 1: return 1
    dem  = 0
    while len(s) != 1:
        dem += 1
        tong = 0
        for i in range(len(s)):
            tong += (ord(s[i]) - ord("0"))
        s = str(tong)
    return dem
if __name__ == "__main__":
    s = input()
    print(tinhTongChuSo(s))