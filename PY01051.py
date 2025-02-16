def tongChuSo(s):
    tong = 0
    for i in range(len(s)):
        tong += int(s[i])
    return str(tong)
def kiemTraThuanNghich(s):
    tong = tongChuSo(s)
    if len(tong) <= 1 : return False
    for i in range(int(len(tong) / 2)):
        if tong[i] != tong[len(tong) - i - 1]: return False
    return True
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraThuanNghich(s) : print("YES")
        else: print("NO")