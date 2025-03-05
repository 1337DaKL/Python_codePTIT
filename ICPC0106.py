from math import *
def doiCoSo(s , n):
    coSo = int(log(n , 2))
    while len(s) % coSo != 0 :
        s = "0" + s
    cosoN = ""
    for i in range(0 , len(s) - coSo + 1 , coSo):
        nhiPhan = s[i : i + coSo]
        tong = 0
        for j in range(len(nhiPhan)):
            if nhiPhan[j] == "1":
                tong += (2 ** (coSo - j - 1))
        if tong >= 10: cosoN = cosoN + chr(ord("A") + tong - 10)
        else : cosoN += str(tong)
    return cosoN
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        n = int(input())
        s = input()
        print(doiCoSo(s ,n))
# 2
# 8
# 10010100010010101
# 2
# 10010100010010101