def tinhTongChuSo(s) :
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return tong
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if tinhTongChuSo(s) % 3 == 0 : print("YES")
        else : print("NO")