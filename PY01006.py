def kiemTraSDep(s) :
    for i in range(0 , len(s) , 1) :
        if s[i] != '4' and s[i] != '7' :
            return False
    return True

if __name__ == "__main__" :
    test = int(input())
    for _ in range(test) :
        s = input()
        if kiemTraSDep(s) :
            print("YES")
        else :
            print("NO")