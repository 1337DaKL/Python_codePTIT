def tinhGiaTriXoay(s):
    tong = 0
    for i in range(len(s)):
        tong = tong + int(ord(s[i])) - int(ord('A'))
    return tong
def rotate(s):
    xoay = tinhGiaTriXoay(s)
    sKetQua = ""
    for i in range(len(s)):
        indexAscii = (ord(s[i]) - ord("A")+ xoay) % 26
        sKetQua = sKetQua + chr(ord("A") + indexAscii)
    return sKetQua
def merge(s1 , s2):
    sKetQua  = ""
    for i in range(len(s1)):
        xoay = (ord(s1[i]) - ord("A") + ord(s2[i]) - ord("A")) % 26
        sKetQua = sKetQua + chr(ord("A") + xoay)
    return sKetQua
if __name__ == "__main__":
    test = int(input())
    for _ in range(test):
        s = input()
        print(merge(rotate(s[0 : len(s) // 2]), rotate(s[len(s)// 2 :len(s) ])))