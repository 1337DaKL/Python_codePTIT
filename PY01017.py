check = True
p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while check :
    s = input()
    if s == "0" :
        check = False
    else :
        n , ss = s.split()
        sKetQua = ""
        indexAscii = -1
        for i in range(len(ss)) :
            if(ss[i] == "_") : indexAscii = 26
            elif ss[i] == "." : indexAscii = 27
            else : indexAscii = ord(ss[i]) - ord("A")
            indexAscii = (int(n) + indexAscii) % 28
            sKetQua = p[indexAscii] + sKetQua
        print(sKetQua)