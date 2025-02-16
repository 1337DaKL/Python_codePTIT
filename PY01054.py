def tinhTich(s):
    tich = 1
    for i in range(len(s)):
        if s[i] != '0':
            tich *= int(s[i])
    return tich
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        print(tinhTich(s))
# 2
# 123410
# 123456789123456789