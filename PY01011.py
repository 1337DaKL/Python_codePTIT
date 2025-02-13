def kiemTraSoThuanNghich(s) :
    for i in range(0 , len(s) , 1) :
        if(s[i] != '0' and s[i] != '2' and s[i] != '4' and s[i] != '6' and s[i] != '8') : return False
        if len(s) % 2 == 1: return False
        if(s[i] != s[len(s) - i - 1]) : return False
    return True

if __name__ == "__main__" :
    test = int(input())
    for _ in range(test) :
        n = int(input())
        for i in range(n) :
            if kiemTraSoThuanNghich(str(i)) :
                print(i , end = " ")
        print()