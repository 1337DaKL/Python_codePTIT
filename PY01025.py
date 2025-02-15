s = input()
sKetQua = ""
for i in range(len(s) - 1 , -1 , -3):
    if i - 3 >= 0:
        sKetQua = "," + s[i - 2 : i + 1] + sKetQua
    else :sKetQua = s[:i + 1] + sKetQua
print(sKetQua)