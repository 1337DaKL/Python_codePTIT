def kiemTraSoKhongGiam(s) :
    for i in range(1 , len(s) , 1) :
        if int(s[i]) < int(s[i - 1]):
            return  False
    return True
if __name__ == "__main__" :
    test = int(input())
    for _ in range(test):
        s = input()
        if kiemTraSoKhongGiam(s) :
            print("YES")
        else :
            print("NO")