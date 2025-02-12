def kiemTraSoDep(s) :
    dem4 = 0
    dem7 = 0
    for i in range(len(s)) :
        if s[i] == '4' :
            dem4 += 1
        if s[i] == '7' :
            dem7 += 1
    tong = dem4 + dem7
    if tong == 4 or tong == 7:
        return  True
    return False
if __name__ == "__main__" :
    s = input()
    if(kiemTraSoDep(s)) :
        print("YES")
    else :
        print("NO")
